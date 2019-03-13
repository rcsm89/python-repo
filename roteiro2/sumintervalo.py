a = int(input())
b = int(input())
menor = a
maior = b
if(a > b):
    maior = a
    menor = b
sum = 0
for i in range(menor, maior + 1):
    if (i > 0):
        sum += i
print(sum)

