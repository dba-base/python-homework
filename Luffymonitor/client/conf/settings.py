#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

# 远端服务器配置
Params = {
    "server": "127.0.0.1",
    "port": 8000,
    'url': '/report/',
    'request_timeout': 30,
}

configs ={
    'HostID': 1,
    "Server": "localhost",
    "ServerPort": 8000,
    "urls":{

        'get_configs' :['api/client/config','get'],  #acquire all the services will be monitored
        'service_report': ['api/client/service/report/','post'],

    },
    'RequestTimeout':30,
    'ConfigUpdateInterval': 30, #5 mins as default

}

# 日志文件配置

PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用于API认证的KEY
KEY = '299095cc-1330-11e5-b06a-a45e60bec08b'
# 用于API认证的请求头
AUTH_KEY_NAME = 'auth-key'

# 数据库采集
db_params = {
    "url":'jdbc:oracle:thin:@%s:%s:%s',
    "user":'scott',
    "password":'tiger',
    "driver":'oracle.jdbc.driver.OracleDriver',
    "jarFile":'D:\\instantclient_11_2\\ojdbc6.jar'
}

# 操作系统的类型

os_type_choices = {'Linux':0,
                   'windows':1,
                   'AIX':2}
