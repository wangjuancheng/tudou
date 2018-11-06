from django.conf.urls import include,url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^index/$', views.index ),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.list),
    url(r'^(\d+)/$', views.detail),

]