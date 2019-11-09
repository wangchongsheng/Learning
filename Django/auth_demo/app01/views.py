from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app01 import models
from functools import wraps


# 账号：demo 密码：123456
# # Create your views here.
# def check_login(f):
#     @wraps(f)
#     def inner(request, *args, **kwargs):
#         if request.session.get("is_login") == "1":
#             return f(request, *args, **kwargs)
#         else:
#             return redirect("/login")
#
#     return inner
#
#
# def login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = models.User.objects.filter(username=username, password=password)
#         if user:
#             # Login succeed
#             request.session['is_login'] = "1"
#             request.session['user_id'] = user[0].id
#             # 1. 生成特殊的字符串
#             # 2. 特殊字符串当成key，再数据库中对应一个session value
#             # 3. 在响应中向浏览器写一个cookie，cookie值就是特殊的字符串
#             return redirect("/index")
#     return render(request, 'login.html')
#
# @check_login
# def index(request):
#     user_id = request.session.get("user_id")
#     # 根据ID去数据库查找用户
#     user_obj = models.User.objects.filter(id=user_id)
#     if user_obj:
#         return render(request, "index.html",{"user":user_obj[0]})
#     else:
#         return render(request, "index.html", {"user": "匿名用户"})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 判断密码是否正确
        user = auth.authenticate(username=username, password=password)
        if user:
            # 判断是否是认证用户
            ret = user.is_authenticated
            print(ret)
            # 将登录的用户封装到request.user
            auth.login(request, user)
            return redirect("/index/")
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("/login/")


# def register(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         # User.objects.create(username=username, password=password) #这个不能用，密码没有sha加密
#         User.objects.create_user(username=username, password=password)
#         return HttpResponse(username + '账号创建成功,<a href="/login/">点击登录</a>')
#     return render(request, 'register.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # User.objects.create(username=username, password=password) #这个不能用，密码没有sha加密
        models.UserInfo.objects.create_user(username=username, password=password)
        return HttpResponse(username + '账号创建成功,<a href="/login/">点击登录</a>')
    return render(request, 'register.html')

def setpasswd(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        new_password = request.POST.get("newpasswd")
        user = User.objects.get(username=username)
        # 校验原来的密码是否正确
        # ret=user.check_password(password)
        # print(ret)
        # 修改密码
        user.set_password(new_password)
        user.save()
        return HttpResponse('密码修改成功,<a href="/login/">点击登录</a>')
    return render(request, 'setpasswd.html')


@login_required
def index(request):
    print(request.user.username)
    print("=" * 50)
    return render(request, "index.html")
