#_*_coding:utf-8_*_
__author__ = 'Alex Li'


configs ={
    'HostID': 1,
    "Server": "192.168.16.56",
    "ServerPort": 8000,
    "urls":{

        'get_configs' :['api/client/config','get'],  #acquire all the services will be monitored
        'service_report': ['api/client/service/report/','post'],

    },
    'RequestTimeout':30,
    'ConfigUpdateInterval': 300, #5 mins as default

}