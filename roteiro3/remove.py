n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
val = int(input())
result, result2 = "[ ", "[ "
for i in range(len(l)):
    result += str(l[i]) + " "
result += "]"
print(result)
if(l == [] ):
    print("A lista estah vazia - nao eh possivel remover elemento")
elif(val in l):
    ind = 0
    for j in range(len(l)):
        if l[j] == val:
            ind = j
    l = l[0:ind] + l[(ind + 1):]
    for i in range(len(l)):
        result2 += str(l[i]) + " "
    result2 += "]"
    print(result2)
else:
    print("Nao eh possivel remover o elemento "+str(val))

