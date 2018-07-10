__author__ = "xiaoyu hao"

__author__ = "xiaoyu hao"
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(BASEDIR)
#print(BASEDIR)
import jaydebeapi
import json
import datetime
from core.plugins.base import BasePlugin

from urllib import request, parse
from conf import sqlsets

def monitor(frist_invoke=1,**kwargs):
    '''
    转换取得表空间列表为字典格式。
    :return:
    '''
    for i,v in kwargs.items():
        ip = i
    result  = BasePlugin(**kwargs).oracle_connect(sqlsets.DBSIZE)
    result1  = BasePlugin(**kwargs).oracle_connect(sqlsets.DBSIZE)
    result = list(result[0])
    re_dict = {
        'ip': ip,
        "instance_name":result[3],
        "time":result[0],
        "dbfile_size":float('%.2f'%result[1]),
        "segment_size":float('%.2f'%result[2])
    }
    return re_dict

# if __name__ == "__main__":
#
#     host_message = {'192.168.2.128': ['root', 'oracle', 22,'scott','tiger','PROD',1521]}
#     a = monitor(**host_message)
#     print(a)
