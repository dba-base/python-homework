__author__ = "xiaoyu hao"

import os,sys
#import module01

#找到模块的路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from module01 import logger
from module01 import logger as logger_alex

#去调用父父目录下的模块


#调用变量
#print(module01.name)

#调用方法
#module01.sayhi()

def logger():
    print("in the main's logger")

logger()

logger_alex()