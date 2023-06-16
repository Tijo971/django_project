from django.db import models

# Create your models here.

class Category(models.Model):
    cate_name = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=60, null=True, blank=True)
    image = models.ImageField(upload_to="category", null=True, blank=True)

class Products(models.Model):
    p_category = models.CharField(max_length=20, null=True, blank=True)
    prod_name = models.CharField(max_length=20, null=True, blank=True)
    prod_price = models.IntegerField(null=True, blank=True)
    prod_description = models.CharField(max_length=90, null=True, blank=True)
    prod_brand = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to="product", null=True, blank=True)
