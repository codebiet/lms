from django.db import models
import datetime

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class book(models.Model):
    image=models.ImageField(upload_to='book_images/')
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication=models.CharField(max_length=100)
    edition=models.CharField(max_length=100)
    description=models.TextField(max_length=500)

class pdf(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    image=models.ImageField(upload_to='pdf_images/')
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication=models.CharField(max_length=100)
    edition=models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    description=models.TextField(max_length=500)




