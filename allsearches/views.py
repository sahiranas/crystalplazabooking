from django.shortcuts import redirect, render
from home.models import DateCheck

def allsearches(request):
    allseacrhes=DateCheck.objects.all()
    context={'alldatesearch':allseacrhes}

    return render(request,'allsearches/allsearches.html',context)

def delete_search_record(request,pk):
    object=DateCheck.objects.get(id=pk)
    object.delete()
    return redirect("/allsearches/")
