#!/usr/bin/env python
__author__ = "xiaoyu hao"


import socket
import sys
import os
import hashlib

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
                self.help()

    def help(self):
        msg ="""
usage:
    ls
    dir
    pwd
    cd dirname
    cd ..
    get filename
    put filename
"""
        print(msg)

    def bye(self,command):
        '''退出方法'''
        command_str = command.split()
        print(command_str[0])
        #self.client.sendall(command.encode())
        if len(command_str) == 1 and command_str[0] == "bye":
            print("11111111111111111")
            self.client.shutdown(2)
            self.client.close()
            sys.exit(0)

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
            print('[%s] error!' %status_code)

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
            print('[%s] error!' % status_code)

    def __progress(self,trans_size, file_size,mode):
        '''
        进度条方法
        :param trans_size: 已传输得数据大小(字节)
        :param file_size: 文件的总大小（字节）
        :param mode: 传输方式
        :return:
        '''
        unit_size = 1048576
        bar_lengh = 100   # 进度条的长度
        percent = float(trans_size)/float(file_size)  #已经传输的大小百分比
        hashes = '=' * int(percent*bar_lengh)         #进度条显示的数量
        spaces = ' ' * (bar_lengh - len(hashes))      #剩余部分通过空格补充，空格数量 = 总长度 - “=”显示的长度
        # /r表示重新回到当前行输出
        r = "\r%s:%.2fm/%.2fm %d%% [%s]"%(mode,trans_size/unit_size,file_size/unit_size,percent*100,hashes+spaces)
        sys.stdout.write(r)
        sys.stdout.flush()  #清空缓存

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
        self.client.sendall(command.encode())
        status_code = self.client.recv(1024).decode()

        #命令正确
        if status_code == "201":
            filename = os.path.basename(command.split()[1])
            #判断文件是否存在
            if os.path.isfile(filename):
                revice_size = os.stat(filename).st_size #接收文件的大小
                self.client.sendall("403".encode())     #告诉客户端文件存在
                responce = self.client.recv(1024)
                self.client.sendall(str(revice_size).encode()) #把文件大小发给服务端进行大小比较
                status_code = self.client.recv(1024).decode()
                #文件大小不一致，续传
                if status_code == "205":
                    print("继续上次位置进行传输")
                    self.client.sendall("000".encode())
                elif status_code == "405":
                    print("文件一致！")
                    return
            #文件不存在，正常下载
            else:
                self.client.sendall("402".encode())
                revice_size = 0

            file_size = self.client.recv(1024).decode() #接收需要传送文件的大小
            file_size = int(file_size)
            self.client.sendall("000".encode())

            #开始接收文件
            with open(filename,"ab") as f:
                file_size += revice_size  # 接收文件的总大小
                m = hashlib.md5()
                while revice_size < file_size:
                    if file_size - revice_size > 1024:
                        size = 1024
                    else:
                        size = file_size - revice_size
                    data = self.client.recv(size)
                    revice_size += len(data)
                    m.update(data)
                    f.write(data)
                    self.__progress(revice_size,file_size,"下载中...")
                new_file_md5 = m.hexdigest()
                server_file_md5 = self.client.recv(1024).decode()
                print("\n 下载完成！")
                if new_file_md5 == server_file_md5:
                    print("\n 文件一致")
        else:
            print("[%s] error！" % (status_code))

    def put(self,command):
        '''
        上传文件
        :return:
        '''
        if len(command.split()) == 2:
            filename = os.path.basename(command.split()[1])
            if os.path.isfile(filename):
                self.client.sendall(command.encode())
                self.client.recv(1024)

                file_size = os.stat(filename).st_size
                self.client.sendall(str(file_size).encode())  #发送文件大小
                status_code = self.client.recv(1024).decode()

                if status_code == "202":
                    with open(filename,"rb") as f:
                        m = hashlib.md5()
                        for line in f:
                            m.update(line)
                            send_size = f.tell()  #tell()返回文件当前的位置，字节，也就是发送文件的大小
                            self.client.sendall(line)
                            self.__progress(send_size,file_size,'上传中')
                    print("\n上传完成！")
                    self.client.sendall(m.hexdigest().encode())
                    status_code = self.client.recv(1024).decode()   #返回状态码
                    if status_code == "203":
                        print("\n文件一致")
                else:
                    print("[%s]" %status_code)
            else:
                print("402 文件不存在")
        else:
            print("401 命令不正确")


if __name__ == "__main__":
    # ip = input("IP:")
    # port = int(input("PORT:"))
    ip = "localhost"
    port = 9999
    IP_PORT = (ip,port)
    print(IP_PORT)
    client = MyClient(IP_PORT)
    client.start()