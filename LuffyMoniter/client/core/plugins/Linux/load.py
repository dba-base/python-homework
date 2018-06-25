#!/usr/bin/env python
#coding:utf-8

import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)

from plugins.base import BasePlugin


def monitor():
    shell_command = 'uptime'

    contents = BasePlugin('192.168.2.128',22,'root','oracle').exec_shell_cmd(shell_command)

    if contents['ERROR'] == "" :
        contents['ERROR'] = 0
    else:
        contents['ERROR'] = 1
    status = contents['ERROR']
    if status != 0: #cmd exec error
        value_dic = {'status':status}
    else:
        value_dic = {}
        li = contents['RESULT'].split("\n")  # 字符串转列表
        content_list = li[:len(li) - 1]
        print(content_list[0])
        # 列表转字典
        uptime = content_list[0].split(',')[:1][0]
        print(uptime)
        print(type(content_list[0]))   #str
        load1,load5,load15 = content_list[0].split('load averages:')[1].split()
        print(load1,load5,load15)
        value_dic= {
            #'uptime': uptime,
            'load1': load1,
            'load5': load5,
            'load15': load15,
            'status': status
        }
    return value_dic



print(monitor())
