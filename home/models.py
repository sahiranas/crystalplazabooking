from django.db import models

# Create your models here.
class Service(models.Model):
    title=models.CharField(max_length=100)
    

    def __str__(self):
        return (self.title)


class Features(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    icon_class=models.CharField(max_length=255)
    
    def __str__(self):
        return (self.title)

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