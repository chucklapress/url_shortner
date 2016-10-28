from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType




# Create your models here.

class BookMark(models.Model):
    url = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=80)
    enterdate = models.DateTimeField(auto_now_add=True)
    hashid = models.CharField(max_length=20)
    appuser = models.ForeignKey(User)


    def __str__(self):
        return self.url

class Click(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    url = models.ForeignKey(BookMark)
    click_counts = models.IntegerField()
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.url)
