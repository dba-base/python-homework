__author__ = "xiaoyu hao"

import socket
import hashlib

host = socket.gethostname()
port = 9999
ADDR = (host,port)

client = socket.socket()
client.connect(ADDR)

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:
        continue
    if cmd.startswith("get"):
        client.send(cmd.encode())
        server_reponse = client.recv(1024)   #接收文件大小
        print("server response:",server_reponse)
        client.send(b"ready to recv file")
        file_total_size = int(server_reponse.decode())
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename + ".new","wb")
        m = hashlib.md5()

        #接收文件
        while received_size < file_total_size:
            if file_total_size - received_size > 1024:
                size = 1024
            else:   #最后一次，剩多少收多少
                size = file_total_size - received_size
                print("last recivesize:",size)

            data = client.recv(size)
            received_size += len(data)
            m.update(data)
            f.write(data)
        else:
            new_file_md5 = m.hexdigest()
            print("file receive done.",received_size,file_total_size)
            f.close()
        server_file_md5 = client.recv(1024)  #接收服务器端的md5值
        print('server file md5:',server_file_md5.decode())
        print('client file md5:',new_file_md5)

client.close()