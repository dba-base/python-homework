__author__ = "xiaoyu hao"


#进程之间共享数据
from multiprocessing import Process, Manager
import os

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(os.getpid())
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()   #生成一个可在多个进程间共享和传递的字典

        l = manager.list(range(5)) #生成一个可在多个进程间共享和传递的列表
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:  #等待所有的进程结束
            res.join()

        print(d)
        print(l)