#Author: xiaoyu hao

import copy

names = ["python","Java","C","C++","C#","python",["Oracle","Mysql","DB2"]]

#浅复制
names2 = names.copy()
names[2] = "PHP"  #修改第一层
names[6][2] = "Postgresql"  #修改第二层
print("原来的names")
print(names)
print("复制的names2")
print(names2)

#['python', 'Java', 'PHP', 'C++', 'C#', 'python', ['Oracle', 'Mysql', 'Postgresql']]
#['python', 'Java', 'C', 'C++', 'C#', 'python', ['Oracle', 'Mysql', 'Postgresql']]

#只复制第一层，第二层复制的是内存地址

#
#使用copy模块进行深copy
#

names_deep = copy.deepcopy(names)
print("原来的names")
print(names)
print("deep后的copy")
print(names_deep)