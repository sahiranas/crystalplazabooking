from django import forms
from ledger.models import *


class ReportForm(forms.Form):
    stage_decoration=forms.IntegerField()
    juice_counter=forms.IntegerField()
    pop_corn_machine=forms.IntegerField()
    sound_system=forms.IntegerField()
    other_income_1=forms.IntegerField()
    other_income_2=forms.IntegerField()
    other_income_3=forms.IntegerField()
   
    cleaning_charge=forms.IntegerField()
    utensils_cleaning_charge=forms.IntegerField()
    parking_charge=forms.IntegerField()
    waste_disposal_charge=forms.IntegerField()
    trasportaion_charge=forms.IntegerField()
    detergents=forms.IntegerField()
    maintanance=forms.IntegerField()
    purchace_of_stock=forms.IntegerField()
    generator_fule=forms.IntegerField()
    electricity_bill=forms.IntegerField()
    water_charge=forms.IntegerField()
    other_expenditure_1=forms.IntegerField()
    other_expenditure_2=forms.IntegerField()
    other_expenditure_3=forms.IntegerField()
    other_expenditure_4=forms.IntegerField()
    



   
        # fields=['stage_decoration','juice_counter','pop_corn_machine','sound_system','other_income_1','other_income_2',
        # 'other_income_3','tota_income','cleaning_charge','utensils_cleaning_charge','parking_charge','waste_disposal_charge',
        # 'trasportaion_charge','detergents','maintanance','purchace_of_stock','generator_fule','electricity_bill','water_charge',
        # 'other_expenditure_1','other_expenditure_2','other_expenditure_3','other_expenditure_4','total_expenditure']