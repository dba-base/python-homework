'''
学生类
'''


class Student(object):

    #初始化学生姓名，性别，年龄
    def __init__(self,name,sex,age):
        self.stu_name = name
        self.stu_sex = sex
        self.stu_age = age
        self.stu_score = 0 #初始化学生的成绩为0，讲师可更改


    def modify_score(self,new_score):
        self.stu_score = new_score

