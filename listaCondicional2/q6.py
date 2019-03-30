n1 = (int(input("Valor 1:")))
n2 = (int(input("Valor 2:")))
n3 = (int(input("Valor 3:")))
ns = [n1, n2, n3]
print("Ordem de leitura: ", n1, n2, n3)
print("Ordem decrescente: ")
if (n1 >= n2):
    if (n2 >= n3):
        print(n1, n2, n3)
    elif (n3 >= n1):
        print(n3, n1, n2)
    else:
        print(n1, n3, n2)
elif(n2 >= n1):
    if(n1 >= n3):
        print(n2, n1, n3)
    elif(n3 >= n2):
        print(n3, n2, n1)
    else:
        print(n2, n1, n3)

