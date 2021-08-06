from mystatistics.models import YearlyReport, Years
from django.shortcuts import render
from ledger.models import Report
from booking.models import BookingData,Month


#function to get all years of bookings 
def allyear():
    allbooking=BookingData.objects.all()
    allreports=Report.objects.all()
    allyears=[]
    for each_object in BookingData.objects.all():
        if each_object.is_completed==True:
            year=each_object.event_date.year
            allyears.append(year)
    return allyears    


def monthnameset():
    for eachobject in YearlyReport.objects.all():
        if eachobject.month==1:
            eachobject.month_name='January'




def statisticshome(request): 
    #calculating total statistics
    total_events=0
    total_income=0
    total_expenditure=0
    profit_gross=0
    for each_report in Report.objects.all():
        total_events+=1
        total_income+=each_report.total_income
        total_expenditure+=each_report.total_expenditure
        profit_gross+=each_report.balance         
    object=None
    year=''
    years=allyear()
    years=list(set(years)) #removing duplicates
    month_list=[] 
    if request.method == 'POST':              
        year=request.POST['year']
        yearobject=Years.objects.get(year=year)
        object=YearlyReport.objects.filter(year=yearobject)       
    context={
        'total_events':total_events,
        'total_income':total_income,
        'total_expenditure':total_expenditure,
        'profit_gross':profit_gross,
        'years':years,
        'year':year,
        'object':object,
    }
    return render(request,'mystatistics/statistics.html',context)


