num = int(input())
nump = []
for i in range(6, num):
    ##div = []
    soma = 0
    for l in range(1, i):
        if (i % l == 0):
            soma += l
            ##div.append(l)
    if (soma == i):
        ##nump.append(i)
        print(i)
##print()
