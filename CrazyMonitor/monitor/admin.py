from django.contrib import admin
from monitor import models
# Register your models here.

class HostAdmin(admin.ModelAdmin):
    list_display =  ('id','name','ip_addr','status')
    filter_horizontal = ('host_groups','templates')


class TemplateAdmin(admin.ModelAdmin):
    filter_horizontal = ('services',)

class ServiceAdmin(admin.ModelAdmin):
    filter_horizontal = ('items',)
    list_display = ('name','interval','plugin_name')
    #list_select_related = ('items',)

admin.site.register(models.Host,HostAdmin)
admin.site.register(models.HostGroup)
admin.site.register(models.Template,TemplateAdmin)
admin.site.register(models.Service,ServiceAdmin)

admin.site.register(models.ServiceIndex)

admin.site.register(models.UserProfile)
