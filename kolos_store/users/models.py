# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
