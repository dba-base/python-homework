#Author: xiaoyu hao

_name = "haoxy"
_passwd = "123"

username = input("name:")
passwd = input("passwd:")

if username == _name  and passwd == _passwd :
    print("welcome login {name}!".format(name=username))
else:
    print("username or password invale!")