__author__ = "xiaoyu hao"

from conf import settings
from core import accounts
from core import logger

def make_transaction(log_obj,account_data,trans_type,amount,**otherss):
    '''
    处理交易事务
    :param log_obj: 日志对象
    :param account_data: 账户信息
    :param tran_type: 交易的类型
    :param amount: 利息
    :param otherss:
    :return:
    '''
    amount = float(amount)
    if trans_type in settings.TRANSACTION_TYPE:
        interest = amount * settings.TRANSACTION_TYPE[trans_type]["interest"]
        old_balance = account_data["balance"]
        if settings.TRANSACTION_TYPE[trans_type]["action"] == "plus":
            new_balance = old_balance + amount + interest
        elif settings.TRANSACTION_TYPE[trans_type]["action"] == 'minus':
            new_balance = old_balance - amount - interest
            if new_balance < 0:
                print('''You credit [%s] is not enough for this transaction [-%s],
                your current balance is [%s]'''
                      %(account_data['credit'],(amount + interest), old_balance))
                return

        account_data['balance'] = new_balance

    else:
        print("\033[31;1mTransaction type [%s] is not exist!\033[0m" % trans_type)

