from django.shortcuts import render,HttpResponse
import json

# Create your views here.
from django import forms
# 模板
class LoginForm(forms.Form):
    # 模板中的元素
    user = forms.CharField(min_length=6,error_messages={"required":"用户名不能为空","min_length":"用户名长度不能小于6位"})
    email = forms.EmailField(error_messages={"required":"邮箱不能为空","invalid":"邮箱格式错误"})



def login(request):
    if request.method == "GET":
        obj = LoginForm({"user":'test123','email':'test@qq.com'})
        return render(request,'login.html',{'oo':obj})
    elif request.method == "POST":
        """
        obj =  LoginForm(request.POST)

        # 验证
        status = obj.is_valid()
        print(status)
        value_dict = obj.clean()
        print(value_dict)
        error_obj = obj.errors.as_json()
        print(error_obj)
        return render(request,'login.html')
        """
        obj = LoginForm(request.POST)
        if obj.is_valid():
            value_dict = obj.clean()
            print(value_dict)
        else:
            # 封装了所有的错误信息
            pass
            # error_obj = obj.errors
            # print(error_obj['email'][0])
            # print(error_obj['user'][0])
        return render(request,'login.html',{'oo':obj})

def login_ajax(request):
    if request.method == "GET":
        return  render(request,'login_ajax.html')
    elif request.method == "POST":
        ret = {'status':True,'error':None,'data':None}
        print(request.POST)
        obj = LoginForm(request.POST)
        if obj.is_valid():
            print(obj.clean())
        else:
            # 方式一
            # res_str = obj.errors.as_json() # res_str是一个字符串
            # ret['status'] = False
            # ret['error'] = res_str
            # 两次反序列化
            # 方式二：

            ret['status'] = False
            ret['error'] = obj.errors.as_data()
            # 一次反序列化
        return HttpResponse(json.dumps(ret,cls=JsonCustonEncoder))

from django.core.validators import ValidationError
class JsonCustonEncoder(json.JSONDecodeError):
    def default(self,field):
        if isinstance(field,ValidationError):
            return {'code':field.code,'message':field.message}
        else:
            return json.JSONEncoder.default(self,field)

def detail(request):
    from app01 import forms
    obj = forms.DetailForm()

    return  render(request,'detail.html',{"obj":obj})

def field(request):
    from app01 import forms
    if request.method == 'GET':
        obj = forms.FieldForm()
        return render(request, 'field.html', {'obj': obj})
    elif request.method == 'POST':
        obj = forms.FieldForm(request.POST)
        obj.is_valid()
        print(obj.clean())
        print(obj.errors.as_json())
        return render(request,'field.html',{'obj':obj})

def widght(request):
    from app01 import forms
    if request.method == 'GET':
        obj = forms.WidghtFrom()
        return render(request, 'widght.html', {'obj': obj})
    elif request.method == 'POST':
        obj = forms.WidghtFrom(request.POST)
        obj.is_valid()
        print(obj.clean())
        print(obj.errors.as_json())
        return render(request,'widght.html',{'obj':obj})

def db(request):
    from app01 import forms
    from app01 import models
    if request.method == 'GET':
        obj = forms.DBForm()
        return render(request, 'db.html', {'obj': obj})