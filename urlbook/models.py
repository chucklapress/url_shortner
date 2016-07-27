from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Click(models.Model):
    timestamp = models.DateTimeField
    url = models.CharField(max_length=25)
    appuser = models.CharField(max_length=25)


class BookMark(models.Model):
    url = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=80)
    enterdate = models.DateTimeField(auto_now_add=True)
    uniqueid = models.CharField(max_length=20)
    appuser = models.ForeignKey(User)
