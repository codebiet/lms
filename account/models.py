from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from multiselectfield import MultiSelectField
import datetime


class MyAccountManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('User must have an email address.')
        #if not username:
        #    raise ValueError('User must have a username.')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using= self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self.db)
        return user

def get_profile_image_filepath(self):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "main\static\main\img\bks.jpg"

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    roll_no = models.CharField(max_length=11)
    branch = models.CharField(max_length=3, choices=(('cse','CSE'), ('it','IT'), ('ece','ECE'), ('ee','EE'), ('me','ME'), ('ce','CE'), ('che','CHE'),))
    year = models.CharField(max_length=1, choices=(('1','I'), ('2','II'), ('3','III'), ('4','IV'),))
    AOI = (
        ('1','WebDev'), 
        ('2','AppDev'), 
        ('3','ML'),
        ('4','AI'), 
        ('5','Electronics'), 
        ('6', 'Electrical'),
    )
    areas_of_interest = MultiSelectField(choices= AOI, min_choices=2)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add =True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now =True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to =get_profile_image_filepath , null=True, blank=True, default= get_default_profile_image)
    hide_email = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

