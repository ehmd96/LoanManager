from django.db import models
# Create your models here.

class Agent(models.Model):
    name = models.CharField(default="", max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

class Customer(models.Model):
    name = models.CharField(default="", max_length=150)
    loanAmount = models.IntegerField(default=0)
    expectedPaidAmount = models.IntegerField(default=0)
    repaidAmount = models.IntegerField(default=0)
    monthsPaid = models.IntegerField(default=0)
    address = models.CharField(default="", max_length=50)
    phone = models.CharField(default="000000000000", max_length=20)
    coordinates = models.CharField(default="", max_length=100)
    agent = models.ForeignKey(Agent, default="" , on_delete=models.CASCADE)