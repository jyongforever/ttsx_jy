from django.db import models


# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=40)

    ushou = models.CharField(max_length=10, default='')
    uaddr = models.CharField(max_length=100, default='')
    uphone = models.CharField(max_length=11, default='')
