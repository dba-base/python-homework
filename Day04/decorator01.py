#  http://egon09.blog.51cto.com/9161406/1836763

import time

#高阶函数 + 嵌套函数 = 装饰器
def timer(func):
    def deco():
        start_time = time.time()
        func()
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

@timer
def test2():
    time.sleep(3)
    print("in the test2")


#test1 = timer(test1)   # 把内存地址赋值给test1，就取到了内存中的内容，这样就实现了装饰器
test1()   #---> deco()  执行test1的时候执行的是deco内嵌函数
test2()