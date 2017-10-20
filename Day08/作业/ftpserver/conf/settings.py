__author__ = "xiaoyu hao"

import os
import sys

#程序基目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)

print(sys.path)

#数据目录
DATABASE = os.path.join(BASE_DIR,'data')

#服务器地址
IP_PORT = ('localhost',9999)

#用户属主目录
HOME_PATH = os.path.join(BASE_DIR,"home")

#用户字典
USERS_PWD = {"root":"root","alex":"123456","haoxy":"1234"}

#磁盘配额   10M
LIMIT_SIZE = 10240000