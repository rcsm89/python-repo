ei = (str(input()))
pm = (str(input()))
val = (float(input()))
motor = (float(input()))
cambio = (str(input()))
cd = 0
if(ei == "A") and (pm == "G"):
    if(val < 100000): cd +=1
    if(motor >= 1.5): cd +=1
    if(cambio == "A"): cd +=1
    if(cd == 3):
        print("Pode comprar!")
    elif(cd == 2):
        print( "Boa compra.")
    elif(cd == 1):
        print( "Pode ser uma opção.")
    elif(cd == 0):
        print("Recomendo pensar melhor...")
else:
    print("Não compre!")
