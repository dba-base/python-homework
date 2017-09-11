

#定义类
class Dog(object):
    #传参数,self,就是实例本身！你实例化时python会自动把这个实例本身通过self参数传进去
    def __init__(self,name):    #构造函数，构造方法，初始化方法
        self.Name = name


    #类的方法
    def sayhi(self):
        print("hello,",self.Name,"is a dog!")

    def eat(self,food):
        print("%s is eating %s"%(self.Name,food))


#类的实例化

d = Dog("alex")     #Dog(d,"alex")   实例化后产生的对象就叫 实例
d2 = Dog("alex2")

#调用类中的方法
d.sayhi()
d2.sayhi()

d.eat("馒头")