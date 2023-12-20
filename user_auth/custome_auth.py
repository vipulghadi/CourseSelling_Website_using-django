from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date
from django import forms
import uuid 

from django.contrib.auth.backends import BaseBackend
from .models import CustomUser


#-----------------------------------------------------------------------------
class AuthenticationBackend(BaseBackend):
    """
    Authentication Backend
    :To manage the authentication process of user
    """

    def authenticate(self, email, password=None):
        user = CustomUser.objects.get(email=email)
        if user :
            return user
        if user is not None :
            user_password=user.password 
           
            if user_password==str(password):
                return user
               
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None


#--------------------------------------------------------------------------------------------
 
class AccountManager(BaseUserManager):
    
    def create_user(self, email,  password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
     
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)
    



#---------------Absract Base User----------------------------------------
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,null=False)
    username = models.CharField(max_length=150,null=True,blank=True)
    phone= models.CharField(max_length=50,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    is_prime= models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser= models.BooleanField(default=False)
    logged_in_as=models.CharField(max_length=100,null=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["logged_in_as",]
    
    def __str__(self) -> str:
        return self.email

    