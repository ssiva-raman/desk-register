from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_info(models.Model):
    user_id=models.IntegerField(primary_key=True, unique=True, null=False)
    name= models.CharField(max_length=25, blank=False)
    age=models.IntegerField(blank=False)
    phone=models.CharField(unique=True,max_length=10, blank=False)
    
    def __str__(self):
        return self.name

class Treatment(models.Model):
    user=models.ForeignKey('User_info', on_delete=models.CASCADE)
    date= models.DateField()
    treatement=models.CharField(max_length=250)
    
    def __str__(self) :
        return (self.treatement)