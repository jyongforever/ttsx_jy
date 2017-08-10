from django.conf.urls import url

import views

urlpatterns=[
    url(r'^add/$',views.add),
    url(r'^$',views.cart),
    url(r'^delcart/$',views.del_cart),
    url(r'^count/$',views.count),
    url(r'^add_count/$',views.add_count),
    url(r'^minus_count/$', views.minus_count),
    url(r'^change_count/$', views.change_count),
    url(r'^delorder/$',views.delorder),

]