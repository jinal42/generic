from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User


# Register your models here.
class Custom(models.Model):
    name = models.CharField(max_length=20, blank=True)
    roll = models.IntegerField( blank=True)
    city = models.CharField(max_length=50, blank=True)



