from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
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

def logout(request):
    #清空session
    request.session.clear()
    return redirect('/login/')