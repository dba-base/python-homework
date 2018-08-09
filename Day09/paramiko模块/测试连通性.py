__author__ = "xiaoyu hao"
import paramiko

def ssh(ip,port,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=port, username=username, password=passwd,timeout=10)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        stdout_res = stdout.read()
        stderr_res = stderr.read()
        result_err = stderr_res.decode()
        result_out = stdout_res.decode()
        print(result_out)
        ssh.close()

    except Exception as e:
        print(ip,'.....',e)

ssh('192.168.2.18',22,'root','cle','hostname')
