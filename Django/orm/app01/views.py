from django.shortcuts import render

# Create your views here.

from app01.models import Book

from app01 import models

def data_oper(req):

    # 添加对象
    # create方式一
    # pub=models.Publish.objects.filter(id=1)
    # authors=models.Author.objects.filter(id__gt=1)
    Book.objects.create(
        title="xx漂流记",
        price=1,
        color='yellow',
        publisher_id=4,
        # 因为外键关系是一对多，publisher只能对应一个对象，所以
        # publisher=pub[0]
    )
    book=models.Book.objects.filter(id=2)[0]


