from django.shortcuts import render,HttpResponse
import json
import time
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from monitor.serializer import ClientHandler
# Create your views here.


def client_config(request,temp_id):

    config_obj = ClientHandler(temp_id)
    config = config_obj.fetch_host_configs()

    if config:
        return HttpResponse(json.dumps(config))

@csrf_exempt
def service_report(request):
    print("client data:",request.POST)

    if request.method == 'POST':
        #REDIS_OBJ.set("test_alex",'hahaha')
        try:
            print('host=%s, service=%s' %(request.POST.get('plugin_name'),request.POST.get('service_name') ) )
            report_data = json.loads(request.POST['data'])
            #print(data)
            #StatusData_1_memory_latest
            service_name = request.POST.get('service_name')

            config_obj = ClientHandler(service_name,data=report_data)
            report = config_obj.report_data()
            if report == 'OK':
                return HttpResponse('上传成功。。')

        except IndexError as e:
            print('----->err:',e)
            return HttpResponse('上传失败。。')


    return HttpResponse(json.dumps(report_data))


