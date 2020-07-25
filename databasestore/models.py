from django.db import models
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
