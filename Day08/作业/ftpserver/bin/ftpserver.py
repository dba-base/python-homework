__author__ = "xiaoyu hao"

import socketserver
import os
from src import auth_user

class MyServer(socketserver.BaseRequestHandler):
    '''ftp服务端'''
    def handle(self):
        try:
            self.conn = self.request
            while True:
                login_info = self.conn.recv(1024).decode()
                result = self.authenticat(login_info)
                status_code = result[0]
                self.conn.sendall(status_code.encode())
                if status_code == "400":
                    continue
                user_msg = self.result[1]
                self.current_path = user_msg['homepath']    #初始化为当前家目录，后续随着cd会改变
                self.home_path = user_msg['homepath']

                #接收从客户端发送过来的命令
                while True:
                    command = self.conn.recv(1024).decode()
                    command_str = command.split()[0]
                    if hasattr(self,command_str):
                        func = getattr(self,command_str)
                        func(command)
                    else:
                        error_code = '401'
                        self.conn.sendall(error_code.encode())
                        print('[%s] 命令不存在...' %error_code)
        except ConnectionRefusedError as e:
            self.conn.close()
            print(e)

    def authenticat(self,login_info):
        '''
        验证用户
        :param login_info: 从客户端接收的用户登陆信息
        :return: 状态码，200 登陆成功  400 登陆失败
        '''
        auth = auth_user.User_auth()
        result = auth.authentication(login_info)
        if result:
            return "200",result
        else:
            return "400",result

    def get(self,command):
        '''
        下载文件
        :return:
        '''

    def put(self,command):
        '''
        上传文件
        :return:
        '''

    def dir(self,command):
        '''
        查看windows目录下的文件
        :return:
        '''
        if len(command.split()) == 1:
            self.conn.sendall("201".encode())
            response = self.conn.recv(1024)
            send_data = os.popen("dir %s" %self.current_path)
            self.conn.sendall(send_data.read().encode())
        else:
            self.conn.sendall("401".encode())

    def ls(self,command):
        '''
        查看linux目录下的文件
        :return:
        '''
        if len(command.split()) == 1:
            self.conn.sendall("201".encode())
            response = self.conn.recv(1024)
            send_data = os.popen("ls %s" %self.current_path)
            self.conn.sendall(send_data.read().encode())
        else:
            self.conn.sendall("401".encode())

    def pwd(self,command):
        '''
        查看当前目录
        :return:
        '''
        if len(command.split()) == 1:
            self.conn.sendall("201".encode())
            response = self.conn.recv(1024)
            send_data = self.current_path
            self.conn.sendall(send_data.read().encode())
        else:
            self.conn.sendall("401".encode())

    def mkdir(self,command):
        '''
        创建目录
        :return:
        '''
        if len(command.split()) > 1 and command.split()[0] == "mkdir":
            dir_name = command.split()[1]
            dir_path = os.path.join(self.current_path,dir_name)
            #判断目录是否存着
            if not os.path.isdir(dir_path):
                self.conn.sendall("201".encode())
                response = self.conn.recv(1024)
                os.popen("mkdir %s" %dir_path)
            else:
                self.conn.sendall("403".encode())
        else:
            self.conn.sendall("401".encode())

    def cd(self,command):
        '''
        切换目录
        :return:
        '''
