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
    monitor_dic = {
        'SwapUsage': 'percentage',
        'MemUsage'  : 'percentage',
    }
    shell_command ="grep 'MemTotal\|MemFree\|Buffers\|^Cached\|SwapTotal\|SwapFree' /proc/meminfo"
    contents = BasePlugin(ip,port,username,passwd).exec_shell_cmd(shell_command)
<<<<<<< HEAD
    run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
=======

<<<<<<< HEAD
    contents = BasePlugin(ip,port,username,passwd).exec_shell_cmd(shell_command)
=======
>>>>>>> 6ecfbf47f8803bc2f0083c090b9bb3c2d7d16b96
>>>>>>> d841c496728554b89a5f20e1073fbaf9b852716a
    if contents['ERROR'] == "" :
        contents['ERROR'] = 0
    else:
        contents['ERROR'] = 1
    status = contents['ERROR']
    if status != 0: #cmd exec error
        value_dic = {'status':status}
    else:
        value_dic = {}
        value_dic['ip'] = ip
        li=contents['RESULT'].split("\n")  # 字符串转列表
        content_list = li[:len(li)-1]      # 取列表开始到倒数第二个元素，最后一个元素为空
        #列表转字典
        for i in content_list:
            key= i.split()[0].strip(':') # factor name
            value = i.split()[1]   # factor value
            value_dic[key] = value
        run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        if monitor_dic['SwapUsage'] == 'percentage':
            value_dic['SwapUsage_p'] = str(100 - int(value_dic['SwapFree']) * 100 / int(value_dic['SwapTotal']))
        #real SwapUsage value
        value_dic['SwapUsage'] = int(value_dic['SwapTotal']) - int(value_dic['SwapFree'])

        MemUsage = int(value_dic['MemTotal']) - (int(value_dic['MemFree']) + int(value_dic['Buffers'])  + int(value_dic['Cached']))
        if monitor_dic['MemUsage'] == 'percentage':
            value_dic['MemUsage_p'] = str(int(MemUsage) * 100 / int(value_dic['MemTotal']))
        #real MemUsage value
        value_dic['MemUsage'] = MemUsage
        value_dic['status'] = status
        value_dic['time']  = run_time

    return value_dic

# if __name__ == '__main__':
#     for i in range(3):
#         host_message = {'192.168.2.128': ['root', 'oracle', 22]}
#         a = monitor(**host_message)
#         print(a)