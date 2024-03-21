from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=20, unique=True)
    profile_image = models.ImageField(upload_to='profile_image/', blank=True, null=True)
    
    objects = CustomUserManager()    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username