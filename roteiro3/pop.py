n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
pos = int(input())
print("[ "+" ".join(map(str, l))+" ]")
if(pos>n):
    print("Nao eh possivel remover o elemento")

else:
    it = l[pos]
    lr = l[:pos]+l[(pos+1):-1]
    print("O item " +str(it)+" serah removido da lista")
    print("[ "+" ".join(map(str,lr))+" ]")

