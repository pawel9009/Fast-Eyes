import uuid
from mysite import settings
from django.db import models

from accounts.models import User


# Model for storing the image with the name and the number of correct and incorrect recognitions.
class Image(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    img = models.ImageField(upload_to=settings.MEDIA_ROOT)
    name = models.CharField(max_length=100)
    correct = models.IntegerField(null=True, default=0)
    incorrect = models.IntegerField(null=True, default=0)

    def __str__(self) -> str:
        return f'{self.name} {self.correct} {self.incorrect}'


# Model for storing the experiment for the user. Including date, percentage of accuracy and time.
class Experiment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True)
    pass_rate = models.FloatField(default=0, null=True)
    samples = models.CharField(max_length=256, default=None, null=False)
    duration = models.IntegerField(null=True, default=500)
    challenge = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.id} {self.pass_rate} {self.duration}'
