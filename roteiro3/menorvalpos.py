n = int(input())
aray = list(map(int, str(input()).split(" ")))
# lr = list(map(int, aray))
menor, im = aray[0], 0
for i in range(1, len(aray)):
    if (aray[i] < menor):
        menor = aray[i]
        im = i
print("Menor valor: " + str(menor))
print("Posicao: " + str(im))
