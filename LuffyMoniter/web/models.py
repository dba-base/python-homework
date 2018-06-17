from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)

# Create your models here.

class IDC(models.Model):
    '''机房表'''
    name = models.CharField(max_length=64,unique=True,verbose_name='机房')

    def __str__(self):
        return self.name

class Business(models.Model):
    '''应用厂商表'''
    name = models.CharField(max_length=64,unique=True,verbose_name='厂商')

    def __str__(self):
        return self.name

class AppCompany(models.Model):
    """应用厂商表"""
    name = models.CharField(max_length=64, unique=True,verbose_name='业务系统')

    def __str__(self):
        return self.name

class Host(models.Model):
    """主机列表"""
    hostname = models.CharField(max_length=64,verbose_name="主机名")
    instance_name = models.CharField(max_length=64,verbose_name="实例名")
    ip_addr = models.GenericIPAddressField(unique=True,verbose_name="IP地址")
    port = models.PositiveSmallIntegerField(default=22,verbose_name="端口号")
    username = models.CharField(max_length=64,verbose_name="用户名")
    db_username = models.CharField(max_length=64)
    password = models.CharField(max_length=128, blank=True, null=True)
    db_password = models.CharField(max_length=128, blank=True, null=True)
    database_type_choices = ((0, 'oracle 10g'), (1, 'oracle 11g'), (2, 'oracle 12c'), (3, 'mysql'))
    database_type = models.SmallIntegerField(choices=database_type_choices,default=0,verbose_name="数据库类型")
    os_type_choices = ((0,'Linux'),(1,'windows'),(2,'AIX'))
    os_type = models.SmallIntegerField(choices=os_type_choices,default=0,verbose_name="OS类型")
    opatch_version = models.CharField(max_length=64,verbose_name="补丁")
    idc = models.ForeignKey("IDC",on_delete=models.CASCADE,verbose_name="机房")
    business = models.ForeignKey("Business",on_delete=models.CASCADE,verbose_name="业务系统名称")
    appcompany = models.ForeignKey("AppCompany",on_delete=models.CASCADE,verbose_name="厂商")

    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.ip_addr


class Tablespace(models.Model):
    name = models.CharField(max_length=64,blank=True)
    total_size = models.CharField(max_length=64,blank=True)
    free_size = models.CharField(max_length=64,blank=True)
    used_size = models.CharField(max_length=64,blank=True)

    def __str__(self):
        return self.name


