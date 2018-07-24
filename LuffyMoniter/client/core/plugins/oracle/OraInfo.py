# __author__ = "xiaoyu hao"
#
# __author__ = "xiaoyu hao"
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(BASEDIR)
# #print(BASEDIR)
import datetime
from core.plugins.base import BasePlugin

from conf import sqlsets

def monitor(frist_invoke=1,**kwargs):
    '''
    转换取得表空间列表为字典格式。
    :return:
    '''
    for i,v in kwargs.items():
        ip = i
    result  = BasePlugin(**kwargs).ora_connect(sqlsets.DBSIZE,1)
    result1  = BasePlugin(**kwargs).ora_connect(sqlsets.PATCH_SQL,1)
    re_dict = {
        'ip': ip,
        "instance_name":result[3],
        "time":result[0],
        "version": result1[3],
        "PSU": result1[6],
        "dbfile_size":float('%.2f'%result[1]),
        "segment_size":float('%.2f'%result[2]),
        "free_size":float('%.2f'%result[4])
    }
    return re_dict


if __name__ == "__main__":
    host_message = {'192.168.2.128': ['root', 'oracle', 22, 'scott', 'tiger', 'PROD', 1521]}
    a = monitor(**host_message)
    print(a)


