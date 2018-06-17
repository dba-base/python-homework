__author__ = "xiaoyu hao"

import jaydebeapi
import os,sys
import json
import time

from urllib import request, parse

BASE_DIR = os.path.dirname(os.path.dirname(os.getcwd()))
# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)
from conf import settings
from conf import sqlsets

def info_tablespace():
    '''
    转换取得表空间列表为字典格式。
    :return:
    '''
    tablespace_dic = {}
    result = get_tablespace()
    for tbs in result:
        tablespace_dic[tbs[0]] = tbs[1:]
    return tablespace_dic


def get_tablespace():
    conn=jaydebeapi.connect(settings.db_params['driver'],[settings.db_params['url'],settings.db_params['user'],settings.db_params['password']],settings.db_params['jarFile'])
    curs = conn.cursor()
    curs.execute(sqlsets.TABLESPACE_SQL)
    result=curs.fetchall()
    curs.close()
    conn.close()
    return result

if __name__ == "__main__":

    url = "http://%s:%s%s" % (settings.Params['server'], settings.Params['port'], settings.Params['url'])
    data = {"tbs_data": json.dumps(info_tablespace())}
    print(data)
    print('正在将数据发送至： [%s]  ......' % url)
    data_encode = parse.urlencode(data).encode('utf-8')
    print(data_encode)
    print(type(data_encode))
    response = request.urlopen(url=url, data=data_encode, timeout=settings.Params['request_timeout'])
    print("\033[31;1m发送完毕！\033[0m ")
    message = response.read().decode()
    print("返回结果：%s" % message)


