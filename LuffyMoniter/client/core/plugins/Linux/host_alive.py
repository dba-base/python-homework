#_*_coding:utf-8_*_
__author__ = 'Alex Li'

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
    value_dic = {}
    shell_command = 'uptime'
<<<<<<< HEAD
    contents = BasePlugin(ip, port, username, passwd).exec_shell_cmd(shell_command)
=======
    contents = BasePlugin(ip,port,username,passwd).exec_shell_cmd(shell_command)
    run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    # contents = BasePlugin('192.168.2.128', 22, 'root', 'oracle').exec_shell_cmd(shell_command)
<<<<<<< HEAD
    if contents['ERROR'] == "" :
        contents['ERROR'] = 0
    else:
        contents['ERROR'] = 1
    status = contents['ERROR']
=======
>>>>>>> 6ecfbf47f8803bc2f0083c090b9bb3c2d7d16b96
>>>>>>> d841c496728554b89a5f20e1073fbaf9b852716a

    if status != 0:
        value_dic = {'status': status}
    #user,nice,system,iowait,steal,idle = result.split()[2:]
    else:
        value_dic= {
            'ip':ip,
            'uptime': contents['RESULT'],
            'time':run_time,
            'status': 0
        }
    return value_dic

# if __name__ == '__main__':
#     host_message = {'192.168.2.128': ['root', 'oracle', 22]}
#     a = monitor(**host_message)
#     print(a)