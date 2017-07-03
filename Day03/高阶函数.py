#f本身是要传入一个函数
def fun(a,b,f):
    return f(a) + f(b)

result = fun(-1,3,abs)
print(result)
