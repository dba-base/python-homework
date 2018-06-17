from django.shortcuts import render
import os,django,sys
from django.shortcuts import render
from django.shortcuts import HttpResponse
import json

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LuffyMoniter.settings")# project_name 项目名称
# django.setup()
# # Create your views here.
from web.models import Tablespace


def report(request):
    if request.method == "POST":
        tbs_data = request.POST.get('tbs_data')
        data = json.loads(tbs_data)
        print(data)
        print(type(data))

        tbs_obj_li = []
        for tbs_name,tbs_value in data.items():
            print(tbs_name,tbs_value)
            tbs_obj = Tablespace(name=tbs_name, total_size=str(tbs_value[0]), free_size=str(tbs_value[1]), used_size=str(tbs_value[2]))
            tbs_obj_li.append(tbs_obj)
        print("tbs_obj_li:",tbs_obj_li)

        Tablespace.objects.bulk_create(tbs_obj_li)
    else:
        tablespace = Tablespace.objects.all()
        # for row in tablespace:
        #     print(row.name,row.total_size,row.used_size,row.free_size)
        # return HttpResponse("接收成功。。。")
        return render(request, 'report.html', {"tablespace_img":tablespace})
