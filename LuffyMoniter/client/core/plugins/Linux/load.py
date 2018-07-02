#!/usr/bin/env python
#coding:utf-8

import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)

from plugins.base import BasePlugin


def monitor(frist_invoke=1,**kwargs):
    for i,v in kwargs.items():
        ip = i
        username = v[0]
        passwd = v[1]
        port = v[2]
    shell_command = 'uptime'

    contents = BasePlugin(ip,port,username,passwd).exec_shell_cmd(shell_command)

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
        # 列表转字典
        uptime = content_list[0].split(',')[:1][0]

        load1,load5,load15 = content_list[0].split('load average:')[1].split()
        print(load1,load5,load15)
        value_dic= {
            'uptime': uptime,
            'load1': load1,
            'load5': load5,
            'load15': load15,
            'status': status
        }
    return value_dic


