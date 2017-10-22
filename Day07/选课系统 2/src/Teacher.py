'''
讲师类
'''

class Teacher(object):

    #定义讲师姓名，性别，年龄，工资，所带的班级字典
    def __init__(self,name,sex,age,salary):
        self.teach_name = name
        self.teach_sex = sex
        self.teach_age = age
        self.teach_sal = salary
        self.teach_classroom = {}   #班级名：班级对象

    #添加及更新所带的班级
    def add_teach_classroom(self,classroom_name,classroom_obj):
        self.teach_classroom[classroom_name] = classroom_obj


