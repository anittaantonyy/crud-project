from django.db import models

# Create your models here.

class employee(models.Model):


    name = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    adress = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

