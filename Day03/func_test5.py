#组合参数，实参个数不固定

def test(*args):
    print(args)

test(1,2,3,4,5)
test(*[1,2,3,4,5])  #    *args = *[1,2,3,4,5]   args = tuple([1,2,3,4,5])

# *args：接受N个位置参数，转换成元组形式
def test2(x,*args):
    print(x)
    print(args)

test2(1,2,3,4,5)


#可以传递字典，**kwargs接受的是关键字参数，转换成的是字典
def test3(**kwargs):
    print('name:',kwargs['name'])
    print('age:',kwargs['age'])
print("\ntest3()\n")
test3(name='haoxy',age=26,sex='F')   #  输出{'name': 'haoxy', 'age': 26, 'sex': 'F'}

#**kwages 与位置参数，默认参数同用，**kwargs放在最后
def test4(name,age=18,**kwargs):
    print(name)
    print(age)
    print(kwargs)

test4('alex',4,sex='m',hobby='car')  #或者test4('alex',age=4,sex='m',hobby='car')

def test5(*args,**kwargs):
    print(args)
    print(kwargs)

test4('alex',4,sex='m',hobby='car')  #或者test4('alex',age=4,sex='m',hobby='car')
print("test5:")
test5('alex',age=4,sex='m',hobby='car')  #或者test4('alex',age=4,sex='m',hobby='car')






