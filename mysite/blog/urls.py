# @Time    : 2018/2/7 0007 15:40
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : urls.py

from django.contrib import admin
from django.urls import path, re_path, include
from blog import views

urlpatterns = [
    path("new/store/",views.introduce),
    path("pay/index/",views.index),
    path("login",views.login),
    ]