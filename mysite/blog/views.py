from django.shortcuts import render,HttpResponse,render_to_response,redirect

# Create your views here.
import datetime
from blog import models

def cur_time(request):

    times=datetime.datetime.now()

    # return HttpResponse("<h1>AAAA</h1>")
    return render(request,"cur_time.html",{"time":times})

# user_list =[]
def userInfo(req):

    if req.method=='POST':
        u = req.POST.get("username",None)
        s = req.POST.get("sex",None)
        e = req.POST.get("email",None)
        # user={"username":username,"sex":sex,"email":email}
        # user_list.append(user)
        models.UserInfo.objects.create(
            username=u,
            sex=s,
            email=e,
        )
    user_list=models.UserInfo.objects.all()
    return render(req,"index.html",{"user_list":user_list})

def special_case_2003(req):

    return HttpResponse("2003")

def year_archive(req,year,month):
    return  HttpResponse(year+"year"+month+"month")

def index(req):
    if req.method=="POST":
        username=req.POST.get("username")
        pwd=req.POST.get("pwd")

        if username == "alice" and pwd == "123":
            return HttpResponse("登陆成功！")

    # return render(req,"login.html")

    alex="you are welcome"
    eric="xxx"
    xialv="shax"
    aliv="handsome"

    # return render_to_response("new.html",locals())
    # return render(req,"new.html",locals())

    return redirect("https://www.baidu.com")

def login(req):

    if req.method=="POST":
        if 1:
            return redirect("https://www.baidu.com")

        return redirect("blog/login")

    return render(req,"login.html")

def introduce(req):
    return HttpResponse("OK")