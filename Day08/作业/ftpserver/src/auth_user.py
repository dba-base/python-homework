__author__ = "xiaoyu hao"

import json
import os
import hashlib
from conf import settings

class User_auth(object):
    '''
    验证用户身份,登陆成功返回用户信息，登陆失败返回null
    '''
    def authentication(self,login_info):
        list = login_info.split(':')
        login_name = list[0]
        login_password = self.hash(list[1])
        DB_FILE = settings.DATABASE + "/%s.db" %login_name

        if os.path.isfile(DB_FILE):
            user_data = self.cat_database(DB_FILE)   #读取用户信息
            if login_name == user_data["username"]:
                if login_password == user_data["password"]:
                    return user_data

    def hash(self,passwd):
        '''
        对用户密码进行md5加密
        :param passwd: 用户密码
        :return:
        '''
        m = hashlib.md5()
        m.update(passwd.encode("utf-8"))
        return m.hexdigest()

    def cat_database(self,file):
        '''
        读取数据文件中用户的信息
        :param file: 用户信息文件
        :return:
        '''
        with open(file,"r") as f:
            data = json.loads(f.read())
            return data

