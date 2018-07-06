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

    shell_command = 'uptime'

    contents = BasePlugin(**kwargs).exec_shell_cmd(shell_command)
    run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    # print(contents)
    # print(type(contents))
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
        days = content_list[0].split(',')[0].split()[2]   #运行天数
        hours_li = content_list[0].split(',')[1].strip().split(':')   #运行小时
        runtime = days + '天' + hours_li[0] + '时' + hours_li[1] + '分'
        users = content_list[0].split(',')[2].split()[0]
        load1,load5,load15 = content_list[0].split('load average:')[1].split()

        value_dic= {
            'ip':ip,
            'runtime': runtime,
            'users': users,
            'load1': float(load1.strip(',')),
            'load5': float(load5.strip(',')),
            'load15': float(load15),
            'time': run_time,
            'status': status
        }
    return value_dic
#
# if __name__ == '__main__':
#     host_message = {'192.168.2.128': ['root', 'oracle', 22]}
#     a = monitor(**host_message)
#     print(a)

