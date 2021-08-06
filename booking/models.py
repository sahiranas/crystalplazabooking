from django.db import models
from django.db.models.fields import CharField
from django.core.validators import RegexValidator

# Create your models here.

class BookingData(models.Model):
    event_choices=(('Marriage Function (Day)',"Marriage Function (Day)"),
                   ('Meeting','Meeting'),
                   ('Reception(Evening)','Reception(Evening)'))

    # manager_name=models.CharField(max_length=50,null=True,blank=True,default='Mr.')
    event_date=models.DateField(null=False,blank=False,unique=True)
    name=models.CharField(max_length=255)
    event_type=models.CharField(choices=event_choices,max_length=255)
    bride_or_groom_name=models.CharField(max_length=255,null=True,blank=True)
    house_name=models.CharField(max_length=255)
    post=models.CharField(max_length=255,null=True,blank=True)
    location=models.CharField(max_length=255)
    booking_date=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)
    advance=models.PositiveIntegerField()
    total_amount=models.PositiveIntegerField(default=40000)
    balance=models.PositiveIntegerField(null=True)
    contact1=models.IntegerField()
    contact2=models.IntegerField()
    is_completed=models.BooleanField(default=False)
   
    kitchen_team=models.CharField(max_length=255,default='Not Provided',null=True,blank=True)
    kitchen_team_license=models.ImageField(upload_to='imgs/',null=True,blank=True)


    class Meta:
        ordering=('event_date',)
   
    

    def __str__(self):
        return( f"{self.name}'s {self.event_type} on {self.event_date} ")



class Month(models.Model):
    name=models.CharField(max_length=50)
    number=models.IntegerField()  
    
    class Meta:
        ordering=('number',)

    def __str__(self):
        return self.name




