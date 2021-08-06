from django.contrib import admin
from django.urls import path,include
from allmessages import views

urlpatterns = [
    path("",views.allmessages,name='allmessages'),


]