from django.contrib import admin
from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^backendindex$', views.backendindex, name="backendindex"),

    url(r'^mybackend_typeindex$', views.mybackend_typeindex, name="mybackend_typeindex"),
    url(r'^mybackend_ptypeadd$', views.mybackend_ptypeadd, name="mybackend_ptypeadd"),
    url(r'^mybackend_typeadd/(?P<tid>[0-9]+)$', views.mybackend_typeadd, name="mybackend_typeadd"),
    url(r'^mybackend_ptypeinsert$', views.mybackend_ptypeinsert, name="mybackend_ptypeinsert"),
    url(r'^mybackend_typeinsert$', views.mybackend_typeinsert, name="mybackend_typeinsert"),
    url(r'^mybackend_typedelete/(?P<tid>[0-9]+)$', views.mybackend_typedelete, name="mybackend_typedelete"),
    url(r'^mybackend_ptypeedit/(?P<tid>[0-9]+)$', views.mybackend_ptypeedit, name="mybackend_ptypeedit"),
    url(r'^mybackend_typeedit/(?P<tid>[0-9]+)$', views.mybackend_typeedit, name="mybackend_typeedit"),
    url(r'^mybackend_ptypeupdate/(?P<tid>[0-9]+)$', views.mybackend_ptypeupdate, name="mybackend_ptypeupdate"),
    url(r'^mybackend_typeupdate/(?P<tid>[0-9]+)$', views.mybackend_typeupdate, name="mybackend_typeupdate"),



    url(r'^mybackend_goodsindex/(?P<tid>[0-9]+)$', views.mybackend_goodsindex, name="mybackend_goodsindex"),
    url(r'^mybackend_goodsadd$', views.mybackend_goodsadd, name="mybackend_goodsindex"),
    url(r'^mybackend_goodsinsert$', views.mybackend_goodsinsert, name="mybackend_goodsinsert"),
    url(r'^mybackend_goodsdelete/(?P<tid>[0-9]+)$', views.mybackend_goodsdelete, name="mybackend_goodsdelete"),

    url(r'^mybackend_goodsedit/(?P<tid>[0-9]+)$', views.mybackend_goodsedit, name="mybackend_goodsedit"),
    url(r'^mybackend_goodsupdate/(?P<tid>[0-9]+)$', views.mybackend_goodsupdate, name="mybackend_goodsupdate"),

    url(r'^mybackend_neworders$', views.mybackend_neworders, name="mybackend_neworders"),
    url(r'^mybackend_historyorders$', views.mybackend_historyorders, name="mybackend_historyorders")

]
