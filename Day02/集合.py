__author__ = "Alex Li"

list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)

list_2 =set([2,6,0,66,22,8,4])

print(list_1,list_2)

#交集
print(  list_1.intersection(list_2) )

#并集
print(list_1.union(list_2))

#差集 in list_1 but not in list_2
print(list_1.difference(list_2))   #list_1 里面有list_2里面没有的
print(list_2.difference(list_1))   #list_2 里面有，list_1里面的没有的

#子集
list_3 = set([1,3,7])
print(list_3.issubset(list_1))
print(list_1.issuperset(list_3))




#对称差集
print(list_1.symmetric_difference(list_2))


print("-------------")

list_4 = set([5,6,7,8])
print(list_3.isdisjoint(list_4)) # Return True if two sets have a null intersection.

print("------------------------------------------------------------------------")
print('''符号表示''')
print("list_1:",list_1)
print("list_2:",list_2)
#交集
print(list_1 & list_2)
#union
print(list_2 | list_1)

#difference
print(list_1 - list_2) # in list 1 but not in list 2

#对称差集,去掉了重复的
print(list_1 ^ list_2)

#插入
list_1.add(999)
list_1.update([888,777,555])
print(list_1)

#删除
print("删除：")
print("remove:",list_1.remove("9"))

#随机删除
print(list_1.pop())
print(list_1.pop())
print(list_1.pop())
print(list_1.pop())
print(list_1)

#
print("discard:")
print(  list_1.discard(888)  )  # Remove an element from a set if it is a member. 没有返回值

len(list_1)  #set的长度

x in list_1  #测试x是否是list_1的成员

x not in list_1  #测试x是否不是list_1的成员

list_2.issubset(list_1)
list_2 <= list_1  #测试是否s中的每一个元素都在t中

list_2.issuperset(list_1)
list_2 >= list_1   #测试是否list_1中的每一个元素都在s中

list_2.union(list_1)
list_2 | list_1    #返回一个新的  #set包含s和t中的每一个元素

list_2.intersection(list_1)
list_2 & list_1    #返回一个新的set包含list_1和list_2中的公共元素

list_2.difference(list_1)
list_2 - list_1    #返回一个新的set包含list_1中有但是list_2中没有的元素

list_2.symmetric_difference(list_1)
list_2 ^ list_1     #返回一个新的set包含list_2和list_1中不重复的元素

list_1.copy()        #返回set “list_1”的一个浅复制
