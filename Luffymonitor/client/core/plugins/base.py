#!/usr/bin/env python
# -*- coding:utf-8 -*-
# from conf import settings

'''
提供ssh访问主机和jdbc访问数据库的接口
'''
import os,sys
import logging
import telnetlib
import time

BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)
import jaydebeapi
from conf import settings

class BasePlugin(object):
    # {'192.168.2.128': ['root', 'oracle', 22, 'scott', 'tiger','prod', 1521,2]}
    def __init__(self, **kwargs):
        self.tn = telnetlib.Telnet()
        for i, v in kwargs.items():
            self.ip = i
            self.username = v[0]
            self.passwd = v[1]
            self.port = v[2]
            self.db_user = v[3]
            self.db_passwd = v[4]
            self.db_port = v[6]
            self.SID = v[5]
            self.login_type = v[7]
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
            # 此函数实现telnet登录主机

    def telnet_login(self,cmd):
        result_dict = {}
        try:
            # self.tn = telnetlib.Telnet(host_ip,port=23)
            self.tn.open(self.ip, port=self.port)
        except Exception as e:
            logging.warning('%s网络连接失败' % self.ip)
            result_dict['ERROR'] = str(e)
            return result_dict
        try:
            # 等待login出现后输入用户名，最多等待10秒
            self.tn.read_until(b'login: ', timeout=200)
            self.tn.write(self.username.encode('ascii') + b'\n')
            # 等待Password出现后输入用户名，最多等待10秒
            self.tn.read_until(b'Password: ', timeout=200)
            self.tn.write(self.passwd.encode('ascii') + b'\n')
            # 延时两秒再收取返回结果，给服务端足够响应时间
            time.sleep(2)
            # 获取登录结果
            # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
            return_result = self.tn.read_very_eager().decode('ascii')
            if return_result.strip().endswith('#') or return_result.strip().endswith('$'):
                logging.warning('%s登录成功' % self.ip)
                # 执行命令
                self.tn.write(cmd.encode('ascii') + b'\n')
                time.sleep(.1)
                # 获取命令结果
                command_result = self.tn.read_very_eager().decode('ascii')
                # logging.info('命令执行结果：\n%s' % command_result)
                result_dict['ERROR'] = ""
                #多行字符串转换成列表，列表第二个到倒数第二个元素，再把列表中的字符串用\n 拼接成字符串
                result_dict['RESULT'] = "\n".join(command_result.split("\r\n")[1:-1])
                return result_dict
            else:
                logging.warning('%s登录失败，用户名或密码错误' % self.ip)
                result_dict['ERROR'] = '登录失败，用户名或密码错误'
                return result_dict
        except Exception as e:
            logging.error(e)
        # self.tn.write(b"exit\n")
    # 退出telnet
    def logout_host(self):
        self.tn.write(b"exit\n")



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
        if self.login_type == 0:
            output = self.ssh(cmd)
        elif self.login_type == 1:
            output = self.telnet_login(cmd)
        return output

# hosts = {'10.10.0.2': ['root', 'oracle', 23, 'scott', 'tiger','prod', 1521,1]}
# ssh = BasePlugin(**hosts)
# a = ssh.exec_shell_cmd('uname -sn')
# print(a['RESULT'].split())

