__author__="xiaoyu hao"

'''
购物车：
用户入口：
1.商品信息放到文件中
2.已购商品，余额记录

商家入口：
可以添加商品，修改商品价格
'''

import os

def get_salary():
    salary = input("Please input salary:")
    if __is_valid_num(salary):
        return int(salary)
    else:
        print('输入非法，请输入一个数字！')

#显示商品
def show_goods_list():
     print('------------shopping list------------')
     with open('db/warehouse_list', 'r',encoding='UTF-8') as f:
         result = list(line.strip().split(' ') for line in f if line)
     return result

def update_goods_list(choice):
    if choice == 'add':
        goods_name = input("Goods Name:")
        goods_price = input("Goods Price:")
        goods_file = open('db/warehouse_list', 'a',encoding='UTF-8')
        goods_file.write('\n')
        goods_file.write(goods_name+' '+goods_price)
    elif choice == 'delete':
        pass
    elif choice == 'update':
        pass
    else:
        pass

def __is_valid_num(num):
    if num.isdigit():
        return True
    else:
        return False

#显示购物车商品
def get_shopping_list():
    print('------------shopping cart------------')
    with open('db/shopping_list', 'r', encoding='UTF-8') as f:
        result = list(line.strip().split(' ') for line in f if line)
    if len(result) == 1:
        print("你购物车里空空如也，赶紧去买点东西吧!")
    else:
        for index, item in enumerate(result):
            print(index, item[0], item[1])

#更新购物车
def choice_shopping(choice_goods):
    goods_file = open('db/shopping_list', 'a', encoding='UTF-8')
    goods_file.write('\n')
    goods_file.write(choice_goods)


def main():
    salary = get_salary()
    Total_salary = int(salary)
    print("你现在有 %s 人民币！" %Total_salary)
    get_shopping_list()  #显示购物车内容

    while True:
        goods_list = show_goods_list()
        for index, item in enumerate(goods_list):
            print(index, item[0], item[1])
        user_choice = input("输入要买商品的编号(%s - %s)："%(1,len(goods_list)-1))
        if __is_valid_num(user_choice):
            user_choice = int(user_choice)
            if user_choice < len(goods_list) and user_choice > 0:
                print("Total_salary:",Total_salary)
                p_item = goods_list[user_choice]
                goods_price = int(p_item[1])
                print('p_item:',p_item)
                if goods_price <= Total_salary: #买得起
                    Total_salary -= goods_price
                    a = p_item[0] + ' ' + p_item[1]+' '+str(Total_salary)
                    print(a)
                    choice_shopping(a)
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" % (p_item[0], Total_salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，啥也买不起了，去挣钱再来吧！\033[0m" % Total_salary)
            else:
                print("prodeuct code [%s] is not exist!"%user_choice)
        elif user_choice == 'q':
            print("----------shopping list -----------------")
            get_shopping_list()
            print("You current balance:%s" % Total_salary)
            exit()
        else:
            print("非法输入，请重新输入！！")

if __name__ == '__main__':
    main()

