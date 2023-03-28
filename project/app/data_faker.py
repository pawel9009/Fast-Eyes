from .models import Experiment

n = 100
dur = [500, 5000, 7000]
pas = 25.0
pass_ra = [float(q) for q in range(5,101,5)]

obj = Experiment.objects.create(user_id=1,pass_rate=25.0, samples='sds', duration=500,challenge=False)

for i in range(n):
    print(i)

"""
 user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True)
    pass_rate = models.FloatField(default=0, null=True)
    samples = models.CharField(max_length=256, default=None, null=False)
    duration = models.IntegerField(null=True, default=500)
    challenge = models.BooleanFiel
"""