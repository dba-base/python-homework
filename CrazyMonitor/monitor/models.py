from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Host(models.Model):
    '''主机信息'''
    name =  models.CharField(max_length=64,unique=True)
    ip_addr =  models.GenericIPAddressField(unique=True)
    host_groups = models.ManyToManyField('HostGroup',blank=True) # A B C
    templates = models.ManyToManyField("Template",blank=True) # A D E
    monitored_by_choices = (
        ('agent','Agent'),
        ('snmp','SNMP'),
        ('wget','WGET'),
    )
    monitored_by = models.CharField(u'监控方式',max_length=64,choices=monitored_by_choices)
    status_choices= (
        (1,'Online'),
        (2,'Down'),
        (3,'Unreachable'),
        (5,'Problem'),
    )
    host_alive_check_interval = models.IntegerField(u"主机存活状态检测间隔", default=30)
    status = models.IntegerField(u'状态',choices=status_choices,default=1)
    memo = models.TextField(u"备注",blank=True,null=True)

    def __str__(self):
        return self.name

class HostGroup(models.Model):
    '''主机组'''
    name = models.CharField(max_length=64,unique=True)
    templates = models.ManyToManyField("Template",blank=True)
    memo = models.TextField(u"备注",blank=True,null=True)

    def __str__(self):
        return self.name

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


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=64,blank=True,null=True)


    def __str__(self):
        return self.name