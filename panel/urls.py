from django.contrib import admin
from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('valoresRef', views.valorRef, name="valoresRef"),
    path('altaInter', views.altaInterV, name="altaInter"),
    path('altaEnsayos', views.altaEnsayoV, name="altaEnsayos"),

]