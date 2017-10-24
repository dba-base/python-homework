#!/usr/bin/env python
# -*- coding:utf-8 -*-
import paramiko
import uuid

class Haproxy(object):

    def __init__(self):
        self.host = '10.10.0.2'
        self.port = 22
        self.username = 'root'
        self.pwd = 'oracle'
        self.__k = None

    def create_file(self):
        file_name = str(uuid.uuid4())
        with open(file_name,'w') as f:
            f.write('sb')
        return file_name

    def run(self):
        self.connect()
        self.upload()
        self.rename()
        self.close()

    def connect(self):
        transport = paramiko.Transport((self.host,self.port))
        transport.connect(username=self.username,password=self.pwd)
        self.__transport = transport

    def close(self):

        self.__transport.close()

    def upload(self):
        # 连接，上传
        file_name = self.create_file()

        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(file_name, '/home/oracle/tttttttttttt.py')

    def rename(self):

        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command('mv /home/oracle/tttttttttttt.py /home/oracle/ooooooooo.py')
        # 获取命令结果
        result = stdout.read()


ha = Haproxy()
ha.run()
