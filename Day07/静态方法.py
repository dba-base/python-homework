

class Dog(object):

    def __init__(self,name):
        self.NAME = name

    @staticmethod
    def eat(self):
        print("%s is eating %s " %(self.NAME,"baozi"))

d = Dog("chengronghua")
d.eat(d)