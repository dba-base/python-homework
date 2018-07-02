__author__ = "xiaoyu hao"
# _*_coding:utf-8_*_
from web import models
import json, time
from django.core.exceptions import ObjectDoesNotExist


class ClientHandler(object):
    def __init__(self):
        self.client_configs = {
            "services": {},
            "host":{}
        }

    def fetch_configs(self):
        try:
            host_obj = models.Host.objects.all()
            host_list = []
            for host in host_obj:
                host_dict ={host.ip_addr:[ host.username,host.password,host.port ]}
            template_list = list(host_obj.templates.select_related())
            for host_group in host_obj.select_related():
                template_list.extend(host_group.templates.select_related())
            print(template_list)
            # [<Template: LInuxGenericServices>, <Template: Database>, <Template: LInuxGenericServices>, <Template: Database>]
            for template in template_list:
                # print(template.services.select_related())

                for service in template.services.select_related():  # loop each service
                    print(service)
                    self.client_configs['services'][service.name] = [service.plugin_name, service.interval]
                    #	{
                    #				"services":{cpu:['cpu_plug',10s,0],memory:['memory_plug',10s],io:['io_plug',10s]}
                    #			}


        except ObjectDoesNotExist:
            pass

        return self.client_configs

