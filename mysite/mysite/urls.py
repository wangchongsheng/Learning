"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blog/', include('blog.urls')),
    path('login/',views.login),
    path('home/',views.home),
    path('cur_time/',views.cur_time),

    # path('cur_time/',views.cur_time),
    # path("userInfo/",views.userInfo),

    # re_path(r'^articles/[0-9]{4}/$',views.special_case_2003),

    # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',views.year_archive),

    # path("index",views.index,{"name":"Alice"}),
    # path("pay/index/",views.index,name="alice")

]
