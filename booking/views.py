from mystatistics.models import Years
from mystatistics.views import allyear
from django.db.models.query import QuerySet
from django.http import request
from booking.forms import BookingForm
from django.shortcuts import redirect, render
from .forms import *
from .models import *
import datetime
from django.views import generic


# Create your views here.

def booking_page(request):
    

    form=BookingForm()
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid(): 
            form.save()

            
            
        return redirect('/booking/list/') 

    context={
        'form':form,
        
    }
    return render (request,'booking/booking.html',context)


def listing_page(request):
    record=BookingData.objects.all()
    months=Month.objects.all()

    context={
        'record':record,
        "months":months
    }
    return render(request,'booking/list.html',context)


def detail_view(request,pk):
    record=BookingData.objects.get(id=pk)
    record.balance=(record.total_amount-record.advance)
    record.save()

    context={
        'record': record,
        
    }
    return render(request,'booking/details.html',context)


def update(request,pk):

    record=BookingData.objects.get(id=pk)
    form=BookingForm(instance=record)
    if request.method=='POST':
        form=BookingForm(request.POST,instance=record)
        if form.is_valid():
            form.save()   
        return redirect('/booking/list/') 
    context={       
        'form':form,
        'record':record
    }
    return render(request,'booking/update.html',context)


def delete(request,pk):
    record=BookingData.objects.get(id=pk)

    if request.method=='POST':

        record.delete()
        return redirect('/booking/list')

    context={
        'record':record
    }

    return render(request,'booking/delete.html',context)
