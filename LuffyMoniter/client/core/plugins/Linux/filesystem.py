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
    shell_command ="df -m | sed '1d'"
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
        value_dic['ip'] = ip
        li=contents['RESULT'].split("\n")  # 字符串转列表
        content_list = li[:len(li)-1]      # 取列表开始到倒数第二个元素，最后一个元素为空

        #列表转字典
        for i in content_list:
            key= i.split()[5].strip(':') # factor name 取得挂载点
            value = i.split()[1:4]   # factor value
            value_dic[key] = value

        value_dic['time'] = run_time
        value_dic['status'] = status

    return value_dic

if __name__ == '__main__':
    # for i in range(3):
        host_message = {'192.168.2.128': ['root', 'oracle', 22]}
        a = monitor(**host_message)
        print(a)