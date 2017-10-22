__author__ = "xiaoyu hao"


import os
import sys
import json
#程序基目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)
from conf import settings
from src import auth_user
from src import socket_server

def create_db():
    '''
    简单的用户文件初始化工作
    :return:
    '''
    user_database = {}
    auth = auth_user.User_auth()
    limitsize = settings.LIMIT_SIZE
    #遍历用户字典
    for k,v in settings.USERS_PWD.items():
        username = k
        password = auth.hash(v)
        user_db_path = settings.DATABASE + r"/%s.db"%username
        user_home_path = settings.HOME_PATH + r"/%s"%username
        print(user_home_path)
        user_database["username"] = username
        user_database["password"] = password
        user_database["limitsize"] = limitsize
        user_database["homepath"] = user_home_path
        if not os.path.isfile(user_db_path):
            with open(user_db_path,'w') as f:
                f.write(json.dumps(user_database))
        else:
            print("文件[%s.db]已存在！"%username)
        create_dir(user_home_path)

def create_dir(path):
    '''
    创建用户的家目录
    :return:
    '''
    if not os.path.isdir(path):
        os.popen("mkdir %s" %path)
    else:
        print("目录[%s]已存在！"%path)

if __name__ == "__main__":
    '''初始化数据并启动程序'''
    create_db()
    socket_server.run()






