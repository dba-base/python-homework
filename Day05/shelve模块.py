__author__ = "xiaoyu hao"

import shelve
import datetime

#shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式

d = shelve.open('shelve_test')  # 打开一个文件

'''
写入文件，生成三个文件（shelve_test.bak,shelve_test.dat,shelve_test.dir）

info = {'age':22,"job":'it'}

name = ["alex", "rain", "test"]
d["name"] = name  # 持久化列表
d["info"] = info  # 持久dict
d['date'] = datetime.datetime.now()
d.close()
'''

#读取
print(d.get('name'))
print(d.get('info'))
print(d.get('date'))

'''
输出：
['alex', 'rain', 'test']
{'age': 22, 'job': 'it'}
2017-07-24 16:19:49.249094
'''