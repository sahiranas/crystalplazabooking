from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views

urlpatterns = [
path("",views.homepage,name="homepage"),

path("sentmessage/",views.sentmessage,name="sentmessage"),
# path("test",views.test)
]
