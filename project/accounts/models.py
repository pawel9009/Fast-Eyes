from django.db import models
from django.contrib.auth.models import AbstractUser
from .const import SEX_CHOICES

class User(AbstractUser):
    birth_day =  models.IntegerField(null=True, blank=True)
    sex = models.CharField(choices=SEX_CHOICES,max_length=10, default=None, null=True)
    ailments = models.TextField(null=True, max_length=1000)

    def __str__(self):
        return f"{self.username}"
