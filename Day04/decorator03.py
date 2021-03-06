__author__ = "xiaoyu hao"

装饰器带参数
user,passwd = 'alex','123'

def auth(auth_type):
    #print("auth.py func:", auth_type)
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and passwd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    res = func(*args,**kwargs)
                    print("------after authentication-----")
                    return res      #加上返回值，支持函数中的返回值，不返回的话，被修饰函数如果有返回值的话，无法返回
                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            elif auth_type == "ldap":
                print("通过ldap远程验证方式登陆......... ")
        return wrapper
    return outer_wrapper

def index():
    print("welcome to index page ... ")

@auth(auth_type="local")   # home = outer_wrapper(home)  home = wrapper()
def home():
    print("welcome to home page ... ")
    return "from home"

@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs page ... ")


index()
print(home())
bbs()