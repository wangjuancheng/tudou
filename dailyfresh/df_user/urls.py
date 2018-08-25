from django.conf.urls import url
# from django.urls import path,re_path
from . import views



urlpatterns = [
    url(r'register/',views.register),
    url(r'register_handle/',views.register_handle),
    url(r'register_exit/', views.register_exit),
    url(r'login/', views.login),
    url(r'login_handle/', views.login_handle),
    url(r'info/', views.info),
    url(r'test/', views.test),
    url(r'site/$',views.site),
    url(r'order/$', views.order),

]