from django.contrib import admin

from web import models
from web.models import Host
from web.models import Business
from web.models import AppCompany
from web.models import IDC
# Register your models here.


class HostAdmin(admin.ModelAdmin):
        list_display = ['id','idc','business','appcompany','hostname','ip_addr','port','instance_name','database_type','os_type','enabled']


# 注册模型到admin中，让admin管理models
admin.site.register(models.Host,HostAdmin)
admin.site.register(models.Business)
admin.site.register(models.AppCompany)
admin.site.register(models.IDC)
