#!/usr/bin/env python

from django.urls import path
from . import views
from fruit.views import master, add_it



urlpatterns =[
    path('', views.index, name='index'),
    path('top', views.top, name='top'),
    path('master', views.master, name='master'),
    path('jouhou', views.jouhou, name='jouhou'),
    path('toukei', views.toukei, name='toukei'),
  #  path('add', views.add, name='add'),
    path('add', views.add_it, name='add'),
]
