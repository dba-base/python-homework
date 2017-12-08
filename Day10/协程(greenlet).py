__author__ = "xiaoyu hao"

#安装geven包
from greenlet import greenlet


def foo1():
    print(12)
    gr2.switch() #切换到foo2
    print(34)
    gr2.switch()


def foo2():
    print(56)
    gr1.switch()  #切换到foo1
    print(78)


gr1 = greenlet(foo1)  #启动一个协程
gr2 = greenlet(foo2)
gr1.switch()

