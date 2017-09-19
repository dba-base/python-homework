__author__ = "xiaoyu hao"

import os
import shelve
from conf import settings
from src import School

'''
主功能入口类
'''
class Center(object):

    def run(self):
        exit_flag = False
        menu = '''
        -----------Welcome to oldboy school --------
        \033[32;1m
        1.学生视图
        2.讲师视图
        3.学校视图
        4.退出
        \033[0m
        '''
        while not exit_flag:
            print(menu)
            user_option = input("请输入操作序号：q退出")
            if user_option == '1':
                Student_view
            elif user_option == '2':
                Teacher_view()
            elif user_option == '3':
                School_view()
            elif user_option == 'q':
                break
            else:
                print("输入不正确")

class School_view(object):
    def __init__(self):
        pass

class Teacher_view(object):
    def __init__(self):
        pass

class Student_view(object):
    def __init__(self):
        pass


