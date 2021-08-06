from django.contrib import admin
from django.urls import path,include
from ledger import views

urlpatterns = [
    path("",views.allreports,name='allreports'),
    path("<int:pk>/",views.detailreport,name='detailreport'),
    path("newreport/<int:pk>/",views.newreport,name="newreport")

] 