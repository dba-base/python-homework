from django.contrib import admin

import web

class HostAdmin(admin.ModelAdmin):
        list_display = ['id','idc','business','appcompany','hostname','ip_addr','port','instance_name','database_type','os_type','enabled']
        filter_horizontal = ('templates',)

class TbsAdmin(admin.ModelAdmin):
        list_display = ['name','total_size','used_size','free_size','date','time','host']


class ServiceAdmin(admin.ModelAdmin):
        list_display = ['name', 'interval', 'plugin_name',]
        filter_horizontal = ('items',)

class TemplateAdmin(admin.ModelAdmin):
        list_display = ['name',]
        filter_horizontal = ('services',)


class ServiceIndexAdmin(admin.ModelAdmin):
        list_display = ['name', 'key', 'data_type', 'memo']


# 注册模型到admin中，让admin管理models
admin.site.register(web.models.Host,HostAdmin)
admin.site.register(web.models.Business)
admin.site.register(web.models.AppCompany)
admin.site.register(web.models.IDC)
admin.site.register(web.models.Tablespace,TbsAdmin)
admin.site.register(web.models.ServiceIndex,ServiceIndexAdmin)
admin.site.register(web.models.Service,ServiceAdmin)
admin.site.register(web.models.Template,TemplateAdmin)
