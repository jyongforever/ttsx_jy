#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import views
from django.conf.urls import url
urlpatterns=[
    url('^$',views.index),
    url('^register/$',views.register),
    url('^register_handle/$',views.register_handle),
    url('^login/$',views.login),
    url('^register_username/$',views.register_username),
    url('^login_check/$',views.login_check),
    url('^login_userinfo/$',views.login_userinfo),

]


