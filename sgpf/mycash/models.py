from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    photo = models.CharField(max_length=100)
