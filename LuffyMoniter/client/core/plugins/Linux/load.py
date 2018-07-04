#!/usr/bin/env python
#coding:utf-8

import os,sys
import datetime
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)

from plugins.base import BasePlugin

def monitor(frist_invoke=1,**kwargs):
    for i,v in kwargs.items():
        ip = i
        username = v[0]
        passwd = v[1]
        port = v[2]
<<<<<<< HEAD
    shell_command = 'uptime'

=======
    print(ip,username,port,passwd)
    shell_command = 'uptime'
>>>>>>> 6ecfbf47f8803bc2f0083c090b9bb3c2d7d16b96
    contents = BasePlugin(ip,port,username,passwd).exec_shell_cmd(shell_command)
    run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
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
            'ip':ip,
            'uptime': uptime,
            'load1': load1,
            'load5': load5,
            'load15': load15,
            'time': run_time,
            'status': status
        }
    return value_dic

if __name__ == '__main__':
    host_message = {'192.168.2.128': ['root', 'oracle', 22]}
    a = monitor(**host_message)
    print(a)

