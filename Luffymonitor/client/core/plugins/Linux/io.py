#!/usr/bin/env python
#coding:utf-8
import os,sys
import datetime
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)

from plugins.base import BasePlugin


'''
iostat -c  | grep -v avg | grep '[^/s]' | grep -v Li | awk  '{print $4}'
'''


def monitor(frist_invoke=1,**kwargs):
    for i,v in kwargs.items():
        ip = i

    #print(ip,username,port,passwd)

    shell_command = 'sar -d 1 3| grep "^Average:"'
    contents = BasePlugin(**kwargs).exec_shell_cmd(shell_command)
    if contents['ERROR'] == "" :
        contents['ERROR'] = 0
    else:
        contents['ERROR'] = 1
    status = contents['ERROR']

    if status != 0:
        value_dic = {'ip': ip,'status': status}
    else:
        value_dic = {}
        run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        #print('---res:',contents['RESULT'])
        user,nice,system,iowait,steal,idle = contents['RESULT'].split()[2:]
        value_dic= {
            'ip': ip,
            'user': user,
            'nice': nice,
            'system': system,
            'idle': idle,
            'time': run_time,
            'status': status
        }
    return value_dic

# if __name__ == '__main__':
#     for i in range(2):
#         host_message = {'192.168.2.128': ['root', 'oracle', 22, 'scott', 'tiger','prod', 1521]}
#         a = monitor(**host_message)
#         print(a)
