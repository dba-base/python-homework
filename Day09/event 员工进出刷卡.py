#_*_coding:utf-8_*_
__author__ = "xiaoyu hao"
import threading
import time
import random

def door():
    door_open_time_counter = 0
    while True:
        if door_swiping_event.is_set():
            print("\033[32;1mdoor opening....\033[0m")
            door_open_time_counter +=1

        else:
            print("\033[31;1mdoor closed...., swipe to open.\033[0m")
            door_open_time_counter = 0 #清空计时器
            door_swiping_event.wait()  #a client thread can wait for the flag to be set

        if door_open_time_counter > 3:#门开了已经3s了,该关了
            door_swiping_event.clear()

        time.sleep(0.5)


def staff(n):

    print("staff [%s] is comming..." % n )
    while True:
        if door_swiping_event.is_set():
            print("\033[34;1mdoor is opened, passing.....\033[0m")
            break
        else:
            print("staff [%s] sees door got closed, swipping the card....." % n)
            door_swiping_event.set()
            print("after set ",door_swiping_event.set())
        time.sleep(0.5)

door_swiping_event  = threading.Event() #设置事件


door_thread = threading.Thread(target=door,)
door_thread.start()

for i in range(1):
    p = threading.Thread(target=staff,args=(i,))
    time.sleep(random.randrange(3))
    p.start()