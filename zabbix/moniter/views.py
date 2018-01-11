from django.shortcuts import render
from  .models import Zabbix_moniter

# Create your views here.

def home(request):
    return render(request,'home.html',{
        'zabbix':Zabbix_moniter.objects.all().order_by('name'),
    })