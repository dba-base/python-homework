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

    def interactive(self):
        '''
        交互程序
        :return:
        '''

    def get(self):
        '''
        下载文件
        :return:
        '''

    def put(self):
        '''
        上传文件
        :return:
        '''

    def __universal_method_none(self, command):
        '''
        通用方法，无输出显示，例如cd等命令
        :param command: 命令
        :return:
        '''

    def __universal_method_data(self,command):
        '''
        通用方法，有输出显示，例如：dir，pwd等命令
        :param command:
        :return:
        '''
    def __progress(self,trans_size, file_size,mode):
        '''
        进度条方法
        :param trans_size: 已传输得数据大小
        :param file_size: 文件的总大小
        :param mode: 传输方式
        :return:
        '''

    def dir(self):
        '''
        查看windows目录下的文件
        :return:
        '''

    def ls(self):
        '''
        查看linux目录下的文件
        :return:
        '''

    def pwd(self):
        '''
        查看当前目录
        :return:
        '''

    def mkdir(self):
        '''
        创建目录
        :return:
        '''

    def cd(self):
        '''
        切换目录
        :return:
        '''
