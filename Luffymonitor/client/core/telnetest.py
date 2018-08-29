__author__ = "xiaoyu hao"
import logging
import telnetlib
import time


class TelnetClient():
    def __init__(self,):
        self.tn = telnetlib.Telnet()

    # 此函数实现telnet登录主机
    def login_host(self,host_ip,username,password):
        try:
            # self.tn = telnetlib.Telnet(host_ip,port=23)
            self.tn.open(host_ip,port=23)
        except:
            logging.warning('%s网络连接失败'%host_ip)
            return False
        # 等待login出现后输入用户名，最多等待10秒
        self.tn.read_until(b'login: ',timeout=20)
        self.tn.write(username.encode('ascii') + b'\n')
        # 等待Password出现后输入用户名，最多等待10秒
        self.tn.read_until(b'Password: ',timeout=20)
        self.tn.write(password.encode('ascii') + b'\n')
        # 延时两秒再收取返回结果，给服务端足够响应时间
        time.sleep(2)
        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode('ascii')
        if 'Login incorrect' not in command_result:
            logging.warning('%s登录成功'%host_ip)
            return True
        else:
            logging.warning('%s登录失败，用户名或密码错误'%host_ip)
            return False

    # 此函数实现执行传过来的命令，并输出其执行结果
    def execute_some_command(self,host_ip,username,password,command):
        if self.login_host(host_ip,username,password):
            # 执行命令
            self.tn.write(command.encode('ascii')+b'\n')
            time.sleep(.1)
            # 获取命令结果
            command_result = self.tn.read_very_eager().decode('ascii')
            # logging.info('命令执行结果：\n%s' % command_result)
            return command_result

    # 退出telnet
    def logout_host(self):
        self.tn.write(b"exit\n")

if __name__ == '__main__':
<<<<<<< HEAD
    host_ip = '192.168.2.112'
    username = 'root'
    password = 'oracle'
    command = 'ls -l'
    telnet_client = TelnetClient()
    # 如果登录结果返加True，则执行命令，然后退出
    result = telnet_client.execute_some_command(host_ip,username,password,command)
    print(result)
    telnet_client.logout_host()
=======
    # 配置选项
    Host = '10.10.0.2'  # Telnet服务器IP
    username = 'root'  # 登录用户名
    password = 'oracle'  # 登录密码
    finish = '~]# '  # 命令提示符
    commands = ['ls -l']
    do_telnet(Host, username, password, finish, commands)  
>>>>>>> 9d185ef5baca19f814048a1bb609757d1bf0353a
