#Author: xiaoyu hao

name = input("name:")
age = int(input("age:"))     #需要强制转换
job = input("job:")
salary = input("salary:")

#第一种变量赋值方式
info = '''
--------info of %s ------
name:%s
age:%d
job:%s
salary:%s
''' %(name,name,age,job,salary)

#第二种变量赋值方式
info2 = '''
--------info of {_name} ------
name:{_name}
age:{_age}
job:{_job}
salary:{_salary}
'''.format(_name=name,_age=age,_job=job,_salary=salary)

print(info2)
