
__author__ = "Alex Li"

def bulk(self):
    print("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating..."%self.name,food)


d = Dog("NiuHanYang")
choice = input(">>:").strip()

if hasattr(d,choice):
    #func = getattr(d,choice)
    #func("chengronghua")
    delattr(d,choice)   #删除
    print("已删除")

else:
    #setattr(d,choice,bulk) #d.talk = bulk    setattr(x, 'y', v) is equivalent to ``x.y = v''   bulk相当于变量名
    #func = getattr(d, choice)   #如果传入的是方法，打印的是内存地址
    #func(d)

    #传入变量
    setattr(d,choice,22)
    print(getattr(d,choice))    #如果传入的是变量，直接打印变量值

print(d.name)