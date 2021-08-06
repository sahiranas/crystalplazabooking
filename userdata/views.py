from django.core.checks import messages
from django.shortcuts import redirect, render
from .models import *

def userregistration(request):

    if request.method=='POST':
        f_name=request.POST['firstname']
        l_name=request.POST['lastname']
        username=request.POST['username']
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User already exist")
            else :
                user =User.objects.create_user(username=username,password=password1,email=email,first_name=f_name,last_name=l_name) 
                user.save()
                Manager.objects.create(user=user)
                return redirect ('/user/registration/')


    return render(request,"userdata/registration.html")



def dashboard(request):
    return render(request,'userdata/dashboard.html')



   ##program to add two numbers
