n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
val = int(input())
if(l!=[]):print("[ "+" ".join(map(str, l))+" ]")
else:print("[ ]")
if(l == [] ):
    print("A lista estah vazia - nao eh possivel remover elemento")
elif(val in l):
    l = l[0:l.index(val)]+l[(l.index(val)+1):]
    print("[ "+" ".join(map(str, l))+" ]")
else:
    print("Nao eh possivel remover o elemento "+str(val))

