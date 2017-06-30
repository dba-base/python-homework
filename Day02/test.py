__author__ = "xiaoyu hao"

def show_goods_list():
    with open("shopping_list", 'r') as f:
        for i in f.readlines():
            print(i)

show_goods_list()