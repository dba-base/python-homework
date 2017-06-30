__author__ = "xiaoyu hao"

'''
#data = open("yesterday",encoding="utf-8").read()

#f 是个文件句柄（字符集，内容，，，，），通过f来操作文件，
f = open("yesterday",'r',encoding="utf-8")
data = f.read()
data2 = f.read()

print(data)

#没打印任何内容，第一次读完后，光标会移到最后一行
print("-------------data2-----:",data2)



f = open("yesterday",'r',encoding="utf-8")


#读取前几行
for i in range(5):
    print(f.readline())

print("------------readlines()---------------")
for line in f.readlines():
    print(line.strip())


print("---------打印10行，不打印第10行-------")

#不推荐
for index,line in enumerate(f.readlines()):
    if index == 9:
        print("----------我是分割线---------")
        continue
    print(line.strip())

'''

''''
f = open("yesterday",'r',encoding="utf-8")

#high bige，推荐
#一行一行的读，不占内存
count = 0
for line in f:
    if count == 9:
        print("----------我是分割线---------")
        break
    print(line)
    count +=1
f.close()
'''

'''
f = open("yesterday",'r',encoding="utf-8")

print(f.tell())      #按字符计数
print(f.readline())  #读一行
print(f.tell())      #当前光标的位置

f.seek(0)   #回到指定的字符位置
print(f.readline())

print(f.encoding)   #显示打开文件的字符集

print(f.fileno())   # 3

print(f.name)   #打印文件名字

print(f.flush())  #刷新到磁盘,例子进度条
'''

f = open("yesterday2",'wb') #文件句柄  二进制文件
f.write("hello binary\n".encode())    #使用encode() 字符串转换成byte类型

f.close()



