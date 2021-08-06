from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, CharField

# Create your models here.

class Years(models.Model):
    year=models.CharField(max_length=4)
    def __str__(self):
        return self.year

         


class YearlyReport(models.Model):
    year=models.ForeignKey(Years,on_delete=CASCADE)
    month=models.IntegerField()
    month_name=models.CharField(max_length=50,default='xxxx')
    total_income=models.PositiveIntegerField(default=0)
    total_expenditure=models.PositiveIntegerField(default=0)
    total_gross=models.IntegerField(default=0)

    def __str__(self):
        return (f"{self.year}- {self.month}") 