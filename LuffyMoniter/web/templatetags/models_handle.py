__author__ = "xiaoyu hao"

from django import template
from django.utils.safestring import mark_safe
from web import models

register = template.Library()

@register.simple_tag
def tablespace_part():
    tablespace = models.Tablespace.objects.filter(time='15:47:32.310310')
    tablespace_li = []
    for tbs in tablespace:
        tbs_z = [tbs.name,tbs.total_size,tbs.free_size,tbs.used_size,tbs.host_id,tbs.host.ip_addr]
        tablespace_li.append(tbs_z)
    print(tablespace_li)
    return mark_safe(tablespace_li)