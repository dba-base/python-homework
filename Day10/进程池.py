__author__ = "xiaoyu hao"

from  multiprocessing import Process, Pool
import time,os

def Foo(i):
    time.sleep(2)
    print("in process:",os.getpid())
    return i + 100

def Bar(arg):
    print('-->exec done:', arg,os.getpid())

if __name__ == '__main__':
    pool = Pool(5)   #允许进程池有5个进程同时运行
    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)  #并行，callback回调,执行完Foo后再执行Bar,主进程调用
        # pool.apply(func=Foo, args=(i,))  #串行

    print('end')
    pool.close()    #先close再join
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。