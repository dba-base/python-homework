__author__ = "xiaoyu hao"

import os,sys
pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, pathname)
sys.path.insert(0, os.path.abspath(os.path.join(pathname, '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LuffyMoniter.settings")  # 在Django 里想单独执行文件写上这句话
import django  # 导入Django
django.setup()  # 执行

from web import models
report_data={'ip': '192.168.2.128', 'SYSAUX': (900.0, 46.5625, 853.4375), 'UNDOTBS1': (130.0, 112.125, 17.875), 'USERS': (63.75, 3.3125, 60.4375), 'SYSTEM': (750.0, 10.5625, 739.4375), 'JINGLONG': (10.0, 9.0, 1.0), 'DATA1': (100.0, 32.3125, 67.6875), 'time': '2018-07-10 15:09'}
tbs_obj_li = []
fs_dict = {key: value for key, value in report_data.items() if key not in {'ip', 'time', 'status'}}
print(fs_dict)
for tbs_name, tbs_size in fs_dict.items():
    print("ip:",report_data['ip'])
    host_obj = models.Host.objects.get(ip_addr=report_data['ip'])
    print(host_obj)
    dict = {
        "name": tbs_name,
        "total_size": tbs_size[0],
        "free_size": tbs_size[1],
        "used_size": tbs_size[2],
        "time": report_data['time'],
        "host": host_obj
    }
    print(dict)
    tbs_obj = models.Tablespace(**dict)
    tbs_obj_li.append(tbs_obj)
print("tbs_obj_li:", tbs_obj_li)
models.Tablespace.objects.bulk_create(tbs_obj_li)
# for row in tablespace:
#     print(row.name,row.total_size,row.used_size,row.free_size)
print('完成入库')
