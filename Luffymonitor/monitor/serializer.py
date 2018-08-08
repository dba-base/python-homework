__author__ = "xiaoyu hao"
# _*_coding:utf-8_*_
# import os,sys
# pathname = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, pathname)
# sys.path.insert(0, os.path.abspath(os.path.join(pathname, '..')))
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LuffyMoniter.settings")  # 在Django 里想单独执行文件写上这句话
# import django  # 导入Django
# django.setup()  # 执行

from web import models
import json, time
from django.core.exceptions import ObjectDoesNotExist



class ClientHandler(object):
    def __init__(self,*args,**kwargs):
        self.args = args
        self.data = kwargs
        self.client_configs = {
            "host":{}
        }


    # 根据模板ID获取主机列表和服务列表
    def fetch_host_configs(self):
        try:
            host_obj = models.Host.objects.all()
            for host in host_obj:
                is_enable = host.enabled
                if is_enable:
                    host_li = [host.username, host.password, host.port,host.db_username,host.db_password,host.instance_name,host.db_port]
                    service_dict = {'services': {}}
                    for temps in host.templates.select_related():
                        for service in temps.services.select_related():
                            print(service)
                            service_dict['services'][service.name] = [service.plugin_name, service.interval]
                    host_li.append(service_dict)
                    self.client_configs["host"][host.ip_addr] = host_li
        except ObjectDoesNotExist:
            pass

        return self.client_configs

    def report_data(self):
        service_name = self.args
        report_data = self.data['data']
        print('%s,%s' %(service_name,report_data))
        if service_name[0] == 'LinuxCPU':
            print("\033[31;1m[%s]\033[0m" %service_name)
            models.CpuInfo.objects.create(**report_data)
            print('完成入库')
            return 'OK'
        if service_name[0] == 'LinuxMemory':
            print("\033[31;1m[%s]\033[0m" %service_name)
            models.MemInfo.objects.create(**report_data)
            print('完成入库')
            return 'OK'
        if service_name[0] == 'LinuxLoad':
            print("\033[31;1m[%s]\033[0m" %service_name)
            models.LoadInfo.objects.create(**report_data)
            print('完成入库')
            return 'OK'
        if service_name[0] == 'LinuxNetwork':
            print("\033[31;1m[%s]\033[0m" %service_name)
            models.CpuInfo.objects.create(**report_data)
            print('完成入库')
            return 'OK'
        if service_name[0] == 'LinuxFilesystem':
            print("\033[31;1m[%s]\033[0m" %service_name)
            fs_obj_li = []
            #取得字典的子集
            fs_dict =  {key: value for key, value in report_data.items() if key not in {'ip','time','status'}}
            for fs_name,fs_size in fs_dict.items():
                dict = {
                    "ip":report_data['ip'],
                    "mount_point": fs_name,
                    "Total_size": fs_size[0],
                    "used_size": fs_size[1],
                    "avail_size": fs_size[2],
                    "time":report_data['time'],
                    "status":report_data['status']
                }
                print(dict)
                fs_obj = models.Filesystem(**dict)
                fs_obj_li.append(fs_obj)
            models.Filesystem.objects.bulk_create(fs_obj_li)
            print('完成入库')
            return 'OK'
        if service_name[0] == 'OraTBS':
            tbs_obj_li = []
            fs_dict = {key: value for key, value in report_data.items() if key not in {'ip', 'time', 'status'}}
            for tbs_name, tbs_size in fs_dict.items():
                host = models.Host.objects.get(ip_addr=report_data['ip'])
                dict = {
                    "name": tbs_name,
                    "total_size": tbs_size[0],
                    "free_size": tbs_size[1],
                    "used_size": tbs_size[2],
                    "time": report_data['time'],
                    "host": host
                }
                print(dict)
                tbs_obj = models.Tablespace(**dict)
                tbs_obj_li.append(tbs_obj)
            print("tbs_obj_li:", tbs_obj_li)
            print("\033[31;1m[%s]\033[0m" % service_name)
            models.Tablespace.objects.bulk_create(tbs_obj_li)
            # for row in tablespace:
            #     print(row.name,row.total_size,row.used_size,row.free_size)
            print('完成入库')
            return 'OK'
        if service_name[0] == 'hostinfo':
            print("\033[31;1mreport_data:[%s]\033[0m" %report_data)
            print("host_li:",report_data)
            for host in report_data:
                print("host------",host)
                models.Host.objects.filter(ip_addr=host["ip_addr"]).update(**host)

# if __name__ == '__main__':
#     dict = {'name':'haoxy','age':28}
#     client = ClientHandler(data=dict)
#     print(client.args,client.data)


