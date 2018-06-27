from django.db import models

# Create your models here.
class ServiceIndex(models.Model):
    '''指标列表'''
    name = models.CharField(max_length=64) #Linux cpu idle
    key =models.CharField(max_length=64,unique=True) #idle
    data_type_choices = (
        ('int',"int"),
        ('float',"float"),
        ('str',"string")
    )
    data_type = models.CharField(u'指标数据类型',max_length=32,choices=data_type_choices,default='int')
    memo = models.CharField(u"备注",max_length=128,blank=True,null=True)

    def __str__(self):
        return "%s.%s" %(self.name,self.key)

class Service(models.Model):
    '''服务列表，一个服务对应多个指标，'''
    name = models.CharField(u'服务名称',max_length=64,unique=True)
    interval = models.IntegerField(u'监控间隔',default=60)
    plugin_name = models.CharField(u'插件名',max_length=64,default='n/a')
    items = models.ManyToManyField('ServiceIndex',verbose_name=u"指标列表",blank=True)
    has_sub_service = models.BooleanField(default=False,help_text=u"如果一个服务还有独立的子服务 ,选择这个,比如 网卡服务有多个独立的子网卡") #如果一个服务还有独立的子服务 ,选择这个,比如 网卡服务有多个独立的子网卡
    memo = models.CharField(u"备注",max_length=128,blank=True,null=True)

    def __str__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(u'模版名称',max_length=64,unique=True)
    services = models.ManyToManyField('Service',verbose_name=u"服务列表")
    #triggers = models.ManyToManyField('Trigger',verbose_name=u"触发器列表",blank=True)
    def __str__(self):
        return self.name