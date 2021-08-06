from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, SET_DEFAULT

class User(AbstractUser):
    pass



class Owners(models.Model):
    user=models.OneToOneField('User',on_delete=SET_DEFAULT, default='not Exist')
    is_owner=models.BooleanField(default=True)
    


class Manager(models.Model):
    user=models.OneToOneField('User',on_delete=SET_DEFAULT, default='not Exist')
    name=models.CharField(max_length=20,default='Manager')
    is_manager=models.BooleanField(default=True)
    id_proof=models.ImageField(upload_to='imgs/',null=True,blank=True)
    contact=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return (self.user.username)


