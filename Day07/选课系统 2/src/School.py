'''
学校类
'''
from src import ClassRoom
from src.Course import Course
from src import Student
from src import Teacher
class School(object):

    #初始化学校名称 学校地址 班级字典 课程字典 学生字典 讲师字典
    def __init__(self,name,address):
        self.sch_name = name
        self.sch_addr = address
        self.sch_classroom = {}
        self.sch_course = {}
        self.sch_teacher = {}
        self.sch_student = {}

    # 创建课程
    def create_course(self,course_name,course_price,course_cycle):
        course_obj = Course(course_name,course_price,course_cycle)   #实例化课程
        self.sch_course[course_name] = course_obj    #更新字典

    #查看课程信息
    def show_course_info(self):
        for course_name in self.sch_course:
            course_obj = self.sch_course[course_name]
            print("课程名称：[%s]\t 课程价格：[%s]\t 课程周期:[%s]\t"
                  %(course_obj.course_name,course_obj.course_price,course_obj.course_cycle))

    # 创建班级
    def create_classroom(self,class_name,course_obj):
        classroom_obj = ClassRoom(class_name,course_obj)   #实例化班级
        self.sch_classroom[class_name] = classroom_obj     #更新字典

    # 查看班级信息
    def show_classroom_info(self):
        for class_name in self.sch_classroom:
            classroom_obj = self.sch_classroom[class_name]
            print("班级名称：[%s] 课程名称：[%s]\t" %(classroom_obj.class_name,classroom_obj.class_course.course_name))


    #创建讲师
    def create_teacher(self,teach_name,sex,age,salary,classroom_name,classroom_obj):
        teacher_obj = Teacher(teach_name,sex,age,salary)
        teacher_obj.add_teach_classroom(classroom_name,classroom_obj)
        self.sch_teacher[teach_name] = teacher_obj

    #更改讲师授课班级
    def modify_teacher_info(self,teach_name,classroom_name,classroom_obj):
        teacher_obj = self.sch_teacher[teach_name]
        teacher_obj.add_teach_classroom(classroom_name, classroom_obj)

    def show_teacher_info(self):
        for teach_name in self.sch_teacher:
            teach_obj = self.sch_teacher[teach_name]
            classroom_list = []
            for c in teach_obj.teach_classroom:
                classroom_list.append(c)
            print("讲师姓名：[%s] \t 讲师性别:[%s]\t 讲师年龄:[%s]\t 讲师工资[%s]\t 所带班级[%s]\t"
                  %(teach_obj.teach_name,teach_obj.teach_sex,teach_obj.teach_age,teach_obj.teach_salary,classroom_list))

    #创建学生
    def create_student(self,stu_name,stu_sex,stu_age,classroom_name):
        student_obj = Student(stu_name,stu_sex,stu_age)   #实例化学生
        self.sch_student[stu_name] = student_obj          #学生对象存放到字典里
        #学生加入到班级
        classroom_obj = self.sch_classroom[classroom_name]
        classroom_obj.class_student[stu_name] = student_obj
        self.sch_classroom[classroom_name] = classroom_obj   #更新班级字典

    #查询学生和讲师的信息，讲师 -- 班级 -- 学生
    def show_teacher_student_info(self,teach_name):
        teacher_obj = self.sch_teacher[teach_name]
        for i in teacher_obj.teach_classroom:
            classroom_obj = self.sch_classroom[i]
            student_list = []
            for j in classroom_obj.class_student:
                print("班级名称： [%s]\t课程：[%s]\t 学生：[%s]\t"
                      %(classroom_obj.class_name,classroom_obj.class_course.course_name,student_list))

        student_list.append(j)
    #更改学生的成绩
    def modify_stu_score(self,tech_name,student_name,new_score):
        teacher_obj = self.sch_teacher[tech_name]
        for i in self.sch_classroom:     #i为班级名
            classroom_obj = teacher_obj.teach_classroom[i]
            for j in classroom_obj.class_student: #j为学生名
                stu_obj = classroom_obj.class_student[j]
                if stu_obj.stu_name == student_name:
                    stu_obj.modify_score(new_score)
            print("学生[%s]的成绩已经从：[%s]修改为：[%s]" %(student_name,stu_obj.stu_score,new_score))






