def ContaDigitosPares(num, pares = 0):
    if(num == 0):
        return pares
    if (num%10)%2 == 0:
        pares += 1
        return ContaDigitosPares(num//10, pares)
    else:
        return ContaDigitosPares(num//10, pares)

a = int(input())
print(ContaDigitosPares(a))
