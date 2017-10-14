from django.db import models

# Create your models here.

# class Greeting(models.Model):
#     when = models.DateTimeField('date created', auto_now_add=True)

class Product(models.Model):
	img_path = models.CharField(max_length=100)
	product_name = models.CharField(max_length=100)