
r1 = float(input())
r2 = float(input())
pi = 3.14

a1 = pi * (r1**2)
a2 = pi * (r2**2)
if(a1>a2):
    print("Primeiro circulo")
elif(a1<a2):
    print("Segundo círculo")
else:
    print("Iguais")