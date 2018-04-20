from django.shortcuts import render,HttpResponse,render_to_response

# Create your views here.
import datetime


def index(req):
    class Person:
        def __init__(self,name,age):
            self.name=name
            self.age=age

    s="hello"
    s2=[1,22,333]
    s3={'username':'csking','sex':'jjj'}
    s4=datetime.datetime.now()
    s5=Person("csking",18)
    s6=6
    s7=[]
    s8=[11,223]
    s9='<a href="#">跳转</a>'
    return  render(req,'index.html',{'obj':s9})

def login(req):
    if req.method=="POST":
        return HttpResponse('OK')

    name="hello"
    num=66
    return render(req,"login.html",locals())


def ordered(req):
    return render(req,"ordered.html")

def shopping_car(req):
    return render(req,"shopping_car.html")
