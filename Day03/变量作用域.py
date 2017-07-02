
# age = 23  #全局变量
# def change_name(name):
#     global sex  #强制修改成全局变量
#     sex = 'M'
#     print("before change",name)
#     name = 'HAOXY'  #局部变量，这个函数就是这个变量的作用域
#     print("after name:",name)
#
# name = 'haoxy'
# change_name(name)
# print(name)
# print(age)
# print("global:",sex)


names = ["scott","sys","system"]

def change_name():
    names[0] = "SCOTT"
    print("inside func:",names)

change_name()
print(names)

'''输出：
inside func: ['SCOTT', 'sys', 'system']
['SCOTT', 'sys', 'system']
'''






