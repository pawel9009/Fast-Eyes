import uuid

from django.db import models

from mysite import settings


class Image(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    img = models.ImageField(upload_to=settings.MEDIA_ROOT)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:

        return f'{self.name} {self.uuid}'
