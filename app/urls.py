from django.urls import path
from . import views
from . import urlsNames as uname

urlpatterns = [
    path('',views.index, name=uname.INDEX ),#POST
    path('list/',views.list, name=uname.LIST ),#GET
]