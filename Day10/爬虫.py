__author__ = "xiaoyu hao"

from gevent import monkey;
monkey.patch_all()  #把当前程序的所有IO操作单独的作上标记，捕捉urllib的IO操作

import gevent
from  urllib.request import urlopen
import time

def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

urls =['https://www.python.org/','https://www.yahoo.com/','https://github.com/']
time_stat = time.time()

#不适用协程
for url in urls:
    f(url)

print("同步cost:",time.time() - time_stat)

async_stat_time = time.time()

#适用协程
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])

print("异步cost:",time.time() - async_stat_time)