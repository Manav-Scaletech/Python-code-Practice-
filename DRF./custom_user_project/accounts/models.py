from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    phone = models.CharField(max_length=15)

    age = models.IntegerField()

    city = models.CharField(max_length=100)

    REQUIRED_FIELDS = [
        "email",
        "phone",
        "age",
        "city",
    ]