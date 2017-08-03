from django.conf.urls import url
import views

urlpatterns = [
    url('^$', views.index),
    url(r'^list(\d+)_(\d+)/$', views.list_goods),
    url(r'^detail/$', views.list_detail),

]
