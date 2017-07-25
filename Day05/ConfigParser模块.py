__author__ = "xiaoyu hao"

import configparser

#文件生成
'''
config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
   config.write(configfile)
'''

#读取

config = configparser.ConfigParser()

config.read('example.ini')
print(config.default_section)  # DEFAULT
print(config.sections())       # ['bitbucket.org', 'topsecret.server.com']


print(config['DEFAULT']['compression'])

print('读取某个section下的内容：')

for key in config['topsecret.server.com']:
    print(key,' = ',config.get('topsecret.server.com',key))

print('-------------或者---------------')
topsecret = config['topsecret.server.com']
for i in topsecret:
    print(i)

#追加
'''
import configparser
config = configparser.RawConfigParser()

config.add_section('Section1')
config.set('Section1', 'an_int', '15')
config.set('Section1', 'a_bool', 'true')
config.set('Section1', 'a_float', '3.1415')
config.set('Section1', 'baz', 'fun')
config.set('Section1', 'bar', 'Python')
config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

with open('example.ini', 'a') as configfile:
    config.write(configfile)
'''