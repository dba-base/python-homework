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
        while not buff.endswith('$ '):
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
        s.close()
        result = buff
    # else:
    #     stdin, stdout, stderr = s.exec_command(cmd)
    #     result = stdout.read()
    #     s.close()
    return result

def run():
    host = '192.168.2.110'
    username = "root"
    password = "oracle"
    port = 22
    cmd = "select instance_name,status from v$instance;"
    result = verification_ssh(host, username, password, port, cmd)
    print("---------------------------%s------------------------------------"%host)
    print(result)
    print("---------------------------------------------------------------")