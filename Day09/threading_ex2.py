<<<<<<< HEAD
__author__ = "xiaoyu hao"
=======
__author__ = "Alex Li"

'''
继承式调用
'''
>>>>>>> 4395f80d72236fb740714254855a34a72a8cf664

import threading
import time

class MyThread(threading.Thread):
<<<<<<< HEAD
    def __init__(self,n):
        super(MyThread, self).__init__()
        self.n = n

    def run(self):
        print("running task",self.n)
        time.sleep(2)

t1 = MyThread("t1")
t2 = MyThread("t2")

t1.start()
t1.join()  #等待t1执行完成
t2.start()
=======
    def __init__(self,n,sleep_time):
        super(MyThread,self).__init__()
        self.n =  n
        self.sleep_time = sleep_time
    def run(self):
        print("runnint task ",self.n )
        time.sleep(self.sleep_time)
        print("task done,",self.n )


t1 = MyThread("t1",2)
t2 = MyThread("t2",4)

t1.start()
t2.start()

t1.join() #=wait()
t2.join()

print("main thread....")
>>>>>>> 4395f80d72236fb740714254855a34a72a8cf664
