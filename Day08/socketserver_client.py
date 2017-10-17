__author__ = "xiaoyu hao"

import socket

client = socket.socket()
client.connect(("localhost", 1234))

while True:
    cmd = input(">>>:").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode("utf-8"))
    cmd_res = client.recv(500)
    print(cmd_res.decode("utf-8"))

client.close()