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
    tablespace_dic = {'ip': ip}
    result  = BasePlugin(**kwargs).ora_connect(sqlsets.TABLESPACE_SQL,2)
    run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    for tbs in result:
        tablespace_dic[tbs[0]] = tbs[1:]
    tablespace_dic['time'] = run_time
    return tablespace_dic


# if __name__ == "__main__":
#
#     # url = "http://%s:%s%s" % (settings.Params['server'], settings.Params['port'], settings.Params['url'])
#     # data = {"tbs_data": json.dumps(info_tablespace())}
#     # print(data)
#     # print('正在将数据发送至： [%s]  ......' % url)
#     # data_encode = parse.urlencode(data).encode('utf-8')
#     # print(data_encode)
#     # print(type(data_encode))
#     # response = request.urlopen(url=url, data=data_encode, timeout=settings.Params['request_timeout'])
#     # print("\033[31;1m发送完毕！\033[0m ")
#     # message = response.read().decode()
#     # print("返回结果：%s" % message)
#     #
#     # for i in range(3):
#     host_message = {'192.168.2.128': ['root', 'oracle', 22,'scott','tiger','PROD',1521]}
#     a = monitor(**host_message)
#     print(a)

