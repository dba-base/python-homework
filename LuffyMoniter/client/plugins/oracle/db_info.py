__author__ = "xiaoyu hao"

import jaydebeapi
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.getcwd()))
# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)
from conf import settings
from conf import sqlsets

def info_tablespace():
    tablespace_list = []
    result = get_tablespace()
    for tbs in result:
        tablespace_list.append(list(tbs))
    return tablespace_list


def get_tablespace():
    conn=jaydebeapi.connect(settings.db_params['driver'],[settings.db_params['url'],settings.db_params['user'],settings.db_params['password']],settings.db_params['jarFile'])
    curs = conn.cursor()
    curs.execute(sqlsets.TABLESPACE_SQL)
    result=curs.fetchall()
    print(result)
    curs.close()
    conn.close()
    return result

if __name__ == "__main__":
    tbs_list=info_tablespace()

