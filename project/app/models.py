from django.db import models

class Image(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=100)
    

