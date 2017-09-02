
2.例：
import time

#内嵌了一个函数deco
def timer(func):
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func runtime is %s" %(stop_time - start_time))
    return deco   #返回deco的内存地址

def test1():
    time.sleep(3)
    print("in the test1")

test1 = timer(test1)  # deco的内存地址
test1()