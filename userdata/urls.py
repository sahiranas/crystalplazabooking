from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *
from userdata import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
path("registration/",views.userregistration,name="userregistration"),
path("registration/userregistration/",views.userregistration,name="userregistration"),
path("dashboard/",views.dashboard,name='dashboard'), 
path("login/",LoginView.as_view(),name='login'),
path("logout/",LogoutView.as_view(),name='logout')



]