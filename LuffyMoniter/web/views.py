from django.shortcuts import render
import os,django,sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LuffyMoniter.settings")# project_name 项目名称
django.setup()
# Create your views here.
from web.models import Tablespace
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))
sys.path.append(BASE_DIR)

from client.plugins.oracle.db_info import info_tablespace
tbs_list=info_tablespace()
tbs_obj_li = []
for tbs_li in tbs_list:
    for i in tbs_li:
        tbs_obj = Tablespace(name=i[0], total_size=str(i[1]), free_size=str(i[2]), used_size=str(i[3]))
        tbs_obj_li.append(tbs_obj)
print(tbs_obj_li)

https://www.cnblogs.com/alphajx/p/5097114.html?utm_source=tuicool&utm_medium=referral