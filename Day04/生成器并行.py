__author__ = "xiaoyu hao"

#http://www.cnblogs.com/alex3714/articles/5765046.html

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

# c = consumer("ChenRonghua")
# c.__next__()
#
# b1= "韭菜馅"
# c.send(b1)
# c.send(b1)
# c.send(b1)
# c.__next__()
# c.__next__()
# c.__next__()

# 参考：http://www.jianshu.com/p/d09778f4e055
def producer(name):
    c = consumer('A')    #只是让函数consumer变成一个生成器
    c2 = consumer('B')
    c.__next__()         #执行next方法才会执行生成器里面的内容,第一次调用时必须先next()或send(None)，否则会报错，
    c.send(None)         #c.__next__()   == c.send(None)
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了1个包子,分两半!")
        c.send(i)
        c2.send(i)

producer("alex")
