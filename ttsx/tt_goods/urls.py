from django.conf.urls import url, include
import views

urlpatterns = [
    url('^$', views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list_goods),
    url(r'^(\d+)/$', views.detail),
    url('^search/$',views.MySearchView.as_view())
]
