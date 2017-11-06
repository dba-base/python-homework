__author__ = "xiaoyu hao"

import paramiko
import time

# 交互式执行命令

def verification_ssh(host,username,password,port,cmd):
    s=paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname = host,port=int(port),username=username, password=password)
    if username == 'root':
        ssh = s.invoke_shell()
        ssh.send('su - oracle\n')
        buff = ''
        while not buff.endswith('$ '):   #逐行读取，直到读取到以$结尾
            resp = ssh.recv(9999).decode()
            buff +=resp
        ssh.send("sqlplus / as sysdba")
        ssh.send('\n')
        buff = ''
        while not buff.endswith('> '):
            resp = ssh.recv(9999).decode()
            buff +=resp
        ssh.send(cmd)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('> '):
            resp = ssh.recv(9999).decode()
            buff +=resp
        result = buff
        s.close()
    else:
        stdin, stdout, stderr = s.exec_command(cmd)
        result = stdout.read()
        s.close()
    return result

def run(host_info,cmd):
    ip = host_info[1]
    username = host_info[2]
    password = host_info[3]
    port = host_info[4]
    result = verification_ssh(ip, username, password, port, cmd)
    print("---------------------------%s------------------------------------"%ip)
    print(result)
    print("---------------------------------------------------------------")