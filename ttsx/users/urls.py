from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^index/$', views.index,name='index'),
     url(r'^login/$',views.login,name='login'),
     url(r'^register/$',views.register,name='register'),
     url(r'^register_handle/$',views.register_handle,name='register_handle'),
     url(r'^check_username_exist/$',views.check_username_exist,name='check_username_exist'),
]
