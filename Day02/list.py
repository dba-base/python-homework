#Author: xiaoyu hao

names = ["python","Java","C","C++","C#","python"]

#遍历
print(names[1])
#切片
print(names[1:3]) #['Java', 'C']
print(names[1:])
print(names[-2]) #C++
print(names[-3:-1])
print(names[-2:]) #取最后两个值

print("步长切片：") #隔一个打印一个
print(names[::2])   # ['python', 'C', 'C#']


print("for遍历：")
for i in names:
    print(i)



#插入
names.append("Ruby") #插入到最后
print(names)

names.insert(1,"PHP") #插入指定位置
print(names)

#修改
names[2] = "Go"
print(names)


#删除
print("删除：")
names.remove("PHP")  #删除指定值
print(names)

del names[2]  #删除指定位置的值
print(names)

names.pop()   #默认删除最后一个值
print(names)

names.pop(1)  #删除指定位置
print(names)

print(names.index("python")) #输出所在位置
print(names[names.index("python")])

#统计python的个数
print(names.count("python"))

#反转
print("反转：")
names.reverse()
print(names)

#排序 按ASCII码排序
print("排序：")
names.sort()
print(names)

#合并
print("合并列表")
names2 = ["Oracle","Mysql","DB2"]
names.extend(names2)
print(names)
#清空
print("清空：")
names.clear()
print(names)

#enumerate内置函数：打印出list中元素的下表

a = [1,2,3,4]
for i in enumerate(a):
    print(i)

'''
输出：
(0, 1)
(1, 2)
(2, 3)
(3, 4)
'''