__author__ = "xiaoyu hao"
#!/usr/bin/env python
import pexpect

# 即将 telnet 所要登录的远程主机的域名
ipAddress = '192.168.2.112'
# 登录用户名
loginName = 'root'
# 用户名密码
loginPassword = 'oracle'
# 提示符，可能是’ $ ’ , ‘ # ’或’ > ’
loginprompt = '[$#>]'

# 拼凑 telnet 命令
cmd = 'telnet ' + ipAddress
# 为 telnet 生成 spawn 类子程序
child = pexpect.spawn(cmd)
# 期待'login'字符串出现，从而接下来可以输入用户名
index = child.expect(["login", "(?i)Unknown host", pexpect.EOF, pexpect.TIMEOUT])
if ( index == 0 ):
    # 匹配'login'字符串成功，输入用户名.
    child.sendline(loginName)
    # 期待 "[pP]assword" 出现.
    index = child.expect(["[pP]assword", pexpect.EOF, pexpect.TIMEOUT])
    # 匹配 "[pP]assword" 字符串成功，输入密码.
    child.sendline(loginPassword)
    # 期待提示符出现.
    child.expect(loginprompt)
    if (index == 0):
        # 匹配提示符成功，输入执行命令 'ls -l'
        child.sendline('ls -l')
        # 立马匹配 'ls -l'，目的是为了清除刚刚被 echo 回显的命令.
        child.expect('ls -l')
        # 期待提示符出现.
        child.expect(loginprompt)
        # 将 'ls -l' 的命令结果输出.
        print(child.before)
        print("Script recording started. Type ^] (ASCII 29) to escape from the scriptshell.")
        # 将 telnet 子程序的执行权交给用户.
        child.interact()
        print('Left interactve mode.')
    else:
        # 匹配到了 pexpect.EOF 或 pexpect.TIMEOUT，表示超时或者 EOF，程序打印提示信息并退出.
        print("telnet login failed, due to TIMEOUT or EOF")
        child.close(force=True)
else:
    # 匹配到了 pexpect.EOF 或 pexpect.TIMEOUT，表示超时或者 EOF，程序打印提示信息并退出.
    print("telnet login failed, due to TIMEOUT or EOF")
    child.close(force=True)