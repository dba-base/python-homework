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
    result  = BasePlugin(**kwargs).ora_connect(sqlsets.DBWAIT_EVENT,2)
    run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    re_dict = {"ip":ip}
    for event in result:
        re_dict[event[0]] = event[1]
    re_dict["time"] = run_time

    return re_dict


if __name__ == "__main__":
    host_message = {'192.168.2.128': ['root', 'oracle', 22, 'scott', 'tiger', 'PROD', 1521]}
    a = monitor(**host_message)
    print(a)


