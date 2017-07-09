
#相当于局部变量
def foo():
    print("in the foo")
    def bar():
        print("in the bar")
    bar()

foo()