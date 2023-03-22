"""
Test program for generating successive times during the challenge
"""
number = 8000
array = []
for x in range(20):
    array.append(round(number))
    print(number)
    if x <= 5:
        number -= number*0.12
    elif x <= 10:
        number -= number*0.08
    elif x <= 15:
        number -= number*0.05
    else:
        number -= number*0.02

print(array)
