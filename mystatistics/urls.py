from django.contrib import admin
from django.urls import path,include
from mystatistics import views

urlpatterns = [
    path("",views.statisticshome,name='statisticshome'),    
]























