from django.shortcuts import redirect, render
from booking.models import BookingData
from ledger.models import *
from ledger.forms import *
from mystatistics.models import YearlyReport, Years
from mystatistics.views import allyear
 
def allreports(request):
    not_found=False
    searchdatefield=None
    found=False
    if request.method=='POST':


       #fetching the date given by user for searching
        searchdate=request.POST.get('searchdate')
        
        all_dates=[]
        # fetching all dates in the booking model and storing it to an array
        for each in BookingData.objects.all():
            date=each.event_date
            all_dates.append(date)

            #checking whether the user given input is present in the Booking model, if yes then found is set to true
        found=False
        for each in all_dates:
            if str(searchdate)==str(each):
                found=True
        if found == True:
            bokingdatefield=BookingData.objects.get(event_date=searchdate)
            searchdatefield=Report.objects.get(event_date=bokingdatefield)
        else:
            searchdatefield=None

            

    allreports=Report.objects.all()
    context={
        'found':found,
        'searchdatefield':searchdatefield,
        'allreports':allreports
    }
    return render(request,'ledger/ledger.html',context)


def detailreport(request,pk):

    report=Report.objects.get(id=pk)
    context={
        'report':report
    }

    return render(request,'ledger/detailreport.html',context)


def newreport(request,pk):
    object=BookingData.objects.get(id=pk)
    form=ReportForm()
    
   
    if request.method=='POST':
        event_month=object.event_date.month
        form=ReportForm(request.POST)                
        if form.is_valid():
            total_rent=object.total_amount
            stage_decoration=form.cleaned_data['stage_decoration']
            juice_counter=form.cleaned_data['juice_counter']
            pop_corn_machine=form.cleaned_data['pop_corn_machine']
            sound_system=form.cleaned_data['sound_system']
            other_income_1=form.cleaned_data['other_income_1']
            other_income_2=form.cleaned_data['other_income_2']
            other_income_3=form.cleaned_data['other_income_3']
            total_income=stage_decoration+juice_counter+pop_corn_machine+sound_system+other_income_1+other_income_2+other_income_3+total_rent
            cleaning_charge=form.cleaned_data['cleaning_charge']
            utensils_cleaning_charge=form.cleaned_data['utensils_cleaning_charge']
            parking_charge=form.cleaned_data['parking_charge']
            waste_disposal_charge=form.cleaned_data['waste_disposal_charge']
            trasportaion_charge=form.cleaned_data['trasportaion_charge']
            detergents=form.cleaned_data['detergents']
            maintanance=form.cleaned_data['maintanance']
            purchace_of_stock=form.cleaned_data['purchace_of_stock']
            generator_fule=form.cleaned_data['generator_fule']
            electricity_bill=form.cleaned_data['electricity_bill']
            water_charge=form.cleaned_data['water_charge']
            other_expenditure_1=form.cleaned_data['other_expenditure_1']
            other_expenditure_2=form.cleaned_data['other_expenditure_2']
            other_expenditure_3=form.cleaned_data['other_expenditure_3']
            other_expenditure_4=form.cleaned_data['other_expenditure_4']
            total_expenditure=cleaning_charge+utensils_cleaning_charge+parking_charge+waste_disposal_charge+trasportaion_charge+detergents+maintanance+purchace_of_stock+generator_fule+electricity_bill+water_charge+other_expenditure_1+other_expenditure_2+other_expenditure_3+other_expenditure_4
            balance=total_income-total_expenditure








            Report.objects.create(
            event_date=object,
            stage_decoration=stage_decoration,
            juice_counter=juice_counter,
            pop_corn_machine=pop_corn_machine,
            sound_system=sound_system,
            other_income_1=other_income_1,
            other_income_2=other_income_2,
            other_income_3=other_income_3,
            total_income=total_income,
            cleaning_charge=cleaning_charge,
            utensils_cleaning_charge=utensils_cleaning_charge,
            parking_charge=parking_charge,
            waste_disposal_charge=waste_disposal_charge,
            trasportaion_charge=trasportaion_charge,
            detergents=detergents,
            maintanance=maintanance,
            purchace_of_stock=purchace_of_stock,
            generator_fule=generator_fule,
            electricity_bill=electricity_bill,
            water_charge=water_charge,
            other_expenditure_1=other_expenditure_1,
            other_expenditure_2=other_expenditure_2,
            other_expenditure_3=other_expenditure_3,
            other_expenditure_4=other_expenditure_4,
            total_expenditure=total_expenditure,
            balance=balance
            )

            #set this variable to true so that it wont be showing in all booking list
            object.is_completed=True
            object.save()

            #getting the year and montha of report
            yearofreport=str(object.event_date.year)
            monthofreport=object.event_date.month
            
            #getting all the years in the Years table which contain all  years after the report submission
            years=allyear()
            years=list(set(years))
            Yearyears=[]
            for each in Years.objects.all():
                year=each.year
                Yearyears.append(year)
            #checking wheter that if there is any year not presnt in YEars Model are present in year field in stattisctics if not create 12 month field corresponding to the year in YearlyReport field and the year in yealr modle
            for each_year in years:
                if (str(each_year) in str(Yearyears)):
                    continue
                else:
                    yearobject=Years.objects.create(year=each_year)
                    for i in range(1,13):

                        month = {	1:'January',
                                2:'February',
                                3:'March',
                                4:'April',
                                5:'May',
                                6:'June',
                                7:'July',
                                8:'August',
                                9:'September',
                                10:'October',
                                11:'November',
                                12:'December'		}

                        YearlyReport.objects.create(year=yearobject,month=i,month_name=month[i])                  
            yearofreportobject=Years.objects.get(year=yearofreport)
            #suuming the monthly staticstics in yearly report
            for each in YearlyReport.objects.filter(year=yearofreportobject):
                if each.month==monthofreport: 
                    each.total_income+=total_income
                    each.total_expenditure+=total_expenditure
                    each.total_gross+=balance
                    each.save() 
        return redirect("/ledger/")
    context={
        'form':form
    }
    return render(request,'ledger/newreport.html',context)
    