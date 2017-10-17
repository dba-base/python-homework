__author__ = "xiaoyu hao"

import hashlib
import socket
import os
import time

host = "0.0.0.0"
port = 9999
ADDR = (host,port)

server = socket.socket()
server.bind(ADDR)
server.listen(5)

while True:
    conn,addr = server.accept()
    print("new connect:",addr)
    while True:
        print("等待指令。。。")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开！")
        cmd,filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            f = open(filename,"rb")
            m = hashlib.md5()
            file_size = os.stat(filename).st_size  #获取文件大小
            conn.send(str(file_size).encode())
            conn.recv(1024)
            for line in f:
                m.update(line)
                conn.send(line)
            print("file md5",m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode())
        print("send done")

server.close()