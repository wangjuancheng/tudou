from django.conf.urls import include,url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^cart/$',views.cart),
    url(r'^add(\d+)_(\d+)/$', views.add),
    url(r'^edit(\d+)_(\d+)/$', views.edit),
    url(r'^delete(\d+)/$', views.delete),

]