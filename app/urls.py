from django.urls import path
from . import views
from . import urlsNames as uname
# from . import api
from . import analise

urlpatterns = [
    path('',views.index, name=uname.INDEX ),#POST
    path(f'{uname.LIST}/',views.list, name=uname.LIST ),#GET
    path(f'{uname.EDIT}/<int:id>',views.edit, name=uname.EDIT ),#GET
    path(f'{uname.GROUP}/',views.group, name=uname.GROUP ),#GET
    path(f'{uname.DELETE}/<int:id>',views.delete, name=uname.DELETE ),#DELETE
    path(f'{uname.BASE}/', views.pag, name=uname.BASE),#GET
 #   path('api/list/', api.TodoListView.as_view(), name='materia-list'),#GET
 #   path('api/list/<int:pk>/', api.TodoDetailView.as_view(), name='materia-detail'),#POST
    path(f'{uname.CH}/', analise.analise, name=uname.CH),#GET
    path(f'{uname.ADICIONAR_CH}/', analise.add_ch, name=uname.ADICIONAR_CH),#POST
    path(f'{uname.ATUALIZAR_CH}/', analise.atualizar, name=uname.ATUALIZAR_CH),#POST
    path(f'{uname.MAIN}/', views.main, name=uname.MAIN),#POST
]
