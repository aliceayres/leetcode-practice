import itchat
from itchat.content import *
import datetime
import xlrd
from xlrd import xldate_as_tuple
import os
import configparser

# 全局变量
# 是否打印debug日志
global debug
debug = True
# 配置文件名称
global global_config_filename
global_config_filename = "autoreply_config.ini"
# 文件上次更新时间缓存
global file_mtime_cache
file_mtime_cache = {}
# 群聊名称白名单缓存
global global_nickname_whitelist
global_nickname_whitelist = {}
# 触发关键字缓存
global keyword_cache
keyword_cache = {}
# 机房值班信息表格名称
global duty_excel_filename
# all_duty状态自动回复标题
global all_duty_title
# 机房值班信息缓存
global duty_cache
duty_cache = {} # 日期 机房 值班人员

# 重新加载机房值班人员缓存
def reloadDutyCache():
    global debug
    if debug:
        print("#### Reloading Duty cache...")
    global duty_excel_filename
    workbook = xlrd.open_workbook(duty_excel_filename)
    all_sheets = workbook.sheet_names()
    sheet = workbook.sheet_by_name(all_sheets[0])
    rows = sheet.nrows
    global duty_cache
    duty_cache = {}
    for i in range(1, rows):
        cell = sheet.cell_value(i, 0)
        date = xldate_as_tuple(cell, 0)
        duty_date = datetime.datetime(*date).strftime('%Y/%m/%d')
        room = sheet.cell_value(i, 1)
        engineer = sheet.cell_value(i, 2)
        if engineer is None or engineer == '':
            continue
        if duty_cache.get(duty_date) is None:
            duty_cache[duty_date] = {}
            duty_cache[duty_date][room] = engineer
        else:
            if duty_cache[duty_date].get(room) is None:
                duty_cache[duty_date][room] = engineer
    # for dt in duty_cache.items():
    #     print(dt)

# 重新加载配置文件相关缓存
def reloadAutoreplyConfig():
    global debug
    if debug:
        print("#### Reloading Autoreply Config cache...")
    conf = configparser.ConfigParser()
    global global_config_filename
    conf.read(global_config_filename,encoding='UTF-8')
    # 白名单
    whitelist_nickname_config = conf.get("whitelist", "nickname")
    white_nicknames = whitelist_nickname_config.split(',')
    global global_nickname_whitelist
    global_nickname_whitelist = {}
    for nick in white_nicknames:
        global_nickname_whitelist[nick] = 0
    # 关键字
    global keyword_cache
    keyword_cache = {}
    keyword_cache["all_duty"] = conf.get("state_keyword", "all_duty")
    keyword_cache["some_duty"] = conf.get("state_keyword", "some_duty")
    # excel名称
    global duty_excel_filename
    duty_excel_filename = conf.get("duty_excel", "filepath") + conf.get("duty_excel", "filename")
    # all_duty回复标题
    global all_duty_title
    all_duty_title = conf.get("reply_title", "all_duty")

# 判断文件是否更新过
def hasModified(filename):
    modified = False
    modify_time = os.stat(filename).st_mtime
    global file_mtime_cache
    if file_mtime_cache.get(filename) is None:
        file_mtime_cache[filename] = modify_time
        modified = True
    else:
        last = file_mtime_cache.get(filename)
        modified = modify_time != last
    global debug
    if debug:
        if modified:
            print("#### File[%s] has been modified!!!" % filename)
    return modified

# 判断群聊是否在白名单
def inWhitelist(chatroom):
    return checkCompleteNicknameWhitelist(chatroom)

# 通过群聊名称完全匹配白名单
def checkCompleteNicknameWhitelist(chatroom):
    chatroom_nickname = chatroom['NickName']
    global global_nickname_whitelist
    return global_nickname_whitelist.get(chatroom_nickname) is not None

class State(object):
    def handle(self,context):
        pass

# 自动回复今日所有机房值班信息
class AllDutyState(State):
    def handle(self, context):
        msg = context.msg
        chatroom = msg['User']
        global debug
        if debug:
            print("@@@@ White list chatroom received a all duty message : " + msg['Content'])
            print("@@@@ Chatroom username: " + chatroom['UserName'])
            print("@@@@ Chatroom nickname: " + chatroom['NickName'])
        global duty_excel_filename
        if hasModified(duty_excel_filename):
            reloadDutyCache()
        global duty_cache
        today = datetime.date.today().strftime('%Y/%m/%d')
        if duty_cache.get(today) is not None:
            global all_duty_title
            reply = all_duty_title.format(current=today)
            reply += '\n --------------------------\n'
            today_duty = duty_cache.get(today)
            for item in today_duty.items():
                reply += '· ' + item[0] + '：' + item[1] + '\n'
            if debug:
                print("@@@@ Reply message:\n %s" % reply)
            itchat.send_msg(reply, msg['FromUserName'])

# 暂无处理
class SomeDutyState(State):
    def handle(self, context):
        return

# 默认状态无处理
class DefaultState(State):
    def handle(self, context):
        return

# 关键字状态上下文
class KeywordContext():
    def __init__(self,state,msg):
        self.state = state
        self.msg = msg

    def replyContent(self):
        return self.state.handle(self)

# Wechat群聊消息回调, 实现关键字自动回复
@itchat.msg_register([PICTURE,TEXT], isGroupChat=True)
def autoReply(msg):
    chatroom = msg['User']
    global global_config_filename
    if hasModified(global_config_filename):
        reloadAutoreplyConfig()
    # 群聊是否在白名单中
    if inWhitelist(chatroom):
        # 自动回复
        if msg['Type'] == TEXT:
            content = msg['Content']
            reply_context = KeywordContext(DefaultState(), msg)
            global keyword_cache
            # 根据content内容分发到状态处理
            # 判断是否属于all_duty状态触发消息
            if content == keyword_cache["all_duty"]:
                reply_context.state = AllDutyState()
            # 判断是否属于some_duty状态触发消息
            # if content.find(keyword_cache["some_duty"]):
            #     split_contents = content.split(' ')
            #     if split_contents[-1] == keyword_cache["some_duty"]:
            #         reply_context.state = SomeDutyState()
            # 实际处理消息
            reply_context.replyContent()

itchat.auto_login(True)
itchat.run()