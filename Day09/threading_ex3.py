__author__ = "xiaoyu hao"

__author__ = "xiaoyu hao"

import threading
import time

def run(n):
    print("task:",n,threading.current_thread())
    time.sleep(2)

# #并发
# t1 = threading.Thread(target=run,args=("t1",))
# t2 = threading.Thread(target=run,args=("t2",))
# t1.start()
# t2.start()
start_time = time.time()
t_objs = []  #存储线程实例
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s"%i,))
    t.setDaemon(True)  #把当前线程设置为守护线程，主线程结束，子线程也结束
    t.start()
    t_objs.append(t)  #

# for t in t_objs:
#     t.join()

print("-----------all threads has finished....",threading.current_thread())   #主进程执行
print("cost:",time.time() - start_time)
