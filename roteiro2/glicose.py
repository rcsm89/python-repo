g = 1
cont = 0
soma = 0
while (True):
    g = int(input())
    if(g == 0):
        break
    cont += 1
    soma += g
media = soma/cont
if(media<110):
    print("Glicose Normal")
elif(media >= 200):
    print("Glicose Muito Alta")
else:
    print("Glicose Alterada")

