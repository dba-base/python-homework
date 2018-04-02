from django.db import models

# Create your models here.
# class Foo(models.Model):
#     name = models.CharField(max_length=1)

#部门表
class Business(models.Model):
    # id
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32,null=True,default="SA")
    # fk = models.ForeignKey('Foo')

#主机表
class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(protocol="ipv4",db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey(to="Business", to_field='id',on_delete=models.CASCADE)

# 应用类型表
class Application(models.Model):
    name = models.CharField(max_length=32)
    r = models.ManyToManyField("Host")
# 2
# class HostToApp(models.Model):
#     hobj = models.ForeignKey(to='Host',to_field='nid')
#     aobj = models.ForeignKey(to='Application',to_field='id')

# hid: 1~10  aid:1~2

