from django.shortcuts import render



# Create your views here.


def csking(req):

    print('前端数据',req.GET)

    return  render(req,'index.html')