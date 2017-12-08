__author__ = "xiaoyu hao"
__author__ = "xiaoyu hao"

import paramiko
import time,os

def put_file(host_info,file_name):
    ip = host_info[1]
    name = host_info[2]
    pwd = host_info[3]
    port = host_info[4]
    date = time.strftime('%Y_%m_%d')
    date_detial = time.strftime('%Y_%m_%d %H:%M:%S')
    f = open('../log/put_%s_record.log' % date, 'a+')  # 操作日志记录，记录程序所有目录的/log目录里
    try:
        transport = paramiko.Transport((ip, port))
        transport.connect(username=name, password=pwd)

        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(file_name, '/tmp/%s' % os.path.basename(file_name))
        transport.close()
    except:
        log = "Time:%s | Type:%s | Detial:%s | Server:%s | Result:%s\n" % (
        date_detial, 'distribute file', file_name, ip, 'failed')
        f.write(log)
        f.close()
        print('\033[31;1mSomething is wrong of %s\033[0m' % ip)
    else:
        log = "Time:%s | Type:%s | Detial:%s | Server:%s | Result:%s\n" % (
        date_detial, 'distribute file', file_name, ip, 'success')
        f.write(log)
        f.close()
        print("\033[32;1mDistribute '%s' to %s Successfully!\033[0m" % (file_name, ip))


os.system('cls')
