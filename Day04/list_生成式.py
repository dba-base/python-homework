__author__ = "xiaoyu hao"

i = [i*2 for i in range(10)]
print(i)


#相当于
a = []
for i in range(10):
    a.append(i*2)

print(a)