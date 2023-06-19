from django.contrib.auth.models import AbstractUser
from django.db import models

from .const import SEX_CHOICES


class User(AbstractUser):
    
    def __str__(self):
        return f"{self.username}"
