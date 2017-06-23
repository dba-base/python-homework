#Author: xiaoyu hao

'''
实现功能：
1.输入用户名密码
2.认证成功后显示欢迎信息
3.输错三次后锁定
'''

#现在只实现了上述功能
#后续补充：
#1.用户注册
#2.用户解锁
#耗时：1天

count = 3

#登陆成功显示
def login_success(username):
    info_msg = '''
    ---------------CONGRANTULATIONS,{_name},SUCCESSFUL --------------
    Hi,{_name},Welcom to login....
    -----------------------------------------------------------------
    '''.format(_name=username)
    print(info_msg)

#登陆失败
def login_fail(username,count):
    if count > 0:
        print("密码输入错误！你还可以输入{_count}次，{_count}次后用户将被锁定".format(_count=count))
        passwd = input("Password:")
        user_passwd_com(username,passwd,count)
    else:
        print("{_name} has been locked!!!".format(_name=username))
        with open("lockuser.list",'a') as f:
            lock_user="%s" %username+"\n"
            f.writelines(lock_user)

#判断用户是否锁定,通过返回的flag判断用户是否被锁定，1为锁定，0为正常状态
def is_lock_user(username):
    flag = 0
    with open("lockuser.list", 'r') as f:
        lockuser = f.readlines()   #列表
        #如果列表不为空
        if len(lockuser) != 0:
            for i in lockuser:
                j = i.split()[0]
                if username == j:
                    print("{_username}已经被锁定！请求管理员解锁！".format(_username=username))
                    flag =1
    return flag

#判断用户密码正确性
def user_passwd_com(username,passwd,count):
    with open("user.list",'r') as f:
        #判断用户是否存在，存在则继续执行，不存在执行else语句
        for i in f.readlines():
            if username == i.split()[0]:
                if passwd == i.split()[1]:
                    login_success(username)
                    #登陆成功后跳出循环
                    break
                else:
                    count = count - 1
                    login_fail(username,count)
                    #锁定后跳出出循环，不执行下面的语句
                    break
        else:
            print("用户不存在！")

#主函数入口
def login_main():
    username = input("username:")
    password = input("password:")
    #判断用户是否存在
    user_status = is_lock_user(username)
    #if is_lock_user(username) != 1:    这样写的话在判断的时候会执行一次函数内容，会和上面的函数重复，打印两次is_lock_user中的内容
    if user_status != 1:
        user_passwd_com(username, password,count)

if __name__ == '__main__':
    login_main()