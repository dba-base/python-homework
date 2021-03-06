from django.views.decorators.csrf import csrf_exempt,csrf_protect
import os,django,sys
from django.utils.timezone import now, timedelta
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,redirect
from django.shortcuts import HttpResponse
import json

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LuffyMoniter.settings")# project_name 项目名称
# django.setup()
# # Create your views here.
from web.models import Tablespace
from web import models

@csrf_exempt
def index(request):
    return render(request,'index.html',)

@csrf_exempt
def monitor_items(request):
    hosts = models.Host.objects.all()
    business = models.Business.objects.all()
    return render(request,'monitor_items.html',locals())

@csrf_exempt
def db_list(request):
    return render(request,'monitor_items.html',)

@csrf_exempt
def tablespace(request):
    tablespace = Tablespace.objects.filter(time='15:47:32.310310')
    hosts = tablespace.values('host_id').distinct()
    print(tablespace)
    return render(request,'tablespace.html',{"tablespace_img":tablespace,"hosts":hosts})

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
        # for row in tablespace:
        #     print(row.name,row.total_size,row.used_size,row.free_size)
        return HttpResponse("接收成功。。。")
    else:
        #获取今天的表空间数据
        tablespace = Tablespace.objects.filter(date=now().date()+timedelta(days=-2))
        return render(request, 'report.html', {"tablespace_img":tablespace})

@csrf_exempt
def tbs_detail(request):
    '''
    取得表空间详细数据，可以获取到7天之内的数据
    :param request:
    :return:
    '''
    if request.method == 'GET':
        tbs = request.GET.get('tbs')
        today_date = now().date()
        date_1 = now().date() + timedelta(days=-7)   #取得7天前的日期
        tablespace = Tablespace.objects.filter(name=tbs,date__gt=date_1).order_by('-date')  #降序
        today_tbs = Tablespace.objects.filter(name=tbs,date=today_date)  #降序
        today_tbs_dict = {}
        for today_detail in today_tbs:
            today_tbs_dict['tbs_name'] = today_detail.name
            today_tbs_dict['total_size'] = today_detail.total_size
            today_tbs_dict['used_size'] = today_detail.used_size
            today_tbs_dict['free_size'] = today_detail.free_size

        today_tbs_data = json.dumps(today_tbs_dict)


        return render(request,'tbs_detail.html',{"tablespace_img":tablespace,"today_data":today_tbs_data})

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