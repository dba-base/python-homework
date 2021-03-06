__author__ = "xiaoyu hao"

#  http://egon09.blog.51cto.com/9161406/1836763

import time

#函数加参数形成通用装饰器

#高阶函数 + 嵌套函数 = 装饰器
def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)   #为了在被装饰的函数中支持输入参数
        stop_time = time.time()
        print("the func runtime is %s" %(stop_time - start_time))
    return deco   #返回deco的内存地址

# def timer():
#     def deco():
#         pass

@timer  # 相当于 test1 = timer(test1)
def test1():
    time.sleep(3)
    print("in the test1")

@timer   # test2 = timer(test2) => deco   后面调用test2("haoxy")  相当于调用 deco("haoxy")
def test2(name):   # 函数加上参数   test2 = timer(test2) => deco test2() => deco()
    time.sleep(3)
    print("in the test2",name)


#test1 = timer(test1)   # 把内存地址赋值给test1，就取到了内存中的内容，这样就实现了装饰器
test1()   #---> deco()  执行test1的时候执行的是deco内嵌函数
test2("haoxy")