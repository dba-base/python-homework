__author__ = "xiaoyu hao"

import redis

pool = redis.ConnectionPool(host='192.168.2.110', port=6379)

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)

pipe.set('name', 'alex')
pipe.set('role', 'sb')

pipe.execute()