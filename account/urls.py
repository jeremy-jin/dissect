# -*- coding: utf-8 -*-
# author: jeremy

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.UserRegister.as_view(), name='register'),
    url(r'^class-base/$', views.CreateUserProfile.as_view(), name='users-class-base'),
    url(r'^myuser/$', views.MyUserProfile.as_view(), name='myuser'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
