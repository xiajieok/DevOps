#!/usr/bin/env python3


from django.conf.urls import url,include
from rest_framework import routers

from Sansa import rest_views

router = routers.DefaultRouter()
router.register(r'users',rest_views.UserViewSet)
router.register(r'assets',rest_views.AssetViewSet)
router.register(r'manufactories',rest_views.ManufactoryViewSet)



urlapatterns = [
    url(r'^',include(routers.url)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]


