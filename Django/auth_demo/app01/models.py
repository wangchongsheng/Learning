from django.db import models
from django.contrib.auth.models import User,AbstractUser


# Create your models here.
# class Users(models.Model):
#     username = models.CharField(max_length=16)
#     password = models.CharField(max_length=32)


class UserInfo(AbstractUser):
    phone = models.CharField(max_length=11)
    addr = models.CharField(max_length=255)

