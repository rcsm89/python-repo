n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
pos = int(input())
if(l == []):
    print("[ ]")
    print("A lista estah vazia - nao eh possivel remover elementos")
elif(l!=[]):
    print("[ "+" ".join(map(str, l))+" ]")
    if(pos>n):
        print("Nao eh possivel remover o elemento")
    else:
        it = l[pos]
        lr = l[:pos]+l[(pos+1):]
        print("O item " +str(it)+" serah removido da lista")
        print("[ "+" ".join(map(str,lr))+" ]")
