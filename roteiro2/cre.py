menor = 0
mmenor = "999"
soma = 0
cont = 0
while True:
    mat = str(input())
    if (mat == "999"):
        break
    cre = float(input())
    if (cont == 0):
        menor = cre
    soma += cre
    cont += 1
    if (menor >= cre):
        menor = cre
        mmenor = mat

print(mmenor)

media = soma/cont
print("%.2f" % media)
