#!/usr/bin/env python
# -*- coding:utf-8 -*-
# from conf import settings

'''
提供ssh访问主机和jdbc访问数据库的接口
'''
import os,sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)
import jaydebeapi
from conf import settings

class BasePlugin(object):
    # {'192.168.2.128': ['root', 'oracle', 22, 'scott', 'tiger','prod', 1521]}
    def __init__(self, **kwargs):
        for i, v in kwargs.items():
            self.ip = i
            self.username = v[0]
            self.passwd = v[1]
            self.port = v[2]
            self.db_user = v[3]
            self.db_passwd = v[4]
            self.db_port = v[6]
            self.SID = v[5]
        self.driver = settings.db_params['driver'],
        self.url = settings.db_params['url']%(self.ip,self.db_port,self.SID),
        self.tnsname = '%s:%s/%s'%(self.ip,self.db_port,self.SID)
        #"url":'jdbc:oracle:thin:@%s:%s:%s'
        self.jarFile = settings.db_params['jarFile']
    def ssh(self, cmd):
        '''
        SSH 方式访问主机
        :param cmd: 要执行的命令
        :return:
        '''
        import paramiko
        result_dict = {}
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=self.ip, port=self.port, username=self.username, password=self.passwd,timeout=10)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            stdout_res = stdout.read()
            stderr_res = stderr.read()
            result_dict['ERROR'] = stderr_res.decode()
            result_dict['RESULT'] = stdout_res.decode()
            ssh.close()
            return result_dict

        except Exception as e:
            print(self.ip,'.....',e)
            result_dict['ERROR'] = str(e)
            return result_dict

    def jdbc_connect(self,sql):
        '''
        访问JDBC数据库接口
        :param sql: 要执行的sql语句
        :return:
        '''
        try:
            conn = jaydebeapi.connect(self.driver[0],[self.url[0],self.db_user,self.db_passwd],self.jarFile)
            curs = conn.cursor()
            curs.execute(sql)
            result = curs.fetchall()
            curs.close()
            conn.close()
            return result
        except Exception as e:
            print(e)

    def ora_connect(self,sql,val):
        '''
        oracle 连接接口
        :param sql: 执行的sql
        :param val: 1 只取结果的一行,返回元组，2 取得所有结果，返回列表，元素为元组
        :return:
        '''
        import cx_Oracle
        conn = cx_Oracle.connect(self.db_user,self.db_passwd,self.tnsname)
        c = conn.cursor()
        if val == 1:
            result = c.execute(sql).fetchone()
        if val == 2:
            result = c.execute(sql).fetchall()
        c.close()
        conn.close()
        return result

    def exec_shell_cmd(self, cmd):
        output = self.ssh(cmd)
        return output


# ssh = BasePlugin('192.168.2.129',22,'root','oracle')
# a = ssh.exec_shell_cmd('sar 1 3')
# print(a)

