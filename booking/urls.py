from django.contrib import admin
from django.urls import path,include
from booking import views

urlpatterns = [
    path("",views.booking_page,name='booking_page'),
    path("list/",views.listing_page,name='listing_page'),
    path('list/<int:pk>/',views.detail_view,name='detail_view'),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>/' ,views.delete,name='delete')
]
