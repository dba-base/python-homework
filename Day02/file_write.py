__author__ = "xiaoyu hao"


# 以w模式打开文件实际是创建一个文件，会覆盖掉已有的文件

#f = open("yesterday2",'w',encoding="utf-8")
f = open("yesterday2",'a',encoding="utf-8")

f.write("我爱北京天安门,,,,,,,\n")   #\n 换行
f.write("天安门上太阳升,\n")



