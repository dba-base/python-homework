

class SchoolMember(object):

    member = 0

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        '''注册'''
        print("just enrolled a new school member [%s]" % self.name)
        SchoolMember.member += 1

    def tell(self):
        '''打印用户信息'''
        print('---------- info %s ----------' % self.name)
        for k,v in self.__dict__.items():
            print("\t",k,v)


    def __del__(self):
        print("开除了【%s】" % self.name)


class School(object):

    def open_branch(self,addr):
        print("open branch school %s" % addr)


class Teacher(SchoolMember,School):   #多继承
    '''老师类'''
    def __init__(self,name,age,sex,salary,course):
        #SchoolMember.__init__(self,name,age,sex)   #经典类写法
        super(Teacher).__init__(name,age,sex)  #新式类写法

        self.salary = salary
        self.course = course


    def teaching(self):
        print("Teacher [%s] is teaching [%s]" %(self.name,self.course))

class Student(SchoolMember):

    def __init__(self,name,age,sex,course,tuition):
        SchoolMember.__init__(self,name,age,sex)
        self.course = course
        self.tuition = tuition #fee
        self.amount = 0

    def pay_tuition(self,amount):
        print("student [%s] has just paied [%s]" %(self.name ,amount))
        self.amount += amount

t1 = Teacher("wuser",23,"f",3000,"python")
s1 = Student("hao",23,"F","PY",3000)
s2 = Student("rendelei",23,"F","PY",3000)


t1.tell()
s1.tell()
t1.open_branch("SH")