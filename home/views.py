from django.core.checks import messages
from django.shortcuts import redirect, render
from home.models import *
from booking.models import BookingData

# Create your views here.

def homepage(request):

    img=Portfolio.objects.all()
    booking_exist=False
    if request.method=='POST':
        dates=request.POST.get('date')
        name=request.POST['name']
        contact=request.POST['contact']
        booking_exist=False
        for each_booking in BookingData.objects.all():
            if str(each_booking.event_date)==str(dates):
                booking_exist=True
        

        temp=DateCheck(name=name,contact=contact,date=dates)
        object_exist=False

        for each in DateCheck.objects.all():
            if str(each.name)==str(temp.name) and str(each.contact)==str(temp.contact) and str(each.date)==str(temp.date):
                object_exist=True
            
        if object_exist ==False:
            temp.save()

    context={
 
        'img':img,
        'booking_exist':booking_exist
    }  

    return render(request,"home/index.html",context)



def sentmessage(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST["message"]
        Allmessages.objects.create(name=name,email=email,subject=subject,message=message)
        return redirect("/")