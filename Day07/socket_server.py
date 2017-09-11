
#服务器端

import socket

server = socket.socket()
server.bind(("localhost",6969)) #绑定要监听的端口
server.listen()  #监听

print("等待电话打进来。。。。")
conn,addr = server.accept() #等待电话打进来,conn就是客户端连过来而在服务端为其生成的一个实例

print("电话来了。。。。")
data = conn.recv(1024)
print("recv:",data)
conn.send(data.upper())

server.close()