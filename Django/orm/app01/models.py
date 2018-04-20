from django.db import models

models.CharField()


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=64)
    price = models.IntegerField()
    color = models.CharField(max_length=64,editable=True)
    page_num = models.IntegerField(null=True)


    publisher = models.ForeignKey("Publish",on_delete=models.CASCADE)  # 一对多关系--》Foreignkey

    # 接受对象
    author = models.ManyToManyField("Author")# 多对多关系

    def __str__(self):
        return self.title


class Publish(models.Model):
    # my_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=63)

    def __str__(self):
        return self.name



class Book2Author(models.Model):
    author=models.ForeignKey("Author",models.CASCADE)
    book=models.ForeignKey("Book",on_delete=models.CASCADE)

    class Meta:
        unique_together=["author","book"]

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
