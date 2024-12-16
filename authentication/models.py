from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(max_length=225, unique=True, verbose_name=_("Email Address"))
    first_name= models.CharField(max_length=100, verbose_name=_("First Name"))
    last_name= models.CharField(max_length=100, verbose_name=_("Last Name"))

    USERNAME_FIELD="email"

    REQUIRED_FIELDS=["first_name", "last_name"]  

    objects= UserManager() 

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def tokens(self):
        pass 