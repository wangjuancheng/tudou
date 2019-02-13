from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^order/$', views.order ),
    url(r'^order_handle/$', views.order_handle),

]