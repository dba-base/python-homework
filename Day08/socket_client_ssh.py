__author__ = "xiaoyu hao"

import socket

host = socket.gethostname()
port = 1234
ADDR = (host,port)

client = socket.socket()
client.connect(ADDR)

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:
        continue     #如果为0，不执行下面的内容，也就不会发送消息给服务端
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024)  #接收命令结果的长度
    print("命令结果大小：",cmd_res_size)
    client.send("开始发送指令吧".encode('utf-8'))  #给服务器反馈确认信息防止粘包
    receive_size = 0
    receive_data = b''
    while receive_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        receive_size += len(data)
        receive_data += data
    else:
        print("cmd res receive done ....",receive_size)
        print(receive_data.decode())

client.close()