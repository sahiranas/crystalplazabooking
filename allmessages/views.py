from home.models import Allmessages
from django.shortcuts import render

def allmessages(request):
    messages=Allmessages.objects.all()
    context={'messages':messages
        }

    return render(request,'allmessages/allmessages.html',context)
