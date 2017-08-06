from django.conf.urls import url

from tt_cart import views

urlpatterns=[
    url(r'^add/$',views.add),
    url(r'^$',views.cart),
    url(r'^delcart/$',views.del_cart),
    url(r'^cart_count/$',views.cart_count),
    url(r'^add_count/$',views.add_count),
    url(r'^minus_count/$', views.minus_count),
    url(r'^change_count/$', views.change_count),

]