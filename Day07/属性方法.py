

class Dog(object):

    food = "baozi"

    def __init__(self,name):
        self.NAME = name
        self.__food = None

    @property
    def eat(cls):   #cls 代表类而不是实例
        print("%s is eating %s " % ("aaa",cls.__food))

    @eat.setter      #修改类方法中的变量
    def eat(cls,food):
        print("food is set :",food)
        cls.__food = food
    @eat.deleter
    def eat(self):
        del self.__food
        print("删完了")

d = Dog("chengronghua")
d.eat   #作为属性调用

#修改属性，调用@eat.setter
d.eat = "mantou"

d.eat

#删除属性，调用上面的 @eat.deleter 方法
del d.eat

