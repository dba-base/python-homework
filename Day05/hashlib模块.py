__author__ = "xiaoyu hao"

# 用于加密相关的操作，3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法

import hashlib
#
# m = hashlib.md5()
# m.update(b"Hello")
# print(m.hexdigest())
# m.update(b"It's me")
# print(m.hexdigest())
# m.update(b"It's been a long time since we spoken...")
#
m2 = hashlib.md5()
m2.update("HelloIt's me天王盖地虎".encode(encoding="utf-8"))   # 需要进行
print(m2.hexdigest())    #十六进制
#
# s2  = hashlib.sha1()
# s2.update(b"HelloIt's me")
# print(s2.hexdigest())


import hmac

h = hmac.new(b"12345","you are 250你是".encode(encoding="utf-8"))
print(h.digest())      #十进制
print(h.hexdigest())   #十六进制