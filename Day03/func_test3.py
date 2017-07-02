def test1():
    print("test1")

def test2():
    print("test2")
    return 0

def test3():
    print("test3")
    return 1,'hello',{'name':'haoxy'},[1,2,3,4]

x=test1()
y=test2()
z=test3()

print(x)
print(y)
print(z)