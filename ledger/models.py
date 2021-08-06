from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from booking.models import BookingData



class Report(models.Model):
    event_date=models.OneToOneField(BookingData,on_delete=CASCADE)
    stage_decoration=models.IntegerField(null=True,blank=True)
    juice_counter=models.IntegerField(null=True,blank=True)
    pop_corn_machine=models.IntegerField(null=True,blank=True)
    sound_system=models.IntegerField(null=True,blank=True)
    other_income_1=models.IntegerField(null=True,blank=True)
    other_income_2=models.IntegerField(null=True,blank=True)
    other_income_3=models.IntegerField(null=True,blank=True)
    total_income=models.IntegerField(null=True,blank=True)
    report_submition_date=models.DateTimeField(auto_now_add=True)
    
    cleaning_charge=models.IntegerField()
    utensils_cleaning_charge=models.IntegerField()
    parking_charge=models.IntegerField(null=True,blank=True)
    waste_disposal_charge=models.IntegerField()
    trasportaion_charge=models.IntegerField(null=True,blank=True)
    detergents=models.IntegerField(null=True,blank=True)
    maintanance=models.IntegerField(null=True,blank=True)
    purchace_of_stock=models.IntegerField(null=True,blank=True)
    generator_fule=models.IntegerField(null=True,blank=True)
    electricity_bill=models.IntegerField(null=True,blank=True)
    water_charge=models.IntegerField(null=True,blank=True)
    other_expenditure_1=models.IntegerField(null=True,blank=True)
    other_expenditure_2=models.IntegerField(null=True,blank=True)
    other_expenditure_3=models.IntegerField(null=True,blank=True)
    other_expenditure_4=models.IntegerField(null=True,blank=True)
    total_expenditure=models.IntegerField()
    balance=models.IntegerField()
