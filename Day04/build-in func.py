__author__ = "xiaoyu hao"

#print( all([1,-5,3]) )
#print( any([]) )
# a= ascii([1,2,"开外挂开外挂"])
# print(type(a),[a])
# a = bytes("abcde",encoding="utf-8")
# b = bytearray("abcde",encoding="utf-8")
# print( b[1] )
# b[1]= 50
# print(b)


#print(a.capitalize(),a)
# def sayhi():pass
# print( callable(sayhi) )

code = '''
def fib(max): #10
    n, a, b = 0, 0, 1
    while n < max: #n<10
        #print(b)
        yield b
        a, b = b, a + b
        #a = b     a =1, b=2, a=b , a=2,
        # b = a +b b = 2+2 = 4
        n = n + 1
    return '---done---'

#f= fib(10)
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

'''

py_obj = compile(code,"err.log","exec")
exec(py_obj)

exec(code)

dir([])  #查看所有的方法

# 匿名函数，三元运算
def sayhi(n):
    print(n)
    for i in range(n):
        print(i)
sayhi(3)

#(lambda n:print(n))(5)
calc = lambda n:3 if n<4 else n
print(calc(2))

#res = filter(lambda n:n>5,range(10))  #过滤出大于5的数字，迭代器
res = map(lambda n:n*2,range(10))
res = [ lambda i:i*2 for i in range(10)]
import functools
res = functools.reduce( lambda x,y:x*y,range(1,10 )) # 依次相乘（阶乘） 1 + 2 + 3 + ... + 10 = 45
print(res )

a = frozenset([1,4,333,212,33,33,12,4]) #不可修改的列表
#print(globals())

def test():
    local_var =333
    print(locals())     #取到局部变量
    print(globals())   # 取到所有的全局变量，生成一个字典
test()
print(globals())
print(globals().get('local_var'))


a = {6:2,8:0,1:4,-5:6,99:11,4:22}

#print(  sorted(a.items()) )
print(  sorted(a.items(),key=lambda x:x[1]) )
print(a )

a = [1,2,3,4,5,6]
b = ['a','b','c','d']

for i in zip(a,b):   #两个列表组合成字典
    print(i)

#import 'decorator'
print("__import__:")
__import__('decorator01')  #通过字符串类型导入模块

print('hash_value:',hash('郝晓宇'))


#转八进制
oc=oct(8)
print(oc)

#转二进制

rep = repr('c')
print(rep)


a = { 1:12,8:323,9:3,-2:5 }
print(sorted(a.items()))   #按key排序
print(sorted(a.items(),key=lambda x:x[1]))   #按值排序
#print(a)

