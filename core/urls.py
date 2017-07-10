# coding: utf-8
from django.conf.urls import url

from core import views
from core import apis


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/room/(?P<label>.+)', apis.room, name='room_api'),
    url(r'^room/(?P<label>.+)$', views.room, name='room'),
]
