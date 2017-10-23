__author__ = "xiaoyu hao"

'''
linux需要通过ssh-keygen生成公钥文件
'''

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('Identity110.pub')
#private_key = paramiko.RSAKey(file_obj=StringIO(key_str))

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.2.110', port=22, username='root', pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df;ifconfig')
result = stdout.read()
print(result.decode())
stdin, stdout2, stderr = ssh.exec_command('ifconfig')
# 获取命令结果
result2 = stdout2.read()
print(result2.decode())

# 关闭连接
ssh.close()