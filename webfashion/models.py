from django.db import models

# Create your models here.

class UserDB(models.Model):
    usernme = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    phnumber = models.IntegerField(null=True, blank=True)
    Password = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to="Profile", null=True, blank=True) 


class CartDB(models.Model):
    Username = models.CharField(max_length=20, null=True, blank=True)
    pro_name = models.CharField(max_length=20, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    colour = models.CharField(max_length=20, null=True, blank=True)
    size = models.CharField(max_length=20, null=True, blank=True)



class Checkout(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    State = models.CharField(max_length=20, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    c_name = models.CharField(max_length=20, null=True, blank=True)
    c_number = models.IntegerField(null=True, blank=True)
    exp_month = models.CharField(max_length=20, null=True, blank=True)
    exp_yer = models.IntegerField(null=True, blank=True)
    cvv = models.IntegerField(null=True, blank=True)

