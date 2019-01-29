#from django.conf.urls import url
from booktest import views
from django.contrib import admin
from django.conf.urls import include, url
urlpatterns = [
    #配置首页url
    url(r'^$',views.index),
    url(r'^delete(\d+)/$',views.delete),
    url(r'^create/$', views.create),
    url(r'^static_test/$',views.static_test),
]