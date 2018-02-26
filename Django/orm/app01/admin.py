from django.contrib import admin


from app01.models import *
# Register your models here.

class Myadmin(admin.ModelAdmin):
    list_display = ("title",'price','publisher','color')
    search_fields = ('title','price')
    # list_filter = ('title')

admin.site.register(Book,Myadmin)