from django.shortcuts import render,redirect,HttpResponse
from app01 import models


# Create your views here.

'''
def test(request):
    obj = HttpResponse('OK')
    import datetime
    v = datetime.datetime.utcnow() +datetime.timedelta(seconds=5)
    obj.set_cookie('k1','v1',max_age=10,expires=v)
    return obj

def login(request):
    # models.Administrator.objects.create(
    #     username='test',
    #     password='123123'
    # )
    message =""
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        c = models.Administrator.objects.filter(username=user,password=pwd)
        if c:
            # 在神奇的地方放置当前用户名
            # 神奇的地方，在用户的浏览器上，硬盘的某个位置
            # Cookie
            rep = redirect('/index.html')
            import time
            import datetime
            timeout = datetime.datetime.now()-datetime.timedelta(seconds=5)
            rep.set_cookie('username',user,expires=timeout) #设置cookie超时时间
            rep.set_cookie('email',user+'@live.com')

            # rep.set_signed_cookie('username',user)
            # rep.set_signed_cookie('pwd',pwd)
            return rep

        else:
            message = "用户名或密码错误"
    return render(request, "login.html",{'msg':message})

def index(requst):
    # 如果用户已经登陆，获取当前登陆的用户名
    # 否则返回登陆页面
    username = requst.COOKIES.get('username')
    if username:
        return render(requst,'index.html',{'username':username})
    else:
       return redirect('/login.html')

    # username="csking"
    # return render(requst,"index.html",{'username':username})
'''
from django import views

class Login(views.View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html',{'msg':''})

    def post(self,request,*args,**kwargs):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        c = models.Administrator.objects.filter(username=user,password=pwd).count()
        if c:
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('index.html')
            return rep
        else:
            message = "用户名或密码错误"
            return render(request,'login.html',{'msg':message})

# FBV
