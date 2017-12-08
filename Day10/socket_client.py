__author__ = "xiaoyu hao"

import socket

HOST = 'localhost'  # The remote host
PORT = 10000  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    msg = bytes(input(">>:"), encoding="utf8")
    s.sendall(msg)
    data = s.recv(1024).decode()

    #
    print('Received', data)
s.close()
