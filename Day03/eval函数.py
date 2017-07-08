#字符串转还成列表
a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
b = eval(a)

print(b)
print(b[0][1])

#字符串转换成字典
a1 = "{1: 'a', 2: 'b'}"
b = eval(a1)
print(b)

#字符串转换成元组
a3 = "([1,2], [3,4], [5,6], [7,8], (9,0))"
b = eval(a3)
print(b)


#arg = "{'bakend': 'www.oldboy.org','record':{'server': '100.1.7.9','weight': 20,'maxconn': 30}}"

arg = input("--->")
arg1 = eval(arg)
print(arg1)


