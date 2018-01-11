from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Zabbix_moniter(models.Model):
    name = models.CharField(max_length=50,null=True)
    ip = models.CharField(max_length=20)
    ping = models.IntegerField(null=True)
    disk = models.DecimalField(max_digits=5,decimal_places=2,null=True)

    def __unicode__(self):
        return  self.name