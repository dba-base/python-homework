#_*_coding:utf-8_*_
import os,sys

import os,sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

import time
import schedule
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
        self.monitored_services = {
            'host': {
                '192.168.2.128':
                    ['root', 'oracle', 22, 'scott', 'tiger', 'PROD', 1521,
                     {'services':
                         {
                             # 'LinuxCPU': ['LinuxCpuPlugin', 30],
                             # 'LinuxLoad': ['LinuxLoadPlugin', 60],
                             # 'LinuxMemory': ['LinuxMemoryPlugin', 9],
                             # 'LinuxFilesystem': ['LinuxFilesystemPlugin', 9],
                             # 'LinuxNetwork': ['LinuxNetworkPlugin', 6]
                         }},
                     {"db_flag": 1},  # 是否是数据库服务器
                     {'ora_services':
                         {
                             'OraTBS': ['OraTBSPlugin', 300],
                             # 'OraDBTime': ['OraDBTimePlugin', 60],
                             # 'OraWaitEvent': ['OraWaitEventPlugin', 9],
                             # 'OraSession': ['OraSessionPlugin', 9],
                         }},
                     {"host_status": 1}]}}

        # request_type = settings.configs['urls']['get_configs'][1]     #get
        # url = "%s/%s" %(settings.configs['urls']['get_configs'][0], settings.configs['HostID'])  #api/client/config/1
        # latest_configs = self.url_request(request_type,url)  #以get方式请求
        # latest_configs = json.loads(latest_configs)
        # self.monitored_services.update(latest_configs)   #放入字典中

    def forever_run(self):
        '''
        start the client program forever
        :return:
        '''
        exit_flag = False
        config_last_update_time = 0
        self.load_latest_configs()  # 获取监控配置信息
        while not exit_flag:

            # start to monitor services
            for ip_k,host_val in self.monitored_services['host'].items():
                host_message = {ip_k:host_val}
                print('正在监控：',host_message)
                if host_val[len(host_val)-1]['host_status'] == 1:  # 判断主机是否可用,1：可用  0：下线
                    for service_name,val in host_val[7]['services'].items():

                        # "services": {'LinuxCPU':['LinuxCpuPlugin',60],'LinuxLoad':['LinuxLoadPlugin',30],'LinuxMemory':['LinuxMemoryPlugin',90],'LinuxNetwork':['LinuxNetworkPlugin',60]}
                        # service_name:LinuxCPU
                        # val: ['LinuxCpuPlugin', 60]
                        if len(val) == 2:             # means it's the first time to monitor
                            host_val[7]['services'][service_name].append(0)
                            #为什么是0， 因为为了保证第一次肯定触发监控这个服务
                        monitor_interval = val[1]   # 监控间隔
                        last_invoke_time = val[2]   # 0
                        if time.time() - last_invoke_time > monitor_interval: #needs to run the plugin
                            host_val[7]['services'][service_name][2]= time.time() #更新此服务最后一次监控的时间
                            # val: ['cpu_plug', 10s,12345],['memory_plug', 5s,23456], ['io_plug', 15s,34567]
                            #start a new thread to call each monitor plugin
                            t = threading.Thread(target=self.os_invoke_plugin,args=(service_name,val,host_message))
                            t.start()
                            print("Going to monitor [%s]" % service_name)

                        else:
                            print("Going to monitor [%s] in [%s] secs" % (service_name,
                                                                            monitor_interval - (time.time()-last_invoke_time)))

                        time.sleep(2)

                    if host_val[8]["db_flag"] == 1:  # 为 1 则为数据库服务器
                        for service_name, val in host_val[9]['ora_services'].items():
                            print("service_name",service_name)
                            print("val",val)
                            if len(val) == 2:             # means it's the first time to monitor
                                host_val[9]['ora_services'][service_name].append(0)
                                #为什么是0， 因为为了保证第一次肯定触发监控这个服务
                            monitor_interval = val[1]   # 监控间隔
                            last_invoke_time = val[2]   # 0
                            if time.time() - last_invoke_time > monitor_interval: #needs to run the plugin
                                host_val[9]['ora_services'][service_name][2]= time.time() #更新此服务最后一次监控的时间
                                # val: ['cpu_plug', 10s,12345],['memory_plug', 5s,23456], ['io_plug', 15s,34567]
                                #start a new thread to call each monitor plugin
                                t = threading.Thread(target=self.ora_invoke_plugin,args=(service_name,val,host_message))
                                t.start()
                                print("Going to monitor [%s]" % service_name)

                            else:
                                print("Going to monitor [%s] in [%s] secs" % (service_name,
                                                                        monitor_interval - (time.time()-last_invoke_time)))
                            time.sleep(2)
                else:
                    print('{%s}主机不可用'%ip_k)
    def os_invoke_plugin(self,service_name,val,host_message):
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
            plugin_callback = func(**host_message)    #执行函数，并把结果放在plugin_callback
            print("\033[0;47;31m--monitor result:%s,%s，%s\033[0m" %(host_message,plugin_name,plugin_callback))

            report_data = {
                'plugin_name':plugin_name,
                'service_name':service_name,
                'data':json.dumps(plugin_callback)
            }   #现对里面的数据进行dump转换成字符串

            request_action = settings.configs['urls']['service_report'][1]  # Post
            request_url = settings.configs['urls']['service_report'][0]     # api/client/service/report/

            # report_data = json.dumps(report_data).encode('utf-8')
            print(report_data)
            print(type(report_data))
            self.url_request(request_action,request_url,params=report_data)
        else:
            print("\033[31;1mCannot find service [%s]'s plugin name [%s] in plugin_api\033[0m"% (service_name,plugin_name ))
        print('--plugin:',val)


    def ora_invoke_plugin(self, service_name, val, host_message):
        '''
        invoke the monitor plugin here, and send the data to monitor server after plugin returned status data each time
        :param service_name: 监控项 LinuxCPU
        :param val: [pulgin_name,monitor_interval,last_run_time]
        :return:
        '''
        plugin_name = val[0]  # api 插件名
        # 反射
        if hasattr(plugin_api, plugin_name):

            func = getattr(plugin_api, plugin_name)
            plugin_callback = func(**host_message)  # 执行函数，并把结果放在plugin_callback
            print("\033[0;47;31m--monitor result:%s,%s，%s\033[0m" % (host_message, plugin_name, plugin_callback))

            report_data = {
                'plugin_name': plugin_name,
                'service_name': service_name,
                'data': json.dumps(plugin_callback)
            }  # 现对里面的数据进行dump转换成字符串

            request_action = settings.configs['urls']['service_report'][1]  # Post
            request_url = settings.configs['urls']['service_report'][0]  # api/client/service/report/

            # report_data = json.dumps(report_data).encode('utf-8')
            print(report_data)
            print(type(report_data))
            self.url_request(request_action, request_url, params=report_data)
        else:
            print("\033[31;1mCannot find service [%s]'s plugin name [%s] in plugin_api\033[0m" % (
            service_name, plugin_name))
        print('--plugin:', val)

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
            print(abs_url,extra_data['params'])
            #把监控的结果以post方式发送给服务端
            try:

                data_encode = urllib.parse.urlencode(extra_data['params']).encode('utf-8')

                # data_encode :
                # report_data = {
                #     'plugin_name': plugin_name,
                #     'service_name': service_name,
                #     'data': json.dumps(plugin_callback)
                # }
                # 把data_encode发送到abs_url
                req = urllib.request.Request(url=abs_url,data=data_encode)
                res_data = urllib.request.urlopen(req,timeout=settings.configs['RequestTimeout'])
                callback = res_data.read()
                #callback = json.loads(callback)
                callback = callback.decode('utf-8')
                print("\033[31;1m[%s]\033[0m" % callback)
                print("\033[31;1m[%s]:[%s]\033[0m response:\n%s" %(action,abs_url,callback))
                return callback
            except Exception as e:
                print('---exec',e)
                exit("\033[31;1m%s\033[0m"%e)




#
if __name__ == "__main__":
    obj = ClientHandle()
    obj.forever_run()

