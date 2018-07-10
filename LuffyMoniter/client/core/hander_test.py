# _*_coding:utf-8_*_
# import os,sys
# pathname = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, pathname)
# sys.path.insert(0, os.path.abspath(os.path.join(pathname, '..')))
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LuffyMoniter.settings")  # 在Django 里想单独执行文件写上这句话
# import django  # 导入Django
# django.setup()  # 执行

# from web import models
# import json, time
# from django.core.exceptions import ObjectDoesNotExist

#
#
# class ClientHandler(object):
#
#     def report_data(self):
#         service_name = ('LinuxFileSystem',)
#
#         report_data = {'ip': '192.168.2.128',
#              '/': ['26718', '25056', '306'],
#              '/dev/shm': ['431', '1', '431'],
#              '/boot': ['485', '40', '421'],
#              'time': '2018-07-05 16:42',
#              'status': 0}
#         if service_name[0] == 'LinuxFileSystem':
#             print("\033[31;1m[%s]\033[0m" %service_name)
#             fs_obj_li = []
#             #取得字典的子集
#             fs_dict =  {key: value for key, value in report_data.items() if key not in {'ip','time','status'}}
#             for fs_name,fs_size in fs_dict.items():
#                 dict = {
#                     "ip":report_data['ip'],
#                     "mount_point": fs_name,
#                     "Total_size": fs_size[0],
#                     "used_size": fs_size[1],
#                     "avail_size": fs_size[2],
#                     "time":report_data['time'],
#                     "status":report_data['status']
#                 }
#                 print(dict)
#                 fs_obj = models.Filesystem(**dict)
#                 fs_obj_li.append(fs_obj)
#             models.Filesystem.objects.bulk_create(fs_obj_li)
#             print('完成入库')
#             return 'OK'
#
# if __name__ == '__main__':
#     client = ClientHandler()
#     client.report_data()


import datetime
import schedule
import threading
import time


def job1():
    print("I'm working for job1")
    time.sleep(2)
    print("job1:", datetime.datetime.now())


def job2():
    print("I'm working for job2")
    time.sleep(2)
    print("job2:", datetime.datetime.now())


def job1_task():
    threading.Thread(target=job1).start()


def job2_task():
    threading.Thread(target=job2).start()


def run():
    schedule.every(5).seconds.do(job1_task)
    schedule.every(10).seconds.do(job2_task)

    while True:
        schedule.run_pending()
        time.sleep(1)

run()