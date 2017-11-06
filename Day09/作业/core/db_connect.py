__author__ = "xiaoyu hao"

import pymysql

class MysqlConnect(object):

    conn = pymysql.connect(host = 'localhost', user = 'root',passwd = 'root', db = 'test', port = 3306)
    cur = conn.cursor()

    def __init__(self,username,password="NULL"):
        self.username = username
        self.password = password

    def login_check(self):
        '''
        连接管理系统账号信息数据库并验证用户名密码信息
        :return:
        '''
        sql = "select * from users where username = '%s' and passwoord = '%s'" \
              % (self.username,self.password)
        try:
            self.cur.execute(sql)
            qur_result = self.cur.fetchall()

            if qur_result == ():
                return 0
            else:
                return 1
            self.cur.close()
            self.conn.close()
        except pymysql.Error as e:
            print('\033[31;1mMysql Error Msg:%s\033[0m' % e)

    def return_server(self):
        '''
        返回主机列表
        :return:元组
        '''
        sql = "select * from host_info"
        self.cur.execute(sql)
        qur_result = self.cur.fetchall()
        return qur_result

# db = MysqlConnect("root")
# result = db.return_server()
#
# for i in result:
#     print(i[1])