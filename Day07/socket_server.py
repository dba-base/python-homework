
#服务器端

import os
import socket

server = socket.socket()
server.bind(("localhost",6969)) #绑定要监听的端口
server.listen()  #监听

while True:
    print("等待电话打进来。。。。")
    conn,addr = server.accept()  # 等待电话打进来,conn就是客户端连过来而在服务端为其生成的一个实例
    print(addr,"的电话来了。。。。")
    while True:
        data = conn.recv(10240).decode()   # 接收从客户端发来的指令
        print("recv:",data)

        if not data:
            print("client has loset ....")
            break
        res = os.popen(data).read()        #
        conn.send(res.encode("utf-8"))     #把结果返回给客户端
        #conn.close()

server.close()