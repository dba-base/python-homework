# __author__ = "xiaoyu hao"
#
# __author__ = "xiaoyu hao"
#
import sys,time
import os
# def __progress(trans_size, file_size, mode):
#     '''
#     进度条方法
#     :param trans_size: 已传输得数据大小(字节)
#     :param file_size: 文件的总大小（字节）
#     :param mode: 传输方式
#     :return:
#     '''
#     UNIT_SIZE = 1048576
#     bar_lengh = 100  # 进度条的长度
#     percent = float(trans_size) / float(file_size)  # 已经传输的大小百分比
#     hashes = '=' * int(percent * bar_lengh)  # 进度条显示的数量
#     spaces = ' ' * (bar_lengh - len(hashes))  # 剩余部分通过空格补充，空格数量 = 总长度 - “=”显示的长度
#     sys.stdout.write(
#         "\r%s:%.2fM/%.2fM %d%% [%s]" %(
#         mode, trans_size / UNIT_SIZE, file_size / UNIT_SIZE, percent * 100, hashes + spaces))
#     sys.stdout.flush()
#
# trans_size = 0
# while trans_size < 11:
#     __progress(trans_size,10, "下载中")
#     time.sleep(1)
#     trans_size += 1

#str = "get C:/progrem/test.mp4"
'''
str = "get test.mp4"
cmd = str.split()[0]
filename = str.split()[1]

print(cmd)
print(filename)

a = os.path.basename(filename)
print(a)

'''

import platform
print(platform.architecture())
print(platform.platform())
print(platform.system())
print(platform.python_version())
def UsePlatform():
  sysstr = platform.system()
  if(sysstr =="Windows"):
    print ("Call Windows tasks")
  elif(sysstr == "Linux"):
    print ("Call Linux tasks")
  elif(sysstr == "Darwin"):   #苹果mac操作系统
    print("Call MACOS tasks")
  else:
    print ("Other System tasks")

UsePlatform()



