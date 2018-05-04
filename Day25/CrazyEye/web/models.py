from django.db import models

# Create your models here.

class IDC(models.Model):
    """机房位置"""
    name = models.CharField(max_length=64)

class Host(models.Model):
    """储存所有主机"""
    hostname = models.CharField(max_length=64)
    ip_addr = models.GenericIPAddressField(unique=True)
    port = models.PositiveSmallIntegerField(default=22)
    idc = models.ForeignKey("IDC")

    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.ip_addr


class HostGroup(models.Model):
    """主机组"""
    name = models.CharField(max_length=64,unique=True)
    hosts = models.ManyToManyField(Host)
    def __str__(self):
        return self.name


class RemoteUser(models.Model):
    """存储远程用户名密码"""
    username = models.CharField(max_length=64)
    auth_type_choice = ((0,'ssh/password'),(1,'ssh/key'))
    auth_type = models.SmallIntegerField(choices=auth_type_choice,default=0)
    password = models.CharField(max_length=128)

    def __str__(self):
        return "%s(%s)" %(self.username,self.auth_type)

    class Meta:
        unique_together = ('username','auth_type','password')

class UserProfile(models.Model):
    """存储堡垒机账号"""



