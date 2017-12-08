__author__ = "xiaoyu hao"

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from multiprocessing import Pool
from core import db_connect
from core import query_oracle
from conf import sqlfile
from core import ssh_func
from core import putfile
from multiprocessing import Process

class RemoteSSH(object):

    def run_oracle(self,h,cmd):
        '''
        调用批量执行oracle命令
        :param h:
        :param cmd:
        :return:
        '''
        query_oracle.run(h,cmd)

    def run_ssh(self,h,cmd):
        '''
        调用批量执行linux命令
        :return:
        '''
        ssh_func.ssh_func(h,cmd)

    def put_file(self,h,cmd):
        '''
        调用批量上传/下载文件方法
        :return:
        '''
        print(cmd)
        putfile.put_file(h,cmd)

    def action(self,dict_type, server_tuple,func_str):
        '''
        通用动作函数，适用于操作数据库和操作系统
        :param dict_type: 操作动作字典
        :param server_tuple: 服务器列表
        :param func_str: 执行的函数名，反射函数中适用
        :return:
        '''
        while True:
            n = 1
            for i in dict_type:
                print(n, i)
                n += 1
            cmd_choice = input("\033[32;0mEnter your choice(or quit to exit!):\033[0m").strip()
            if not cmd_choice:
                continue
            if cmd_choice in dict_type:
                cmd = dict_type.get(cmd_choice)  # 取得字典中的值
            elif cmd_choice == 'quit':
                sys.exit()
            elif cmd_choice == '3':
                break
            else:
                print("非法操作!")
                continue
            for h in server_tuple:
                self.interactive(h,func_str,cmd)
            print('\033[1;31;40mComplete\033[0m')

    def single_action(self):
        '''
        查询单个服务器的信息
        :return:
        '''
        pass

    def interactive(self,h,command_str,cmd):
        '''
        交互程序
        :return:
        '''
        if hasattr(self,command_str):
            func = getattr(self,command_str)
            func(h,cmd)
        else:
            print("[%s] 非法命令..." %401)
            #self.help()

def main():
    os.system('cls')
    #os.system('clear') # linux or MacOS
    print('\033[32;1mWelcome to the Manager System!\033[0m')

    while True:   #程序主菜单
        #管理员登陆验证
        username = input("Username:").strip()
        password = input("Password:").strip()
        db_conn = db_connect.MysqlConnect(username,password)
        mark = db_conn.login_check()
        if mark == 0:
            print('\033[31;1mUsername or password wrong!Please try again!\033[0m')
        elif mark == 1:     #1验证成功
            print('\033[32;1mLogin Success!\033[0m')
            #打印主机列表
            print('The server list are as follow:')
            db_conn = db_connect.MysqlConnect(username)
            servers = db_conn.return_server()  #从数据库中返回用户元组
            for server in servers:
                print("%s:%s" %(server[0],server[1]))

            print('''\033[32;1m选择执行方式：
                        1. 批量执行
                        2. 选择主机
                        3. 返回
                        4. 退出\033[0m
                        ''')
            choice_type = input('\033[32;1mYour choice:\033[0m').strip()
            if choice_type == '1':
                server_tuple = db_conn.return_server()
            elif choice_type == '2':
                ip = input('输入主机IP地址：')
                server_tuple = db_conn.return_sigle_server(ip)
            print(server_tuple)
            while True:
                #使用字典，方便反射方法里取到对应的函数名（key）
                action_dict = {'1':'run_oracle',
                               '2':'run_ssh',
                               '3':'put_file',
                               '4':'exit'}
                print('''What do you want to do?
                         1. 批量执行oracle命令.
                         2. 批量执行linux命令.
                         3. 批量上传/下载文件.
                         4. 退出''')
                choice = input('\033[32;1mYour choice:\033[0m').strip()
                if not choice:
                    continue
                if choice in action_dict:
                    func_str = action_dict.get(choice)
                    print(func_str)
                    if choice == '1':
                        dict_type = sqlfile.DBMSG_DICT.copy()  # 复制sqlfile中的字典
                        rs = RemoteSSH()  # 实例化类
                        rs.action(dict_type, server_tuple, func_str)
                    elif choice == '2':
                        dict_type = sqlfile.OSMSG_DICT.copy()  # 复制sqlfile中的字典
                        rs = RemoteSSH()  # 实例化类
                        rs.action(dict_type, server_tuple, func_str)
                    elif choice == '3':
                        while True:
                            file_name = input("\033[32;0mEnter your put filename,(or quit to exit!):\033[0m").strip()
                            if not file_name:
                                continue
                            if os.path.isfile(file_name):
                                for h in server_tuple:
                                    rs = RemoteSSH()  # 实例化类
                                    rs.interactive(h, func_str, file_name)
                            elif file_name == 'quit':
                                sys.exit()
                            elif file_name == '3':
                                break
                            else:
                                print('输入错误！')

                else:
                    print("\033[31;1m输入错误！\033[0m")


if __name__ == "__main__":    #必须写
    main()