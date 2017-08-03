# coding=utf-8
from django.db import models
from tinymce.models import HTMLField

class GoodsInfo(models.Model):
    gcontent=HTMLField()