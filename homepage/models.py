import email
from django.db import models
# What is model??
# Model is a structure that defines the structure of the data that will be stored in the database. 

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()   
    age = models.IntegerField()
    phone = models.CharField(max_length=10, blank=True)  


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    