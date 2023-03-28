from accounts.models import User

user = User.objects.all().filter(username='admin')
n = 100
print(user)
dur = [500, 5000, 7000]

pass_ra = [float(q) for q in range(5,101,5)]



for i in range(n):
    print(i)