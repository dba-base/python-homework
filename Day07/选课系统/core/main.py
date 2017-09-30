__author__ = "xiaoyu hao"

import os
import shelve
from conf import settings
from src.School import School

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
                Student_view()
            elif user_option == '2':
                Teacher_view()
            elif user_option == '3':
                School_view()
            elif user_option == 'q':
                break
            else:
                print("输入不正确")

class School_view(object):
    #初始化数据文件
    def __init__(self):
        #判断有没有数据文件，有则打开，没有则新建
        if os.path.exists(settings.school_file + '.dat'):
            if os.path.getsize(settings.school_file + '.dat') != 0:
                self.school_db = shelve.open(settings.school_file)
                self.school_manager()
                self.school_db.close()
            else:
                print('没有创建学校，请创建！')
                self.create_school()
                self.school_manager()
                self.school_db.close()

        else:
            print('没有创建学校，请创建！')
            self.create_school()
            self.school_manager()
            self.school_db.close()

    def create_school(self):
        '''
        创建学校
        :return:
        '''
        self.school_db = shelve.open(settings.school_file)       # 打开文件
        self.school_db['北京'] = School('oldboy北京总部','北京')
        self.school_db['上海'] = School('oldboy上海分部','上海')

    def school_manager(self):
        '''
        校区操作方法，包括添加课程，添加讲师，添加班级，查看讲师、班级、课程
        :return:
        '''
        while True:
            for school_name in self.school_db:
                print('学校名称：%s' %school_name )

            school_option = input('请输入对应的学校名称：').strip()
            if school_option in self.school_db:
                self.school_option = school_option
                self.school_obj = self.school_db[school_option]   #取得学校对象
                while True:
                    menu = '''
                    欢迎来到oldboy 【%s】校区
                    1.添加课程 add_course
                    2.添加讲师 add_teacher
                    3.添加班级 add_classroom    
                    4.查看讲师 show_teacher
                    5.查看班级 show_classroom
                    6.查看课程 show_course
                    7.退出程序 exit
                    ''' %school_option
                    print(menu)
                    #需要优化，通过数字区分响应操作
                    user_choice = input('选择以上的操作：').strip()
                    if hasattr(self,user_choice):
                        getattr(self,user_choice)()
            else:
                print('学校不存在，请输入正确的学校名称!')

    def add_course(self):
        course_name = input("请输入课程名称：").strip()
        if course_name in self.school_obj.sch_course:
            print("【%s】课程已经存在" %course_name)
        else:
            course_price = input("请输入课程价格：").strip()
            course_cycle = input("请输入课程周期：").strip()
            self.school_obj.create_course(course_name,course_price,course_cycle)
            print("[%s]课程添加成功！")
        self.school_db.update({self.school_option:self.school_obj})   #更新shelve数据文件

    def add_teacher(self):
        teach_name = input('').strip()
        sex = input('').strip()
        age = input('').strip()
        salary = input('').strip()
        classroom_name = input('').strip()
        if classroom_name in self.school_obj.sch_classroom:
            classroom_obj = self.school_obj.sch_classroom[classroom_name]
            if teach_name not in self.school_obj.sch_teacher:
                self.school_obj.create_teacher(teach_name, sex, age, salary, classroom_name, classroom_obj)
                print("讲师添加成功！")
            else:
                print("讲师已存在！")
            self.school_db.update({self.school_option:self.school_obj})

    def add_classroom(self):
        class_name = input('请输入班级名：').strip()
        couser_name = input('输入课程名：').strip()
        if class_name not in self.school_obj.sch_classroom:
            if couser_name in self.school_obj.sch_course:
                course_obj = self.school_obj.sch_course[couser_name]
                self.school_obj.create_classroom(class_name, course_obj)
                self.school_db.update({self.school_option:self.school_obj})
                print("课程新增成功！")
            else:
                print('课程不存在！')
        else:
            print('班级已存在！')


    def show_teacher(self):
        self.school_obj.show_teacher_info()

    def show_classroom(self):
        self.school_obj.show_classroom_info()

    def show_course(self):
        self.school_obj.show_course_info()

    def exit(self):
        self.school_db.close()
        exit('欢迎下次使用！')

class Teacher_view(object):
    def __init__(self):
        if os.path.exists(settings.school_file+'.dat'):
            self.school_db = shelve.open(settings.school_file)
            self.teacher_manager()
            self.school_db.close()
        else:
            print('学校都不存在创建个鸡吧讲师！')
            exit()

    def teacher_manager(self):
        print('欢迎进入讲师视图：')
        for school_name in self.school_db:
            print('学校名称：%s' % school_name)
        school_option = input('请输入对应的学校名称：').strip()
        if school_option in self.school_db:
            self.school_obj = self.school_db[school_option]  # 取得学校对象
            teacher_name = input('输入讲师的名字：').strip()
            if teacher_name in self.school_obj.sch_teacher:
                while True:

                    menu = '''
                        欢迎来到oldboy 【%s】校区
                        1.查看班级 show_classroom
                        2.修改成绩 modify_stu_score
                        3.退出系统 exit
                        ''' % school_option
                    print(menu)
                    # 需要优化，通过数字区分响应操作
                    user_choice = input('选择以上的操作：').strip()
                    if hasattr(self, user_choice):
                        getattr(self, user_choice)(teacher_name)
        else:
            print('学校不存在，请输入正确的学校名称!')

    def show_classroom(self,teacher_name):
        self.school_obj.show_teacher_student_info(teacher_name)

    def modify_student_score(self,teacher_name):
        student_name = input("请输入学生姓名：").strip()
        if student_name in self.school_obj.sch_student:
            new_score = input("输入分数：").strip()
            self.modify_stu_score(teacher_name,student_name,new_score)
            self.school_db.update({self.school_option:self.school_obj})
            print("修改成功！")
        else:
            print("学生不存在！")

    def exit(self):
        exit("退出！")





class Student_view(object):
    def __init__(self):
        if os.path.exists(settings.school_file + '.dat'):
            self.shcool_db = shelve.open(settings.school_file)
            self.student_manager()
            self.shcool_db.close()
        else:
            print('煞笔，学校不存在！')
            exit()

    def student_manager(self):
        print('欢迎来到学生管理视图')
        for sch_name in self.shcool_db:
            print('学校名称：[%s]' %sch_name)

        choice = input('选择学校名：').strip()
        if choice in self.shcool_db:
            self.school_obj = self.shcool_db[choice]
            stu_name = input('请输入学生姓名：')
            if stu_name in self.school_obj.sch_student:
                stu_sex = input()
                stu_age = input()
                classroom_name = input()
                if classroom_name in self.school_obj.sch_classroom:
                    self.school_obj.create_student(stu_name, stu_sex, stu_age, classroom_name)
                    self.school_db.update({self.choice:self.school_obj})
                    print('学生注册成功！')

                else:
                    print('班级不存在！')
                    exit()
            else:
                print('学生已存在！')
                exit()
        else:
            print('学校不存在！')
            exit()





