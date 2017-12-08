import paramiko

transport = paramiko.Transport(('192.168.2.110', 22))
transport.connect(username='root', password='oracle')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将lid_rsa110.txt 上传至服务器 /tmp/id_rsa110.txt
sftp.put('F:\github\python_homework\Day09\作业\core\db_connect.py', '/tmp/b_connect')
# 将/tmp/yum.log 下载到本地 from_server.log
#sftp.get('/tmp/yum.log', 'from_server.log')

transport.close()
