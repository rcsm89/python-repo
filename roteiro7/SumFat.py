def fat(a):
    if(a==1):
        return 1
    elif(a == 0):
        return 0
    else:
        return (fat(a-1)*a)


soma = 0
for i in range(5):
    a = int(input())
    if(a%3 == 0):
        soma += fat(a)
print(soma)
