import paramiko

private_key = paramiko.RSAKey.from_private_key_file('id_rsa110.txt')

transport = paramiko.Transport(('10.10.0.2', 22))
transport.connect(username='root', pkey=private_key)

sftp = paramiko.SFTPClient.from_transport(transport)
# 将lid_rsa110.txt 上传至服务器 /tmp/id_rsa110.txt
sftp.put('id_rsa110.txt', '/tmp/id_rsa110.txt')
# 将/tmp/yum.log 下载到本地 from_server.log
sftp.get('/tmp/yum.log', 'from_server.log')

transport.close()