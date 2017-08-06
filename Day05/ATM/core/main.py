__author__ = "xiaoyu hao"

from core import auth
from core import logger
from core import accounts
from core import transaction

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

def repay(acc_data):
    '''
    还款
    :return:
    '''
    '''
        print current balance and let user do the withdraw action
        :param acc_data:
        :return:
        '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
            Credit :    %s
            Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)

        if withdraw_amount == 'b':
            back_flag = True


def withdraw(acc_data):
    '''
    取款
    :return:
    '''
    '''
        print current balance and let user do the withdraw action
        :param acc_data:
        :return:
        '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
            Credit :    %s
            Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)

        if withdraw_amount == 'b':
            back_flag = True


def transfer(acc_data):
    '''
    转账
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
                Credit :    %s
                Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        receiver = input("\033[33;1mInput receiver:\033[0m").strip()
        if receiver == acc_data["account_id"]:
            print("\033[33; receiver is yourself ... \033[0m")
        elif receiver == "b":
            back_flag = True
        else:
            #判断收款人是否存在,存在返回用户信息，不存在返回False
            receiver_account_data = auth.auth_check(receiver)
            if receiver_account_data:
                if receiver_account_data["status"] == 0:  #检查收款人的状态是否正常
                    transfer_amount = input("\033[33;1mInput transfer amount:\033[0m").strip()
                    if len(transfer_amount) > 0 and transfer_amount.isdigit():
                        new_balance = transaction.make_transaction(trans_logger, account_data, 'transfer', transfer_amount)
                        transaction.make_transaction(trans_logger, receiver_account_data, 'repay',transfer_amount)
                        if new_balance :
                            print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
                            back_flag = True

                    else:
                        print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % transfer_amount)

                    if transfer_amount == 'b':
                        back_flag = True
            else:
                continue




def pay_check():
    '''
    账单查询
    :return:
    '''
    pass

def logout(acc_data):
    exit("Bye,thanks! [%s],welcome to next login".center(50, "#") %acc_data["account_id"])

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
        interaction(user_data)
