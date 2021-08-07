from django.db import models



class Portfolio(models.Model):
    img=models.ImageField(upload_to='imgs/')

class DateCheck(models.Model):
    name=models.CharField(max_length=200,default='Unknown')
    contact=models.IntegerField(null=True,blank=True)
    date=models.DateField()
    search_time=models.DateTimeField(auto_now_add=True)
        
class Allmessages(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    subject=models.CharField(max_length=70,null=True,blank=True)
    message=models.TextField(max_length=1000,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(self.subject)