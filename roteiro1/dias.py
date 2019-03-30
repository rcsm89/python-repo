dia = int(input())
if(dia > 7) or (dia < 1):
    print("valor invalido")
else:
    if(dia==1):
        print("Domingo")
    if(dia == 2):
        print("Segunda")
    elif(dia == 3):
        print("Terça")
    elif(dia == 4):
        print("Quarta")
    elif(dia == 5):
        print("Quinta")
    elif(dia == 6):
        print("Sexta")
    elif(dia == 7):
        print("Sabado")
    