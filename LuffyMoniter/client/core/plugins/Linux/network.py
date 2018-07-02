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
    shell_command = 'sar -n DEV 1 5 |grep -v IFACE |grep Average'
<<<<<<< HEAD
    contents = BasePlugin(ip,port,username,passwd).exec_shell_cmd(shell_command)
=======
    contents = BasePlugin(ip, port, username, passwd).exec_shell_cmd(shell_command)
>>>>>>> 6ecfbf47f8803bc2f0083c090b9bb3c2d7d16b96
    #result = subprocess.Popen(shell_command,shell=True,stdout=subprocess.PIPE).stdout.readlines()
    value_dic = {'status':0, 'data':{}}
    li = contents['RESULT'].split("\n")  # 字符串转列表
    content_list = li[:len(li) - 1]  # 取列表开始到倒数第二个元素，最后一个元素为空

    for line in content_list:
        line = line.split()
        nic_name,t_in,t_out = line[1],line[4],line[5]
        value_dic['data'][nic_name] = {"t_in":line[4], "t_out":line[5]}
    return value_dic
<<<<<<< HEAD

if __name__ == '__main__':
    host_message = {'192.168.231.110': ['root', 'oracle', 22]}
    a = monitor(**host_message)
    print(a)
=======
>>>>>>> 6ecfbf47f8803bc2f0083c090b9bb3c2d7d16b96
