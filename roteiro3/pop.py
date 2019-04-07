n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
pos = int(input())
result = "[ "
for i in range(len(lista)):
    result += str(lista[i]) + " "
result += "]"
print(result)
if lista == []:
    print("A lista estah vazia - nao eh possivel remover elementos")
elif (lista != []):
    if(pos>n):
        print("Nao eh possivel remover o elemento")
    else:
        it = lista[pos]
        print("O item " + str(it) + " serah removido da lista")
        lista = lista[:pos] + lista[(pos + 1):]
        result2 = "[ "
        for i in range(len(lista)):
            result2 += str(lista[i]) + " "
        result2 += "]"
        print(result2)
