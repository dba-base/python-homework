__author__ = "xiaoyu hao"

import socketserver
import os
import hashlib
from src import auth_user
from conf import settings

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
                self.user_msg = result[1]
                self.current_path = self.user_msg['homepath']    #初始化为当前家目录，后续随着cd会改变
                self.home_path = self.user_msg['homepath']

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
        if len(command.split()) == 2:
            filename = os.path.basename(command.split()[1])
            file_path = self.current_path + r"\%s"%filename
            #判断文件在服务器端是否存在
            if os.path.isfile(file_path):
                self.conn.sendall("201".encode())   #命令可以执行
                file_size = os.stat(file_path).st_size   #文件总的大小
                status_code = self.conn.recv(1024).decode()  #接收客户端返回的文件是否存在
                #客户端存在文件
                if status_code == "403":
                    self.conn.sendall("000".encode())
                    exist_file_size = self.conn.recv(1024).decode()
                    exist_file_size = int(exist_file_size)
                    #判断是否需要续传
                    if exist_file_size < file_size:
                        self.conn.sendall("205".encode())
                        file_size -= exist_file_size
                        response = self.conn.recv(1024)
                    #客户端文件已存在，并且大小相等，不提供下载
                    else:
                        self.conn.sendall("405".encode())
                        return #???
                elif status_code == "402":
                    exist_file_size = 0

                with open(file_path,'rb') as f:
                    self.conn.sendall(str(file_size).encode())  #如果是续传，发送的是剩余文件大小，如果是整传，发送的是文件总大小
                    response = self.conn.recv(1024)
                    f.seek(exist_file_size)
                    m = hashlib.md5()
                    for line in f:
                        m.update(line)
                        self.conn.sendall(line)
                self.conn.sendall(m.hexdigest().encode())
            else:
                self.conn.sendall("401".encode())
        else:
            self.conn.sendall("401".encode())

    def put(self,command):
        '''
        上传文件
        :return:
        '''
        filename = os.path.basename(command.split()[1])
        file_path = self.current_path + r"\%s" %filename
        self.conn.sendall('000'.encode())
        file_size = self.conn.recv(1024).decode()
        file_size = int(file_size)                #文件大小
        limit_size = self.user_msg["limitsize"]   #空间限额
        userd_size = self.__getdirsize(self.home_path)   #已用空间
        print("limitsize:%s,used_size:%s" %(limit_size/1024/1024,userd_size/1024/1024))
        if limit_size >= file_size + userd_size:
            self.conn.sendall('202'.encode())
            with open(file_path,'wb') as f:
                revice_size = 0
                m = hashlib.md5()
                while revice_size < file_size:
                    if file_size - revice_size > 1024:
                        size = 1024
                    else:
                        size = file_size - revice_size
                    data = self.conn.recv(size)
                    revice_size += len(data)
                    f.write(data)
                    m.update(data)
                new_file_md5 = m.hexdigest()   #生成新的md5值
                client_file_md5 = self.conn.recv(1024).decode()
                if new_file_md5 == client_file_md5:
                    self.conn.sendall("203".encode())
        else:
            self.conn.sendall("404 磁盘空间不足！".encode())

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
            self.conn.sendall(send_data.encode())
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
        if len(command.split()) == 2 and command.split()[0] == "cd":
            dir_name = command.split()[1]    #切换目录
            user_home_path = settings.HOME_PATH + r"\%s" %self.user_msg["username"]  #家目录
            dir_path = os.path.join(self.current_path,dir_name)
            #返回上级目录
            if dir_name == ".." and len(self.current_path) > len(user_home_path): #不能访问家目录的上级目录
                self.conn.sendall("201".encode())
                response = self.conn.recv(1024)
                self.current_path = os.path.dirname(self.current_path)
            elif os.path.isdir(dir_path):
                self.conn.sendall("201".encode())
                response = self.conn.recv(1024)
                if dir_name != "." and dir_name != "..":
                    self.current_path += r"\%s"%dir_name   #切换目录
            else:
                self.conn.sendall("402".encode())
        else:
            self.conn.sendall("402".encode())

    def __getdirsize(self,home_path):
        '''
        统计目录的空间大小
        :return:目录总大小
        '''
        size = 0
        for root,dirs,files in os.walk(home_path):   #遍历目录下所有的目录和文件，dirs和files为列表
            size += sum(os.path.getsize(os.path.join(root,filename)) for filename in files)
        return size

def run():
    server = socketserver.ThreadingTCPServer(settings.IP_PORT, MyServer)
    server.serve_forever()
