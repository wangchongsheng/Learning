from django.db import models

# Create your models here.

class UserType(models.Model):
    caption = models.CharField(max_length=32)

