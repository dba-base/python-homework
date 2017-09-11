

class Person(object):

    def __init__(self,name,age):
        self.Name = name
        self.Age = age

    def talk(self):
        print(self.Name,"person is talking ...")

class BlackPerson(Person):

    def __init__(self,name,age,strength):   #先继承，再重载
        Person.__init__(self,name,age)    #继承父类的变量
        self.Strength = strength   #实现自己的变量

    def walk(self):
        print("is walking ....")

b = BlackPerson("hao",18)

b.talk()