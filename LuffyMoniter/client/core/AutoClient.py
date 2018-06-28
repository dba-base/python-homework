#_*_coding:utf-8_*_
import time
from conf import settings
import urllib
import urllib.request
from urllib.error import URLError
import json
import threading
from core.plugins import plugin_api

class ClientHandle(object):
    def __init__(self):
        self.monitored_services = {}

    def load_latest_configs(self):
        '''
        load the latest monitor configs from monitor server
        :return:
        '''
        # request_type = settings.configs['urls']['get_configs'][1]     #get
        # url = "%s/%s" %(settings.configs['urls']['get_configs'][0], settings.configs['HostID'])  #api/client/config/1
        # latest_configs = self.url_request(request_type,url)  #以get方式请求
        # latest_configs = json.loads(latest_configs)
        # self.monitored_services.update(latest_configs)   #放入字典中
        self.monitored_services = {'services':
                                       {'LinuxCPU':
                                            ['LinuxCpuPlugin',60],
                                        'LinuxLoad':
                                            ['LinuxLoadPlugin',30],
                                        'LinuxMemory':
                                            ['LinuxMemoryPlugin',90],
                                        'LinuxNetwork':
                                            ['LinuxNetworkPlugin',60]
                                        },
                                   'host':{'192.168.2.128':['root','oracle']}
                                   }

    def forever_run(self):
        '''
        start the client program forever
        :return:
        '''
        exit_flag = False
        config_last_update_time = 0

        while not exit_flag:
              if time.time() - config_last_update_time > settings.configs['ConfigUpdateInterval']:
                  self.load_latest_configs()    # 获取最新的监控配置信息
                  print("Loaded latest config:", self.monitored_services)
                  config_last_update_time = time.time()
              #start to monitor services

              for service_name,val in self.monitored_services['services'].items():

                  # "services": {'LinuxCPU':['LinuxCpuPlugin',60],'LinuxLoad':['LinuxLoadPlugin',30],'LinuxMemory':['LinuxMemoryPlugin',90],'LinuxNetwork':['LinuxNetworkPlugin',60]}
                  # service_name:LinuxCPU
                  # val: ['LinuxCpuPlugin', 60]

                  if len(val) == 2:             # means it's the first time to monitor
                      self.monitored_services['services'][service_name].append(0)
                      #为什么是0， 因为为了保证第一次肯定触发监控这个服务
                  monitor_interval = val[1]   # 监控间隔
                  last_invoke_time = val[2]   # 0
                  if time.time() - last_invoke_time > monitor_interval: #needs to run the plugin
                      print(last_invoke_time,time.time())
                      self.monitored_services['services'][service_name][2]= time.time() #更新此服务最后一次监控的时间
                      # val: ['cpu_plug', 10s,12345],['memory_plug', 5s,23456], ['io_plug', 15s,34567]
                      #start a new thread to call each monitor plugin
                      t = threading.Thread(target=self.invoke_plugin,args=(service_name,val))
                      t.start()
                      print("Going to monitor [%s]" % service_name)

                  else:
                      print("Going to monitor [%s] in [%s] secs" % (service_name,
                                                                    monitor_interval - (time.time()-last_invoke_time)))

              time.sleep(1)

    def invoke_plugin(self,service_name,val):
        '''
        invoke the monitor plugin here, and send the data to monitor server after plugin returned status data each time
        :param service_name: 监控项 LinuxCPU
        :param val: [pulgin_name,monitor_interval,last_run_time]
        :return:
        '''
        plugin_name = val[0]    #api 插件名
        # 反射
        if hasattr(plugin_api,plugin_name):
            func = getattr(plugin_api,plugin_name)
            plugin_callback = func()    #执行函数，并把结果放在plugin_callback
            print("--monitor result:",plugin_callback)
            print(type(plugin_callback))

            # report_data = {
            #     'client_id':settings.configs['HostID'],
            #     'service_name':service_name,
            #     'data':json.dumps(plugin_callback)
            # }
            #
            # request_action = settings.configs['urls']['service_report'][1]  # Post
            # request_url = settings.configs['urls']['service_report'][0]     # api/client/service/report/
            #
            # #report_data = json.dumps(report_data)
            # print('---report data:',report_data)
            # self.url_request(request_action,request_url,params=report_data)
        else:
            print("\033[31;1mCannot find service [%s]'s plugin name [%s] in plugin_api\033[0m"% (service_name,plugin_name ))
        print('--plugin:',val)


    def url_request(self,action,url,**extra_data):
        '''
        cope with monitor server by url
        :param action: "get" or "post"
        :param url: witch url you want to request from the monitor server
        :param extra_data: extra parameters needed to be submited
        :return: 返回网站的全部数据
        '''

        #http://192.168.16.56/8000/api/client/config/1
        #http://192.168.16.56/8000/api/client/service/report/
        abs_url = "http://%s:%s/%s" % (settings.configs['Server'],
                                       settings.configs["ServerPort"],
                                       url)
        if action in  ('get','GET'):
            print(abs_url,extra_data)
            try:
                req = urllib.request.Request(abs_url)
                req_data = urllib.request.urlopen(req,timeout=settings.configs['RequestTimeout'])  #打开一个网站
                callback = req_data.read()   #读取网站全部内容
                #print "-->server response:",callback
                return callback
            except URLError as e:
                exit("\033[31;1m%s\033[0m"%e)

        elif action in ('post','POST'):
            #print(abs_url,extra_data['params'])
            #把监控的结果以post方式发送给服务端
            try:
                data_encode = urllib.urlencode(extra_data['params'])

                # data_encode :
                # report_data = {
                #     'client_id': settings.configs['HostID'],
                #     'service_name': service_name,
                #     'data': json.dumps(plugin_callback)
                # }
                # 把data_encode发送到abs_url
                req = urllib.request.Request(url=abs_url,data=data_encode)
                res_data = urllib.request.urlopen(req,timeout=settings.configs['RequestTimeout'])
                callback = res_data.read()
                callback = json.loads(callback)
                print("\033[31;1m[%s]:[%s]\033[0m response:\n%s" %(action,abs_url,callback))
                return callback
            except Exception as e:
                print('---exec',e)
                exit("\033[31;1m%s\033[0m"%e)
