'''
班级类
'''

class ClassRoom(object):

    #定义班级名称，课程对象，学生字典
    def __init__(self,class_name,course_obj):
        self.class_name = class_name
        self.class_course = course_obj
        self.class_student = {}



