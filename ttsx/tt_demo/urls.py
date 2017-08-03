# coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^mce/$',views.mce),
    url(r'^mce2/$', views.mce2),

]
