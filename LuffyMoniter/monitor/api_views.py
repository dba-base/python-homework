from django.shortcuts import render,HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from monitor.serializer import ClientHandler
# Create your views here.


def client_config(request,client_id):

    config_obj = ClientHandler(client_id)
    config = config_obj.fetch_configs()

    if config:
        return HttpResponse(json.dumps(config))

@csrf_exempt
def service_report(request):
    print("client data:",request.POST)

    if request.method == 'POST':
        #REDIS_OBJ.set("test_alex",'hahaha')
        try:
            print('host=%s, service=%s' %(request.POST.get('client_id'),request.POST.get('service_name') ) )
            data =  json.loads(request.POST['data'])
            #print(data)
            #StatusData_1_memory_latest
            client_id = request.POST.get('client_id')
            service_name = request.POST.get('service_name')
            #把数据存下来
            data_saveing_obj = data_optimization.DataStore(client_id,service_name,data,REDIS_OBJ)

            #redis_key_format = "StatusData_%s_%s_latest" %(client_id,service_name)
            #data['report_time'] = time.time()
            #REDIS_OBJ.lpush(redis_key_format,json.dumps(data))


        except IndexError as e:
            print('----->err:',e)


    return HttpResponse(json.dumps(data))


