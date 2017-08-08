# -*- coding:utf-8 -*-
import views
from django.conf.urls import url

urlpatterns = [
    url('^$', views.info),
    url('^register/$', views.register),
    url('^register_handle/$', views.register_handle),
    url('^login/$', views.login),
    url('^register_username/$', views.register_username),
    url('^login_check/$', views.login_check),
    url('^order(\d*)/$', views.order),
    url('^site/$', views.site),
    url('^logout/$', views.logout),
    url('^islogin/$',views.islogin),
]
