from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import os,django,sys
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,redirect
from django.shortcuts import HttpResponse
import json

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LuffyMoniter.settings")# project_name 项目名称
# django.setup()
# # Create your views here.
from web.models import Tablespace

@csrf_exempt
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

@csrf_exempt
def tbs_detail(request):
    if request.method == 'GET':
        tbs = request.GET.get('tbs')
        tablespace = Tablespace.objects.filter(name=tbs)
        return render(request,'tbs_detail.html',{"tablespace_img":tablespace})

def modal(request):
    return render(request,'modals1.html')

'''
777	SYSAUX	860.0	41.9375	818.0625
778	UNDOTBS1	130.0	110.625	19.375
779	USERS	63.75	3.4375	60.3125
780	SYSTEM	750.0	10.6875	739.3125
781	JINGLONG	10.0	9.0	1.0
782	DATA1	100.0	32.3125	67.6875
'''