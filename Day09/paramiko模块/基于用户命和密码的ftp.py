import paramiko

transport = paramiko.Transport(('10.10.0.2', 22))
transport.connect(username='root', password='oracle')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将lid_rsa110.txt 上传至服务器 /tmp/id_rsa110.txt
sftp.put('id_rsa110.txt', '/tmp/id_rsa110.txt')
# 将/tmp/yum.log 下载到本地 from_server.log
sftp.get('/tmp/yum.log', 'from_server.log')

transport.close()
