from django.db import models

models.CharField()


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=64)
    price = models.IntegerField()
    color = models.CharField(max_length=64)
    page_num = models.IntegerField(null=True)
    publisher = models.ForeignKey("Publish",on_delete=models.CASCADE)  # 一对多关系--》Foreignkey

    # 接受对象
    author = models.ManyToManyField("Author")

    def __str__(self):
        return self.title


class Publish(models.Model):
    # my_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=63)

    def __str__(self):
        return self.city


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
