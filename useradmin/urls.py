"""useradmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from stage import views
from stage.views import * 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'BasicInfo', views.BasicInfoViewSet)
router.register(r'HostGroup', views.HostGroupViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^windowsapi/clooect$','stage.views.collect'),
    url(r'^windowsapi/gethost$','stage.views.gethosts'),
    #url(r'^linuxapi/clooect$','linuxserver.views.collect'),
    #url(r'^linuxapi/gethost$','linuxserver.views.gethosts'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
