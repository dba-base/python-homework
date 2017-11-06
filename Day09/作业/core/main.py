__author__ = "xiaoyu hao"

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from multiprocessing import Pool
from core import db_connect
from core import query_oracle
from conf import sqlfile
import threading

class RemoteSSH(object):
    def __init__(self,h,cmd):
        self.h = h
        self.cmd =cmd
    def run_oracle(self):
        query_oracle.run(h,cmd)

def main():
    os.system('cls')
    #os.system('clear') # linux or MacOS
    print('\033[32;1mWelcome to the Manager System!\033[0m')

    while True:   #程序主菜单
        #登陆
        username = input("Username:").strip()
        password = input("Password:").strip()

        db_conn = db_connect.MysqlConnect(username,password)
        mark = db_conn.login_check()
        if mark == 0:
            print('\033[31;1mUsername or password wrong!Please try again!\033[0m')
        elif mark == 1:
            print('\033[32;1mLogin Success!\033[0m')
            print('The server list are as follow:')
            db_conn = db_connect.MysqlConnect(username)
            server_tuple = db_conn.return_server()  #从数据库中返回用户元组
            for server in server_tuple:
                print("%s:%s" %(server[0],server[1]))
            while True:
                print(
                '''What do you want to do?    
            1.Execute the oracle command batch.
            2.Execute the oracle command batch.
            3.Distribute file(s) batch.
            4.Exit.''')
                choice = input('\033[32;1mYour choice:\033[0m').strip()
                if choice == '1':
                    threads = []   #存放线程
                    DB_DICT = sqlfile.DBMSG_DICT.copy()  # 复制sqlfile中的字典
                    while True:
                        n = 1
                        for i in DB_DICT:
                            print(n,i)
                            n += 1
                        cmd_choice = input("\033[32;0mEnter your choice(or quit to exit!):\033[0m").strip()
                        if cmd_choice in DB_DICT:
                            cmd = sqlfile.DBMSG_DICT.get(cmd_choice)  #取得字典中的值
                        elif cmd_choice == 'quit':
                            sys.exit()
                        else:
                            print("非法操作!")
                            continue
                        for h in server_tuple:
                            rs = RemoteSSH(h,cmd)    #实例化类
                            t1 = threading.Thread(target=rs.run_oracle())
                            t1.start()  #启动进程
                            threads.append(t1)
                        for t in threads:
                            print(t)
                            t.join() # 主线程等待子线程执行完毕
                        print("执行完成！")
                        threads.clear()
                elif choice == '2':
                    pass
                else:
                    print("\033[31;1m输入错误！\033[0m")


if __name__ == "__main__":    #必须写
    main()