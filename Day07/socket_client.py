

import socket

client = socket.socket() # 声明socket类型，同时生成socket连接对象

client.connect(('localhost',6969))

while True:
    #client.send(b"hello world!!")
    msg = input(">>:").strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode("utf-8"))    # 向服务器端发送指令，不能发送空
    data = client.recv(10240)           # 接收从服务器返回的结果
    print(data.decode())

client.close()