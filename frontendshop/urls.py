from django.contrib import admin
from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^index$', views.index, name="index"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^dologin$', views.dologin, name='dologin'),
    url(r'^list$', views.list, name='list'),
    url(r'^draw$', views.draw_certificate, name='draw_certificate'),
	url(r'^vipusers$', views.vipusers, name='vipusers'),
	url(r'^shoppingCart$', views.shoppingCart, name='shoppingCart'),
	

]
