from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    age =  models.IntegerField()

    def __str__(self):
        return f"{self.username}"
