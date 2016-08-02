# -*- coding: utf-8 -*-
# author: jeremy

from django.conf.urls import url, include
from rest_framework import routers
from api.restful import (
    users,
    example,
)

router = routers.DefaultRouter()
router.register(r'users', users.UserViewSet)
router.register(r'groups', users.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^example/', example.ExampleView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
