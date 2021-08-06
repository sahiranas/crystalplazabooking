from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, SET_DEFAULT

class User(AbstractUser):
    id_proof=models.ImageField(upload_to='imgs/',null=True,blank=True)
    contact=models.IntegerField(null=True,blank=True)


class Owners(models.Model):
    user=models.OneToOneField('User',on_delete=SET_DEFAULT, default='not Exist')


class Manager(models.Model):
    user=models.OneToOneField('User',on_delete=SET_DEFAULT, default='not Exist')


