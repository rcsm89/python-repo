p1 = (int(input("Peso 1: ")))
c1 = (int(input("Comp. 1: ")))
p2 = (int(input("Peso 2: ")))
c2 = (int(input("Comp. 2: ")))
if(p1>=10) and (p1<=100) and (c1 >=10) and (c1<=100) and (c2>=10) and (c2<=100):

    if(p1*c1 == p2*c2):
        print("Gangorra equilibrada")
    elif(p1*c1 > p2* c2):
        print("Gangorra desequilibrada para a esquerda")
    else:
        print("Gangorra desequilibrada para a direita")
else:
    print("Valores invalidos! ")
