__author__ = "xiaoyu hao"

#除了第一个和第二个数外，任意一个数都可以由前两个数相加得到
#1，1，2，3，5，8，13，21 ....

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        yield b   #换成yield就变成了生成器
        a, b = b, a + b
        n = n + 1
    return 'done'

#f = fib(10)
#print(f)     #<generator object fib at 0x034B6120>
#print(f.__next__())
#print(f.__next__())
#print(f.__next__())
#print(f.__next__())
#print(f.__next__())
#print(f.__next__())

