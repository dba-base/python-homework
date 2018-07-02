#_*_coding:utf-8_*_
__author__ = 'Alex Li'

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
    value_dic = {}
    shell_command = 'uptime'
    contents = BasePlugin(ip,port,username,passwd).exec_shell_cmd(shell_command)
    # contents = BasePlugin('192.168.2.128', 22, 'root', 'oracle').exec_shell_cmd(shell_command)

    #user,nice,system,iowait,steal,idle = result.split()[2:]
    value_dic= {
        'uptime': contents['RESULT'],
        'status': 0
    }
    return value_dic

