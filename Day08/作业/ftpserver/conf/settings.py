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
IP_PORT = ('0.0.0.0',9999)