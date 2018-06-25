#!/usr/bin/env python
# -*- coding:utf-8 -*-
# from conf import settings

'''
提供ssh访问主机和jdbc访问数据库的接口
'''
class BasePlugin(object):

    def __init__(self, hostname,port,username,password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def ssh(self, cmd):
        '''
        SSH 方式访问主机
        :param cmd: 要执行的命令
        :return:
        '''
        import paramiko
        try:
            result_dict = {}
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password,timeout=10)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            stdout_res = stdout.read()
            stderr_res = stderr.read()
            result_dict['ERROR'] = stderr_res.decode()
            result_dict['RESULT'] = stdout_res.decode()
            ssh.close()
            return result_dict

        except Exception as e:
            print(e)

    def jdbc(self,sql):
        '''
        访问数据库接口
        :param sql: 要执行的sql语句
        :return:
        '''
        pass

    def exec_shell_cmd(self, cmd):
        output = self.ssh(cmd)
        return output


# ssh = BasePlugin('192.168.2.128',22,'root','oracle')
# status,result = ssh.exec_shell_cmd('sar 1 3')
# print(status)
# print(result)
