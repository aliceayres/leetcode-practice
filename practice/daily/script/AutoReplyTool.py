#!/usr/bin/python
# -*- coding: UTF-8 -*-

import itchat
from itchat.content import *
import datetime
import xlrd
from xlrd import xldate_as_tuple
import os
import configparser
from apscheduler.schedulers.background import BackgroundScheduler
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

LOG_FORMAT = '%(asctime)s - Thread[%(thread)s] - %(filename)s[L%(lineno)d] - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# 配置缓存
class ConfigCache():
    def __init__(self):
        self.config_filename = "autoreply_config.ini" # 配置文件名称
        self.file_mtime_cache = {} # 文件上次更新时间缓存
        self.nickname_whitelist = {} # 群聊名称白名单
        self.keyword_cache = {} # 触发关键字缓存
        self.duty_cache = {} # all_duty状态自动回复标题
        self.duty_excel_filename = None # 机房值班信息表格名称
        self.all_duty_title = None # 机房值班信息缓存: 日期 机房 值班人员
        self.receiver_mail = None # 接收二维码的邮箱
        self.mail_username = "autoreceivebox@163.com"
        self.mail_password = "111111auto"
        self.mail_hostname = "smtp.163.com"
        self.initCaches()

    def initCaches(self):
        '''
        初始化
        :return:
        '''
        logging.info("@@@@ Initializing global caches ...")
        if self.hasModified(self.config_filename):
            self.reloadAutoreplyConfig()
        if self.hasModified(self.duty_excel_filename):
            self.reloadDutyCache()

    def hasModified(self,filename):
        '''
        判断文件是否更新过
        :param filename:
        :return:
        '''
        is_modified = False
        modify_time = os.stat(filename).st_mtime
        if self.file_mtime_cache.get(filename) is None:
            is_modified = True
        else:
            last = self.file_mtime_cache.get(filename)
            is_modified = modify_time != last
        if is_modified:
            self.file_mtime_cache[filename] = modify_time
            logging.info("@@@@ File[%s] has been modified!!!" % filename)
        return is_modified

    def lookupConfigCache(self):
        '''
        更新配置文件缓存
        :return:
        '''
        if self.hasModified(self.config_filename):
            self.reloadAutoreplyConfig()

    def lookupDutyCache(self):
        '''
         更新值班文件缓存
        :return:
        '''
        if self.hasModified(self.duty_excel_filename):
            self.reloadDutyCache()

    def reloadAutoreplyConfig(self):
        '''
        重新加载配置文件相关缓存
        :return:
        '''
        logging.info("@@@@ Reloading Autoreply Config cache...")
        conf = configparser.ConfigParser()
        conf.read(self.config_filename, encoding='UTF-8')
        # 白名单
        whitelist_nickname_config = conf.get("whitelist", "nickname")
        white_nicknames = whitelist_nickname_config.split(',')
        self.nickname_whitelist = {}
        for nick in white_nicknames:
            self.nickname_whitelist[nick] = 0
        # 关键字
        self.keyword_cache = {}
        all_duty_keyword_config = conf.get("state_keyword", "all_duty")
        all_duty_keywords = all_duty_keyword_config.split(',')
        self.keyword_cache["all_duty"] = {}
        for key in all_duty_keywords:
            self.keyword_cache["all_duty"][key] = 0
        self.keyword_cache["some_duty"] = conf.get("state_keyword", "some_duty")
        # excel名称
        self.duty_excel_filename = conf.get("duty_excel", "filepath") + conf.get("duty_excel", "filename")
        # all_duty回复标题
        self.all_duty_title = conf.get("reply_title", "all_duty")
        # 接收二维码的邮箱
        self.receiver_mail = conf.get("mail","receiver")

    def reloadDutyCache(self):
        '''
        重新加载机房值班人员缓存
        :return:
        '''
        logging.info("@@@@ Reloading Duty cache...")
        workbook = xlrd.open_workbook(self.duty_excel_filename)
        all_sheets = workbook.sheet_names()
        sheet = workbook.sheet_by_name(all_sheets[0])
        rows = sheet.nrows
        self.duty_cache = {}
        for i in range(1, rows):
            cell = sheet.cell_value(i, 0)
            date = xldate_as_tuple(cell, 0)
            duty_date = datetime.datetime(*date).strftime('%Y/%m/%d')
            room = sheet.cell_value(i, 1)
            engineer = sheet.cell_value(i, 2)
            if engineer is None or engineer == '':
                continue
            if self.duty_cache.get(duty_date) is None:
                self.duty_cache[duty_date] = {}
                self.duty_cache[duty_date][room] = engineer
            else:
                if self.duty_cache[duty_date].get(room) is None:
                    self.duty_cache[duty_date][room] = engineer
                    # for dt in duty_cache.items():
                    #     print(dt)

# 微信处理类
class WechatHandler():
    def __init__(self):
        self.cache = ConfigCache()

    def getChatRoomUserName(self, nickname):
        '''
        获取群聊唯一标识
        :param nickname:
        :return:
        '''
        # rooms = itchat.get_chatrooms(update=True)
        rooms = itchat.search_chatrooms(name=nickname)
        if rooms is not None and len(rooms) > 0:
            return rooms[0]['UserName']
        return None

    def inWhitelist(self, chatroom):
        '''
        判断群聊是否在白名单
        :param chatroom:
        :return:
        '''
        return self.checkCompleteNicknameWhitelist(chatroom)

    def checkCompleteNicknameWhitelist(self, chatroom):
        '''
        通过群聊名称完全匹配白名单
        :param chatroom:
        :return:
        '''
        chatroom_nickname = chatroom['NickName']
        return self.cache.nickname_whitelist.get(chatroom_nickname) is not None

    def autoReplyAllDuty(self, msg):
        '''
        自动回复值班信息
        :param msg:
        :return:
        '''
        chatroom = msg['User']
        logging.info("@@@@ White list chatroom received a all duty message : %s" % msg['Content'])
        reply = self.getAllDutyMsg()
        if reply is not None:
            # logging.info("@@@@ Reply message:\n %s" % reply)
            starttime = datetime.datetime.now()
            logging.info("@@@@ Autoreplied all duty msg to [%s][%s] chatroom " % (chatroom['UserName'], chatroom['UserName']))
            itchat.send_msg(reply, chatroom['UserName'])  # msg['FromUserName']
            endtime = datetime.datetime.now()
        logging.info("@@@@ Send reply cost %s seconds" % str((endtime - starttime)))

    def getAllDutyMsg(self):
        '''
        获取当日值班信息
        :return:
        '''
        self.cache.lookupDutyCache()
        today = datetime.date.today().strftime('%Y/%m/%d')
        if self.cache.duty_cache.get(today) is not None:
            reply = self.cache.all_duty_title.format(current=today)
            reply += '\n --------------------------\n'
            today_duty = self.cache.duty_cache.get(today)
            for item in today_duty.items():
                reply += '· ' + item[0] + '：' + item[1] + '\n'
            return reply
        return None

    def broadcastAllDuty(self):
        '''
        广播值班信息
        :return:
        '''
        for white in self.cache.nickname_whitelist:
            username = wechatHandler.getChatRoomUserName(white)
            if username is None:
                continue
            msg = self.getAllDutyMsg()
            logging.info("@@@@ Broadcast all duty msg to [%s][%s] chatroom " % (white,username))
            itchat.send_msg(msg, username)

    def handleQrcode(self,qrcode,uuid,status):
        '''
        处理二维码
        :param qrcode:
        :param uuid:
        :param status:
        :return:
        '''
        global notSendQrcode
        if notSendQrcode and len(qrcode) != 0:
            logging.info('@@@@ Saving QR image and send email ...')
            with open('QR.png', 'wb') as f:
                f.write(qrcode)
            self.sendQrcodeMail(qrcode)
            notSendQrcode = False

    def sendQrcodeMail(self,qrimage):
        '''
        发送登录二维码到邮箱
        :param qrimage:
        :return:
        '''
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = "自动回复登录二维码"
        msgRoot['From'] = self.cache.mail_username
        msgRoot['To'] = self.cache.receiver_mail
        msgText = MIMEText('<b>您的微信机器人需要重新扫码登录.</b><br><img src="cid:qrimage">', 'html', 'utf-8')
        msgRoot.attach(msgText)
        msgImage = MIMEImage(qrimage)
        msgImage.add_header('Content-ID', '<qrimage>')
        msgRoot.attach(msgImage)
        smtp = smtplib.SMTP()
        smtp.connect(self.cache.mail_hostname)
        smtp.login(self.cache.mail_username, self.cache.mail_password)
        smtp.sendmail(self.cache.mail_username, self.cache.receiver_mail, msgRoot.as_string())
        smtp.quit()

    def textMsgRegister(self,msg):
        '''
        处理来自微信的群聊文本消息
        :param msg:
        :return:
        '''
        chatroom = msg['User']
        self.cache.lookupConfigCache()
        # 群聊是否在白名单中
        if self.inWhitelist(chatroom):
            starttime = datetime.datetime.now()
            # 自动回复
            if msg['Type'] == TEXT:
                content = msg['Content']
                reply_context = KeywordContext(DefaultState(), msg, self)
                # 根据content内容分发到状态处理
                # 判断是否属于all_duty状态触发消息
                if self.cache.keyword_cache["all_duty"].get(content) is not None:
                    reply_context.state = AllDutyState()
                # 判断是否属于some_duty状态触发消息
                # if content.find(keyword_cache["some_duty"]):
                #     split_contents = content.split(' ')
                #     if split_contents[-1] == keyword_cache["some_duty"]:
                #         reply_context.state = SomeDutyState()
                # 实际处理消息
                reply_context.handle()
            endtime = datetime.datetime.now()
            logging.info("@@@@ Run cost %s seconds" % str((endtime - starttime)))

class State(object):
    def handle(self,context):
        pass

class AllDutyState(State):
    def handle(self, context):
        # 自动回复今日所有机房值班信息
        wechatHandler = context.wechatHandler
        wechatHandler.autoReplyAllDuty(context.msg)

class SomeDutyState(State):
    def handle(self, context):
        # 暂无处理
        return

class DefaultState(State):
    def handle(self, context):
        # 默认状态无处理
        return

# 关键字状态上下文
class KeywordContext():
    def __init__(self,state,msg,wechatHandler):
        self.state = state
        self.msg = msg
        self.wechatHandler = wechatHandler

    def handle(self):
        return self.state.handle(self)

global wechatHandler
wechatHandler = WechatHandler()

@itchat.msg_register([TEXT], isGroupChat=True)
def autoReply(msg):
    '''
    Wechat群聊消息回调, 实现关键字自动回复
    :param msg:
    :return:
    '''
    global wechatHandler
    wechatHandler.textMsgRegister(msg)

def dailyScheduledBroadcast():
    '''
    定时任务广播值班信息
    :return:
    '''
    logging.info('@@@@ Schedule job triggered ...')
    global wechatHandler
    wechatHandler.broadcastAllDuty()

def keepAlive():
    itchat.send_msg('保活信息', 'filehelper')

def runScheduler():
    '''
    启动定时任务不能
    :return:
    '''
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=dailyScheduledBroadcast, trigger='cron', day_of_week='0-6', hour=9, minute=0, second=0)
    scheduler.add_job(func=keepAlive, trigger='interval',seconds = 600)
    scheduler.start()
    logging.info('@@@@ Background Scheduler started!!!')

def logoutCallback():
    logging.info('@@@@ logout callback...')

def qrCodeCallback(uuid, status, qrcode):
    global wechatHandler
    wechatHandler.handleQrcode(qrcode,uuid,status)

if __name__ == '__main__':
    while True:
        global notSendQrcode
        notSendQrcode = True
        # itchat.auto_login(hotReload=True,loginCallback=runScheduler,exitCallback=logoutCallback)
        # itchat.auto_login(hotReload=True,enableCmdQR=1,loginCallback=runScheduler,exitCallback=logoutCallback)
        itchat.auto_login(hotReload=True,loginCallback=runScheduler,exitCallback=logoutCallback,qrCallback=qrCodeCallback)
        itchat.dump_login_status()
        itchat.run(debug=False)
        logging.info('@@@@ itchat run end！')
    logging.info('@@@@ __main__ end！')