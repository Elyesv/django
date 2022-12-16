from django.db import models

# Create your models here.
class Product(models.Model):
    image_url = models.TextField(max_length=200)
    name = models.TextField(max_length=200)
    stock = models.IntegerField()
    price = models.IntegerField()