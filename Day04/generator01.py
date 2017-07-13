__author__ = "xiaoyu hao"
#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
#列表：提前生成
L = [x * x for x in range(10)]
print(L)   #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 已经生成了结果
#生成器：只有访问的时候才生成
g = (x * x for x in range(10))
print(g)    #<generator object <genexpr> at 0x02CF5120>    只是提供了一种算法

#遍历
for i in g:
    print(i)

print(next(g))
print(next(g))
print(next(g))


#只有一个next() 方法，2.x __next__()

