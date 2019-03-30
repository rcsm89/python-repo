temp = (float(input()))
sec = input()
if(temp >= 37) and (sec=="S"):
    print("Ecames Especiais")
elif(temp>=37):
    print("Exames Basicos")
elif(temp<=37) and (sec=="N"):
    print("Liberado")
elif(temp<=37):
    print("Ecames Básicos")
else:
    print("Erro")