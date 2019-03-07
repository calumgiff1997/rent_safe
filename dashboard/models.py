from django.db import models

class EmployeeManager(models.Model):
    employeeID = models.IntegerField(max_length=8, primary_key = True)
    password = models.CharField(max_length=32)
    
class Car(models.Model):
    registration = models.CharField(max_length=30, primary_key = True)
    make/model = models.CharField(max_length=30)
    issues = models.CharField(max_length=256)
    
class Contract(models.Model):
    contractID = models.CharField(max_length=32, primary_key = True)
    registration = models.CharField(max_length=16)
    employeeID = models.IntegerField(max_length=8)
    customerID = models.IntegerField(max_length=8)
                           

class Customer(models.Model):
    customerID = models.IntegerField(max_length=8, primary_key = True)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    email = models.CharField(max_length=32)
# Create your models here.l,.
