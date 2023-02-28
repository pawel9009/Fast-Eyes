from django.db import models


class Image(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return super().__str__()
