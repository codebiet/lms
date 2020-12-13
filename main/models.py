from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from multiselectfield import MultiSelectField
from account.models import Account
from datetime import timedelta
from django.utils import timezone
import datetime

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class book(models.Model):
    image=models.ImageField(upload_to='book_images/')
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication=models.CharField(max_length=100)
    edition=models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    description=models.TextField(max_length=500)
    

    def __str__(self):
        return self.name

class pdf(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    image=models.ImageField(upload_to='pdf_images/')
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication=models.CharField(max_length=100)
    edition=models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    description=models.TextField(max_length=500)
    

    def __str__(self):
        return self.name

class issued_book(models.Model):
    STATUS = (('Pending' ,'Pending'), ('Issued', 'Issued'),)
    account = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    book = models.ForeignKey(book, null=True, on_delete=models.SET_NULL)
    date_issued = models.DateField(auto_now_add=True, null=True)
    last_date = models.DateField(default= timezone.now().date() + timedelta(days=90))
    status = models.CharField(default= STATUS[0], null=True, choices=STATUS, max_length=40)

