from django.db import models

# Create your models here.



class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    ut = models.ForeignKey('UserType',models.CASCADE)
class UserType(models.Model):
    caption = models.CharField(max_length=32)