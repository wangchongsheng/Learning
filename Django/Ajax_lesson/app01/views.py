from django.shortcuts import render,HttpResponse

# Create your views here.


def index(req):

    return render(req,"index.html")

def ajax_receive(req):
    if req.method=="POST":
        print("req.POST",req.POST)
    return HttpResponse("hello2")

def ajax_register(req):
    if req.method=="POST":
        username=req.POST.get("username")
        if username=="alex":
            return HttpResponse("1")
        return HttpResponse("0")
    return render(req,"register.html")
