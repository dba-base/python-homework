# encoding=utf-8

def do_telnet(Host, username, password, finish, commands):
    import telnetlib
    '''''Telnet远程登录：Windows客户端连接Linux服务器'''

    # 连接Telnet服务器  
    tn = telnetlib.Telnet(Host, port=23, timeout=10)
    tn.set_debuglevel(2)

    # 输入登录用户名  
    tn.read_until('login: '.encode('utf-8'))
    tn.write(username.encode('ascii') + b'\n')

    # 输入登录密码  
    tn.read_until('password: '.encode('utf-8'))
    tn.write(password.encode('ascii') + b'\n')

    # 冯总：
    # 1.BSS精细化，差异化，2.MSS智慧化，3.开发转型 4.推动运维变革-全网集中统一的维护体系
    # 5.人才转型

    # 登录完毕后执行命令  
    tn.read_until(finish)
    for command in commands:
        tn.write('%s\n' % command)

        # 执行完毕后，终止Telnet连接（或输入exit退出）
    tn.read_until(finish)
    tn.close()  # tn.write('exit\n')


if __name__ == '__main__':
    # 配置选项
    Host = '192.168.2.112'  # Telnet服务器IP
    username = 'root'  # 登录用户名
    password = 'oracle'  # 登录密码
    finish = '~]# '  # 命令提示符
    commands = ['ls -l']
    do_telnet(Host, username, password, finish, commands)  