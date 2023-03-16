n= 8000
lista = []
for x in range(20):
    lista.append(round(n))
    print(n)
    if x<=5:
        n-= n*0.12
    elif x<=10:
        n-= n*0.08
    elif x<=15:
        n-= n*0.05
    else:
        n-= n*0.02
    

print(lista)
