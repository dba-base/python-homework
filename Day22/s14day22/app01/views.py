from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        print(settings.CSRF_HEADER_NAME)
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        print(user,pwd)
        if user == 'root' and pwd == '123':
            #session中设置值
            request.session['username'] = user
            request.session['is_login'] = True
            if request.POST.get('rmb',None) == '1':
                #设置超时时间
                request.session.set_expiry(10)
            return redirect('/index/')
        else:
            return render(request,'login.html')

def index(request):
    # session中获取值
    if request.session['is_login']:
        return HttpResponse(request.session['username'])
    else:
     return HttpResponse('gun')

<<<<<<< HEAD
######################## Form #####################
from django import forms
from django.forms import widgets
from django.forms import fields
class FM(forms.Form):
    # 字段本身只做验证
    user = fields.CharField(
        error_messages={'required': '用户名不能为空.'},
        widget=widgets.Textarea(attrs={'class': 'c1'}),
        label="用户名",
        )
    pwd = fields.CharField(
        max_length=12,
        min_length=6,
        error_messages={'required': '密码不能为空.', 'min_length': '密码长度不能小于6', "max_length": '密码长度不能大于12'},
        widget=widgets.PasswordInput(attrs={'class': 'c2'})
    )
    email = fields.EmailField(error_messages={'required': '邮箱不能为空.','invalid':"邮箱格式错误"})

    # f = fields.FileField()

    p = fields.FilePathField(path='app01')

    city1 = fields.ChoiceField(
        choices=[(0,'上海'),(1,'广州'),(2,'东莞')]
    )
    city2 = fields.MultipleChoiceField(
        choices=[(0,'上海'),(1,'广州'),(2,'东莞')]
    )

from app01 import models
def fm(request):
    if request.method == "GET":
        # 从数据库中吧数据获取到
        dic = {
            "user": 'r1',
            'pwd': '123123',
            'email': 'sdfsd@qq.com',
            'city1': 1,
            'city2': [1,2]
        }
        obj = FM(initial=dic)
        return render(request,'fm.html',{'obj': obj})
    elif request.method == "POST":
        # 获取用户所有数据
        # 每条数据请求的验证
        # 成功：获取所有的正确的信息
        # 失败：显示错误信息
        obj = FM(request.POST)
        r1 = obj.is_valid()   #验证请求的内容和Form1里面的是否验证通过。通过是True，否则False。
        print(r1)
        if r1:
            # obj.cleaned_data
            print(obj.cleaned_data)
            # cleaned_data类型是字典，里面是提交成功后的信息
            # 输出为字典{'user': 'r1', 'pwd': 'aaaaaaa', 'email': 'sdfsd@qq.com', 'p': 'app01/__init__.py', 'city1': '1', 'city2': ['1', '2']}
            print(obj.cleaned_data.get('user'))
            #输出 r1
            models.UserInf.objects.create(**obj.cleaned_data)
        else:
            # ErrorDict
            # print(obj.errors.as_json())
            # print(obj.errors['user'][0])
            return render(request,'fm.html', {'obj': obj})
        return render(request,'fm.html')
=======
def logout(request):
    #清空session
    request.session.clear()
    return redirect('/login/')
>>>>>>> 60b0239ea35daa7a919c8e221a922a9c17116c8b
