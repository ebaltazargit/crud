from django.contrib import admin
from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('valoresRef', views.valoresRef, name="valoresRef"),
    path('altaInter', views.altaInterfAZ, name="altaInter"),
    path('altaEnsayos', views.altaEnsayos, name="altaEnsayos"),

]