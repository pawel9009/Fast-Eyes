from django.contrib.auth.models import AbstractUser
from django.db import models

from .const import SEX_CHOICES


class User(AbstractUser):
    birth_day = models.IntegerField(null=False, blank=False)
    sex = models.CharField(choices=SEX_CHOICES, max_length=10 )
    ailments = models.TextField(default='', max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.username}"
