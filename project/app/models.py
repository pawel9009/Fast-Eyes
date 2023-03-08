import uuid
import datetime
from django.db import models
from accounts.models import User

from mysite import settings


class Image(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    img = models.ImageField(upload_to=settings.MEDIA_ROOT)
    name = models.CharField(max_length=100)
    correct = models.IntegerField(null=True, default=0)
    incorrect = models.IntegerField(null=True ,default=0)
    


    def __str__(self) -> str:

        return f'{self.name} {self.uuid}'
    

class Experiment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date = models.DateField(default=datetime.datetime.now)
    pass_rate = models.FloatField(default=0, null=True)
    samples = models.CharField(max_length=256, default=None, null=False)

    def __str__(self) -> str:
        return f'{self.id} {self.user_id} {self.date}'





