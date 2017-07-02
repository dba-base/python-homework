# -*- coding:utf-8 -*-

import sys
# python 2.x
'''
s = "你好"

s_to_gbk = s.decode("uft-8").encode("gbk")

'''

#encode 编码   decode 解码

print(sys.getdefaultencoding())

s = "你好"  #文件编码为utf-8 s为默认编码：Unicode，可直接转换成任意的编码格式，无需进行decode

#转换成gbk
s_to_gbk = s.encode("gbk")
print(s_to_gbk)

#转换成 utf-8
s_to_uft8 = s.encode("utf-8")
print(s_to_uft8)

# s.encode("gbk") -- GBK  s.encode("gbk").decode("gbk")  -- GBK 转换成unicode
# s.encode("gbk").decode("gbk").encode("gb2312")  - unicode 转换成  gb2312
print(s.encode("gbk").decode("gbk").encode("gb2312").decode("gb2312"))