from django.urls import path
from . import views
from . import urlsNames as uname
from . import api
urlpatterns = [
    path('',views.index, name=uname.INDEX ),#POST
    path(f'{uname.LIST}/',views.list, name=uname.LIST ),#GET
    path(f'{uname.EDIT}/<int:id>',views.edit, name=uname.EDIT ),#GET
    path(f'{uname.GROUP}/',views.group, name=uname.GROUP ),#GET
    path(f'{uname.DELETE}/<int:id>',views.delete, name=uname.DELETE ),#DELETE
    path('api/list/', api.TodoListView.as_view(), name='materia-list'),#GET
    path('api/list/<int:pk>/', api.TodoDetailView.as_view(), name='materia-detail'),#POST
]

