#Author: xiaoyu hao

import sys

print(sys.path)

print(sys.argv)   #打印参数

#ptyhon sys_os_mod.py 1 2 3 4
#输出：['C:/Users/xiaoyu/PycharmProjects/c14/Day2/sys_os_mod.py',1,2,3,4]
#下面会输出2
#print(sys.argv[2])

import os

#cmd_dir = os.system("dir")  #执行命令，但不保存结果

cmd_dir = os.popen("dir").read()  # popen 执行命令，并把结果放在内存里，通过read()把结果读出来
print("----> ",cmd_dir)

#创建目录
#os.mkdir("作业")   #在当前目录下创建一个目录


a=60<<2
d=-60<<2
b=60>>2
c=-60>>2

print("60<<2,左移<<:",a)
print("-60<<2,左移<<:",d)
print("60>>2,右移>>:",b)
print("-60>>2,右移:",c)


