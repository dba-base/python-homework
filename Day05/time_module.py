__author__ = "xiaoyu hao"

import time

time.time()   #获取时间戳

time.sleep(2)

time.gmtime()  #help(time.gmtime())  时间戳转换成元组，UTC时区
time.gmtime(10)  # 把秒转换成时间 10/3600/24/365 + 1970

x=time.localtime()  #转换成本地时间
print(x.tm_year)  # 取出年值
print(x.tm_yday)  # 一年中的第几天

print(time.mktime(x) )   #转换成时间戳

print(time.strftime("%Y-%m-%d %H:%M:%S",x))   #格式化输出日期 2017-07-21 13:49:59

print(time.strptime("2017-07-21 13:49:59","%Y-%m-%d %H:%M:%S"))
#time.struct_time(tm_year=2017, tm_mon=7, tm_mday=21, tm_hour=13, tm_min=49, tm_sec=59, tm_wday=4, tm_yday=202, tm_isdst=-1)

print(time.asctime(x))  #Fri Jul 21 14:16:43 2017
print(time.ctime(10000)) #传入的是秒

print("------------------------------------------------------------------------------------------------------")
import datetime
print(datetime.datetime.now()) #返回当前的时间
print(datetime.date.fromtimestamp(time.time()) )  # 时间戳直接转成日期格式 2016-08-19
print(datetime.datetime.now() )
print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分

c_time  = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2)) #时间替换



