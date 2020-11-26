from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from account.models import Account


class CreateUserForm(UserCreationForm):
    roll_no = forms.CharField(max_length=11)
    branch = forms.ChoiceField(choices=(('cse','CSE'), ('it','IT'), ('ece','ECE'), ('ee','EE'), ('me','ME'), ('ce','CE'), ('che','CHE')))
    year = forms.ChoiceField(choices = (('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV')))
    AOI = (
        ('1','WebDev'), 
        ('2','AppDev'), 
        ('3','ML'),
        ('4','AI'), 
        ('5','Electronics'), 
        ('6', 'Electrical'),
    )
    areas_of_interest = MultiSelectField(choices=AOI)
    class Meta:
        model = User
        fields = {'first_name','last_name','roll_no', 'branch', 'year', 'areas_of_interest', 'username','email', 'password1', 'password2'}