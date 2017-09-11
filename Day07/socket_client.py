

import socket

client = socket.socket() #声明socket类型，同时生成socket连接对象

client.connect(('localhost',6969))

client.send(b"hello world!!")
data = client.recv(1024)
print("recv:",data)

client.close()