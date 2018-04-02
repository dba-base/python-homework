from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.shortcuts import redirect

def login(request):

    # request 包含用户提交的所有信息
    # 获取用户提交的方法
    # print(requext.method)

    error_msg = ''

    if request.method == 'POST':
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'root' and pwd == '123':
            #去跳转
            return redirect('/home')
        else:
            #用户名和密码不匹配
            error_msg = '用户名或密码错误'

    return render(request,'login.html',{'error_msg':error_msg})   # 传递到login.html并替换error_msg

USER_LIST = [
    {'username':'hxy','email':'1234567','gender':'男'},
    {'username':'rdl','email':'1234567','gender':'男'},
    {'username':'lsq','email':'1234567','gender':'男'},
    {'username':'hbz','email':'1234567','gender':'男'},
]

def home(request):
    if request.method == 'POST':
        #获取用户提交的表单数据，post请求
        u = request.POST.get('username')
        e = request.POST.get('email')
        g = request.POST.get('gender')
        temp = {'username':u,'email':e,'gender':g}
        USER_LIST.append(temp)
    return render(request,'home.html',{'user_list':USER_LIST})   #user_list变量传递到home.html页面