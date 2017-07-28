__author__ = "xiaoyu hao"

import os
import json
import time
from core import db_handler
from conf import settings

def acc_auth(account,password):
    '''
    用户验证:账户是否存在，密码是否过期等
    :param account:
    :param password:
    :return:
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" %(db_path,account)

    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'],"%Y-%m-%d"))  #把字符串转换成时间戳
                if time.time() > exp_time_stamp:
                    print("\033[031;1mAccount [%s] has expired,please contact the back to get as new card!\033[0m " %account)
                else:
                    return account_data
            else:
                print("\033[031;1mAccount Id or password is incorrect!\033[0m")
    else:
        print("\033[031;1mAccount [%s] dose not exist!\033[0m" % account)


def acc_login(user_data,log_obj):
    '''

    :param user_data:
    :param log_obj:
    :return:
    '''

    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()

        auth = acc_auth(account,password)  # 用户信息

        if auth:
            user_data["is_authenticated"] = True
            user_data["account_id"] = account
            log_obj.info("[%s] 登陆成功！" %account)
            return auth  #把用户的信息返回
        else:
            log_obj.warn("[%s] 登陆失败！" %account)
        retry_count += 1

    else:
        pass
        exit()
