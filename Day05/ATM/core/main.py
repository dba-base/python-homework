__author__ = "xiaoyu hao"

from core import auth
from core import logger

#交易日志
trans_logger = logger.logger('transaction')
#登陆日志
access_logger = logger.logger('access')

user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None

}

def account_info(acc_data):
    '''
    用户信息
    :return:
    '''
    print("------- [%s] information ------- " %user_data["account_id"])
    for info in acc_data:
        print("%s : %s" % (info,acc_data[info]))

def repay():
    '''
    还款
    :return:
    '''
    pass

def withdraw():
    '''
    取款
    :return:
    '''
    pass

def transfer():
    '''
    转账
    :return:
    '''
    pass

def pay_check():
    '''
    账单查询
    :return:
    '''
    pass

def logout():
    pass

def interaction(acc_data):
    '''
    ATM程序入口
    :return:
    '''
    menu = '''
    \033[32;1m1. 账户信息
    2. 还款
    3. 取款
    4. 转账
    5. 账单查询
    6. 退出\033[0m
    '''
    menu_dict = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout
    }

    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dict:
            menu_dict[user_option](acc_data)
        else:
            print("\033[31;1mOption is invalid!\033[0m")


def run():
    '''

    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        print(user_data)
        interaction(acc_data)
