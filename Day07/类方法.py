

class Dog(object):

    food = "baozi"

    def __init__(self,name):
        self.NAME = name

    @classmethod
    def eat(cls):   #cls 代表类而不是实例
        print("%s is eating %s " % ("aaa", cls.food))
        print("cls name is :",cls.__name__)

d = Dog("chengronghua")
d.eat()