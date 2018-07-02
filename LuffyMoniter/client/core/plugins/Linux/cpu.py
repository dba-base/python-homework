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
    print(ip,username,port,passwd)
    shell_command = 'sar 1 3| grep "^Average:"'
    contents = BasePlugin(ip,port,username,passwd).exec_shell_cmd(shell_command)
    if contents['ERROR'] == "" :
        contents['ERROR'] = 0
    else:
        contents['ERROR'] = 1
    status = contents['ERROR']

    if status != 0:
        value_dic = {'status': status}
    else:
        value_dic = {}
        print('---res:',contents['RESULT'])
        user,nice,system,iowait,steal,idle = contents['RESULT'].split()[2:]
        value_dic= {
            'user': user,
            'nice': nice,
            'system': system,
            'idle': idle,
            'status': status
        }
    return value_dic

# if __name__ == '__main__':
#     host_message = {'192.168.2.128': ['root', 'oracle', 22]}
#     a = monitor(**host_message)
#     print(a)