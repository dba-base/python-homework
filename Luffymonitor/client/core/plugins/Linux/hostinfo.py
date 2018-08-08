#!/usr/bin/env python
#coding:utf-8
import os,sys
import threading
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)

from plugins.base import BasePlugin

hostinfo_li = []

def monitor(**kwargs):

    shell_command = 'uanme -a'
    print(kwargs)
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
        contents['ERROR'] = 0
    else:
        contents['ERROR'] = 1
    status = contents['ERROR']

    if status != 0:
        value_dic["ip_addr"] = ip
        value_dic["enabled"] = 0
        value_dic["hostname"] = "NULL"
    else:
        li = contents['RESULT'].split("\n")  # 字符串转列表
        content_list = li[:len(li) - 1]  # 取列表开始到倒数第二个元素，最后一个元素为空
        value_dic["ip_addr"] = ip
        value_dic["enabled"] = 1
        value_dic["hostname"] = contents['RESULT'].strip()
    hostinfo_li.append(value_dic)


# if __name__ == '__main__':
#     kwargs={'192.168.2.128': ['root', 'oracle', 22, 'scott', 'tiger', 'prod', 1521],
#      '192.168.2.129': ['root', 'oracle', 22, 'scott', 'tiger', 'prod', 1521]}
#     a=monitor(**kwargs)
#     print(a)