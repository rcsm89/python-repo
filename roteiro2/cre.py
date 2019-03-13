menor = 0
mmenor = ""
soma = 0
cont = 0
while True:
    mat = str(input())
    if (mat == "999"):
        break
    cre = float(input())
    soma += cre
    cont += 1
    if (menor < cre):
        menor = cre
        mmenor = mat

print(menor)
print(mmenor)
media = soma/cont
print("%.2f" % media)
