#!/usr/bin/env python
#coding:utf-8
import os,sys
import threading
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)

from plugins.base import BasePlugin
from conf import settings

hostinfo_li = []

def monitor(**kwargs):

    shell_command = 'ps -ef | grep smaon | grep -v grep;uname -sn'  # Linux hostname
    thread_list = []  # 线程存放列表
    for ip,v in kwargs.items():
        host_info = {ip: v}
        print(host_info)
        t = threading.Thread(target=exec_cmd, args=(shell_command,ip,host_info))
        t.setDaemon(True)   #设置线程为后台线程
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()


    return hostinfo_li

def exec_cmd(cmd,ip,kwargs):
    value_dic = {}
    contents = BasePlugin(**kwargs).exec_shell_cmd(cmd)
    if contents['ERROR'] == "":
        status = 0
    else:
        status = 1
    if status != 0:
        value_dic["ip_addr"] = ip
        value_dic["enabled"] = 0
        value_dic["hostname"] = "NULL"
        value_dic["comment"] = contents['ERROR']
    else:
        li = contents['RESULT'].split()  # 字符串转列表
        if li[0] in settings.os_type_choices:   #判断操作系统是否在列表中
            os_type = settings.os_type_choices.get(li[0])
        else:
            os_type = 3
        value_dic["ip_addr"] = ip
        value_dic["enabled"] = 1
        value_dic["os_type"] = os_type
        value_dic["hostname"] = li[1]
    hostinfo_li.append(value_dic)



# if __name__ == '__main__':
#     kwargs={'192.168.2.128': ['root', 'oracle', 22, 'scott', 'tiger', 'prod', 1521]}
#     # kwargs={'10.10.0.2': ['root', 'oracle', 22, 'scott', 'tiger', 'prod', 1521],'192.168.2.128': ['root', 'qqq', 22, 'scott', 'tiger', 'prod', 1521]}
#     # kwargs={'192.168.2.128': ['root', 'oracle', 22, 'scott', 'tiger', 'prod', 1521],'192.168.2.129': ['root', 'oracle', 22, 'scott', 'tiger', 'prod', 1521],'10.10.0.2': ['root', 'oracle', 22, 'scott', 'tiger', 'prod', 1521]}
#     a=monitor(**kwargs)
#     print(a)