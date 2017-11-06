__author__ = "xiaoyu hao"

import paramiko
import time

def ssh_fun(host_info,cmd,sysname):
    ip = host_info[1]
    username = host_info[2]
    password = host_info[3]
    port = host_info[4]
    date = time.strftime('%Y_%m_%d')
    date_detial = time.strftime('%Y_%m_%d %H:%M:%S')
    f = open('../log/%s_%s_record.log' % (sysname, date), 'a+')  # 操作日志记录，记录程序所有目录的/log目录里
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()  # 读取know_host文件
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_host文件中的主机

        ssh.connect(ip,int(port),username,password,timeout=5)
        stdin, stdout, stderr = ssh.exec_command(cmd)

        cmd_result = stdout.read(),stderr.read()
        print('\033[32;1m-------------%s--------------\033[0m' % ip)
        for line in cmd_result:
            print(line.decode())
        print('\033[32;1m-----------------------------\033[0m')
    except :
        log = "Time:%s | Type:%s | Detial:%s | Server:%s | Result:%s\n" % (date_detial, 'cmd batch', cmd, ip, 'failed')
        f.write(log)
        f.close()
        print('\033[31;1mSomething is wrong of %s\033[0m' % ip)
    else:
        log = "Time:%s | Type:%s | Detial:%s | Server:%s | Result:%s\n" % (date_detial, 'cmd batch', cmd, ip, 'success')
        f.write(log)
        f.close()
        return 1