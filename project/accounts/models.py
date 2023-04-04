from django.contrib.auth.models import AbstractUser
from django.db import models

from .const import SEX_CHOICES


class User(AbstractUser):
    birth_year = models.IntegerField(null=True, blank=True, choices=[(i, i) for i in range(1900, 2020, 1)])
    sex = models.CharField(choices=SEX_CHOICES, max_length=10, default='')
    ailments = models.TextField(default=None, max_length=2000, null=True, blank=True)

    def __str__(self):
        return f"{self.username}"
