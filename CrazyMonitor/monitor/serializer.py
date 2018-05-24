#_*_coding:utf-8_*_
__author__ = 'Alex Li'

from monitor import models
import json,time
from django.core.exceptions import  ObjectDoesNotExist

class ClientHandler(object):

    def __init__(self, client_id):
        self.client_id = client_id
        self.client_configs = {
            "services":{}
        }


    def fetch_configs(self):
        try:
            host_obj = models.Host.objects.get(id=self.client_id)
            template_list= list(host_obj.templates.select_related())
            for host_group in host_obj.host_groups.select_related():
                template_list.extend( host_group.templates.select_related() )
            print(template_list)    #[<Template: LInuxGenericServices>, <Template: Database>, <Template: LInuxGenericServices>, <Template: Database>]
            for template in template_list:
                #print(template.services.select_related())

                for service in template.services.select_related(): #loop each service
                    print(service)
                    self.client_configs['services'][service.name] = [service.plugin_name,service.interval]



        except ObjectDoesNotExist:
            pass

        return  self.client_configs

