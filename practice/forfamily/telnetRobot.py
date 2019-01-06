#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pexpect
import logging

LOG_FORMAT = '%(asctime)s - %(filename)s[L%(lineno)d] - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

def get_information_by_rt(rt):
    '''
    根据提案号一次性获取有用的信息
    :param rt:
    :return:
    '''
    info = {}
    info['cmd'] = ''
    info['port'] = '8080'
    info['ip'] = '192.168.1.1'
    return info

def get_dividing_vlan_cmd(rt):
    '''
    获取自动划分vlan的命令
    :param rt: 提案号
    :return: 自动划分vlan的命令
    '''
    dividingVlanCmd = ''
    return dividingVlanCmd

def get_check_port(rt):
    '''
    获取待检查的端口
    :param rt:
    :return:
    '''
    port = '8080'
    return port

def get_switchIP(rt):
    '''
    获取交换机的IP
    :param rt:
    :return:
    '''
    ip = '192.168.1.1'
    return ip

def check_port_down(child, port):
    '''
    检查端口是否down
    :param child: telnet登陆成功的操作句柄
    :param port: 端口
    :return:
    '''
    # todo 判断端口是否DOWN
    return True

def get_telnet_username_password(ip):
    '''
    获取交换机的用户名密码
    :param ip: 交换机IP
    :return: （用户名，密码）
    '''
    element = {}
    element['username'] = 'username'
    element['password'] = 'password'
    return element

def telnet_login(ip, username, password):
    '''
    telnet 登陆
    :param ip: 交换机IP
    :param username: 用户名
    :param password: 密码
    :return: telnet登陆成功的操作句柄（None为登陆失败）
    '''
    cmd = 'telnet ' + ip
    loginprompt = '[$#>]'
    child = pexpect.spawn(cmd)
    index = child.expect(["login", "(?i)Unknown host", pexpect.EOF, pexpect.TIMEOUT])
    if index == 0:
        # 匹配'login'字符串成功，输入用户名.
        child.sendline(username)
        # 期待 "[pP]assword" 出现.
        index = child.expect(["[pP]assword", pexpect.EOF, pexpect.TIMEOUT])
        # 匹配 "[pP]assword" 字符串成功，输入密码.
        child.sendline(password)
        # 期待提示符出现.
        index = child.expect(loginprompt)
        if index == 0:
            return child
        else:
            logging.warn("!!!! telnet login [%s] failed, due to TIMEOUT or EOF" % ip)
            child.close(force=True)
            return None
    else:
        logging.warn("!!!! telnet login [%s] failed, due to TIMEOUT or EOF" % ip)
        child.close(force=True)
        return None

def divide_vlan(child,rt):
    '''
    执行划分VLAN
    :param child:
    :param cmd:
    :return:
    '''
    dividingVlanCmd = get_dividing_vlan_cmd(rt)
    # todo 执行划分VLAN

def auto_vlan(rt):
    '''
    自动划分Vlan
    :param rt: 提案号
    :param ip: 交换机IP
    :return:
    '''
    logging.info('@@@@ prepare auto dividing vlan for rt[%s]' % rt)
    switchIp = get_switchIP(rt)
    element = get_telnet_username_password(switchIp)
    username = element['username']
    password = element['password']
    child = telnet_login(switchIp, username, password)
    if child is not None:
        port = get_check_port(rt)
        if check_port_down(child, port):
            # 满足端口DOWN的条件
            divide_vlan(child, rt)
        else:
            logging.info('@@@@ the rt[%s] port is UP, nothing done' % rt)
        # 关闭操作句柄
        child.close(force=True)

if __name__ == '__main__':
    rt = '10086'
    auto_vlan(rt)