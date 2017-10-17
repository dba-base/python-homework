__author__ = "xiaoyu hao"

import socket
import os

host = socket.gethostname()
port = 1234
ADDR = (host,port)

server = socket.socket()
server.bind(ADDR)
server.listen(5)

while True:
    print("Wait ")
    conn,addr = server.accept()
    print("new conn:",addr)
    while True:
        print("等待新指令。。")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开。。")
            break
        print("执行指令：",data)
        cmd_res = os.popen(data.decode()).read()
        print("before send",len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output ..."
        #下面两个send放在一起容易发生粘包的错误
        conn.send( str(len(cmd_res.encode())).encode("utf-8"))
        client_ask = conn.recv(1024) #等待客户端确认 ，防止粘包，中间加入一个确认语句
        print(client_ask.decode())
        conn.send(cmd_res.encode("utf-8"))

server.close()



