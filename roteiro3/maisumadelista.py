n = int(input())
if(n<0):
    print("O valor informado para N foi negativo")
elif(n==0):
    print("Lista vazia - O valor de S eh zero")
else:
    l,s= [], 0
    for i in range(n):
        l.append(int(input()))
    if(n%2!=0): l.insert(n//2, 0)
    for j in range((len(l)//2)):
        s+= (l[j]-l[-(j+1)])**2
    print("S = "+str(s))
