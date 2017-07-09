#f本身是要传入一个函数

# 1. 把一个函数名当作实参传递给另外一个函数
# 2. 返回值中包含函数名

'''
def fun(a,b,f):
    return f(a) + f(b)

result = fun(-1,3,abs)
print(result)
'''

import time

def bar():
    time.sleep(3)
    print("in the bar ")


def fun1(func):   # 传入的参数为函数名
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the func runtime is %s" %(stop_time - start_time))

def fun2(func):
    print(func)
    return func

fun1(bar)
t = fun2(bar())
t()
