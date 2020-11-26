from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from account.models import Account
from account.admin import AccountAdmin
from django.contrib.auth import get_user_model


class CreateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address.")
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
    password1 = forms.CharField(widget= forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget= forms.PasswordInput)
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'roll_no', 'branch', 'year', 'areas_of_interest', 'password1', 'password2')

    """def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = Account.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email"""

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit = True):
        user = super(CreateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    
