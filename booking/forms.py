from django import forms
from django.db.models import fields

from.models import *

class BookingForm(forms.ModelForm):
    class Meta:
        model=BookingData
        fields=['event_date','name','event_type','bride_or_groom_name','house_name','post','location','advance','total_amount',
        'contact1','contact2']
    