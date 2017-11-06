__author__ = "xiaoyu hao"

import threading
import queue,time

def producer():
    while True:
        for i in range(10):
            q.put("骨头 %s" % i)

        print("开始等待所有的骨头被取走...")
        print(q.qsize())
        q.join()
        print("所有的骨头被取完了...")

def consumer(n):
    #while q.qsize() > 0:
    while True:
        print("%s 取到" % n, q.get())
        time.sleep(1)
        q.task_done()  # 告知这个任务执行完了

q = queue.Queue()

p = threading.Thread(target=producer, )
p.start()

c1 = threading.Thread(target=consumer,args=("alex",))
#c1 = consumer("李闯")
c1.start()