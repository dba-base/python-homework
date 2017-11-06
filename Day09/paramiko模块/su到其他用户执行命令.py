__author__ = "xiaoyu hao"
import paramiko
import time

# 交互式执行命令

def verification_ssh(host,username,password,port,root_pwd,cmd):
    s=paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname = host,port=int(port),username=username, password=password)
    if username != 'root':
        ssh = s.invoke_shell()
        time.sleep(0.1)
        ssh.send('su - \n')
        buff = ''
        while not buff.endswith('Password: '):
            resp = ssh.recv(9999).decode()
            buff += resp
        ssh.send(root_pwd)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('# '):
            resp = ssh.recv(9999).decode()
            buff +=resp
        ssh.send(cmd)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('# '):
            resp = ssh.recv(9999).decode()
            buff +=resp
        s.close()
        result = buff
    else:
        stdin, stdout, stderr = s.exec_command(cmd)
        result = stdout.read()
        s.close()
    return result

if __name__ == "__main__":
    host = '192.168.2.110'
    username = "oracle"
    password = "oracle"
    port = 22
    root_pwd = "oracle"
    cmd = "ifconfig"
    result = verification_ssh(host, username, password, port, root_pwd, cmd)
    print(result)