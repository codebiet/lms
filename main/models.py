from django.db import models

class Book(models.Model):
    image=models.ImageField(width_field=10,height_field=15)
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication=models.CharField(max_length=100)
    edition=models.CharField(max_length=100)
    description=models.TextField(max_length=500)

class PDF(models.Model):
    image=models.ImageField(width_field=10,height_field=15)
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication=models.CharField(max_length=100)
    edition=models.CharField(max_length=100)
    description=models.TextField(max_length=500)