from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BookMark(models.Model):
    url = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=80)
    enterdate = models.DateTimeField(auto_now_add=True)
    uniqueid = models.CharField(max_length=20)
    appuser = models.ForeignKey(User)
    def __str__(self):
        return self.url

class Click(models.Model):
    timestamp = models.DateTimeField
    url = models.ForeignKey(BookMark)
    def __str__(self):
        return self.url
