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
            temp_obj = models.Template.objects.get(id = self.args)
            host_obj = temp_obj.host_set.all()    #反向查询
            for host in host_obj:
                host_li =[ host.username,host.password,host.port ]
                service_dict = {'services': {}}
                for service in temp_obj.services.select_related():  # loop each service
                    print(service)
                    service_dict['services'][service.name] = [service.plugin_name, service.interval]
                host_li.append(service_dict)
                self.client_configs["host"][host.ip_addr] = host_li

            print(self.client_configs)

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
        if service_name[0] == 'LinuxFileSystem':
            print("\033[31;1m[%s]\033[0m" %service_name)
            models.Filesystem.objects.create(**report_data)
            print('完成入库')
            return 'OK'

if __name__ == '__main__':
    dict = {'name':'haoxy','age':28}
    client = ClientHandler(data=dict)
    print(client.args,client.data)


