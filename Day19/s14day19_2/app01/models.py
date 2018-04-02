from django.db import models

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = '用户类型'
        verbose_name_plural = '用户类型'

class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32,unique=True)
    ctime = models.DateTimeField(auto_now_add=True,null=True)
    uptime = models.DateTimeField(auto_now=True, null=True)

class UserInfo(models.Model):
    # id列，自增，主键
    # 用户名列，字符串类型，指定长度
    # 字符串、数字、时间、二进制
    username = models.CharField(max_length=32,blank=True,verbose_name='用户名')
    password = models.CharField(max_length=60, help_text='pwd')
    email = models.CharField(max_length=60)
    test = models.EmailField(max_length=19,null=True,error_messages={'invalid': '请输入密码'})
    # user_group_id 数字
    user_group = models.ForeignKey("UserGroup",to_field='uid', on_delete=models.CASCADE) # (uid,catption,ctime,uptimew)
    user_type_choices = (
        (1, '超级用户'),
        (2, '普通用户'),
        (3, '普普通用户'),
    )
    user_type_id = models.IntegerField(choices=user_type_choices,default=1)
