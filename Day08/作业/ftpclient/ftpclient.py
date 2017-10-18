#!/usr/bin/env python
__author__ = "xiaoyu hao"


import socket

class MyClient(object):
    '''
    ftp 客户端程序
    '''
    def __init__(self,ip_port):
        self.ip_port = ip_port

    def connect(self):
        '''
        连接服务器
        :return:
        '''
        self.client = socket.socket()
        self.client.connect(self.ip_port)

    def start(self):
        '''
        程序开始
        :return:
        '''
        self.connect()
        while True:
            username = input("username:").strip()
            password = input("password:").strip()
            login_info = ("%s:%s" %(username,password))
            self.client.sendall(login_info.encode())
            status_code = self.client.recv(1024).decode()   #返回状态码

            if status_code == "400":
                print("[%s] 用户验证失败！" %status_code)
                continue
            else:
                print("[%s] 用户验证成功！" % status_code)

            self.interactive()

    def interactive(self):
        '''
        交互程序
        :return:
        '''
        while True:
            command = input(">>").strip()
            if not command:
                continue
            command_str = command.split()[0]
            if hasattr(self,command_str):
                func = getattr(self,command_str)
                func(command)
            else:
                print("[%s] 非法命令..." %401)

    def __universal_method_none(self, command):
        '''
        通用方法，无输出显示，例如cd等命令
        :param command: 命令
        :return:
        '''
        self.client.sendall(command.encode())
        status_code = self.client.recv(1024).decode()
        if status_code == '201':  #命令可执行
            self.client.sendall('000'.encode())   #给服务器返回确认信息，让服务器继续执行
        else:
            print('[%s] Error!' %status_code)


    def __universal_method_data(self,command):
        '''
        通用方法，有输出显示，例如：dir，pwd等命令
        :param command:
        :return:
        '''
        self.client.sendall(command.encode())
        status_code = self.client.recv(1024).decode()
        if status_code == '201':  # 命令可执行
            self.client.sendall('000'.encode())  # 给服务器返回确认信息，让服务器继续执行
            data = self.client.recv(1024).decode()   #接收服务端返回的结果并打印
            print(data)
        else:
            print('[%s] Error!' % status_code)

    def __progress(self,trans_size, file_size,mode):
        '''
        进度条方法
        :param trans_size: 已传输得数据大小
        :param file_size: 文件的总大小
        :param mode: 传输方式
        :return:
        '''

    def dir(self,command):
        '''
        查看windows目录下的文件
        :return:
        '''
        self.__universal_method_data(command)

    def ls(self,command):
        '''
        查看linux目录下的文件
        :return:
        '''
        self.__universal_method_data(command)

    def pwd(self,command):
        '''
        查看当前目录
        :return:
        '''
        self.__universal_method_data(command)

    def mkdir(self,command):
        '''
        创建目录
        :return:
        '''
        self.__universal_method_none(command)

    def cd(self,command):
        '''
        切换目录
        :return:
        '''
        self.__universal_method_none(command)

    def get(self, command):
        '''
        下载文件
        :param command:
        :return:
        '''

    def put(self):
        '''
        上传文件
        :return:
        '''