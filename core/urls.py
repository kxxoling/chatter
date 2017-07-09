# coding: utf-8
from django.conf.urls import url

from core import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^room/(?P<label>.+)$', views.room, name='room'),
]
