from django.conf.urls import url

from tt_order import views

urlpatterns=[
    url(r'^list/$',views.list),
    url(r'^handle/$',views.handle),
]