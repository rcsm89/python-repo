mv = 0
ma = 0
cont = 0
sumvel = 0
while(True):
    controle = (input()).upper()
    if(controle!="S"):
        break
    ano = int(input())
    vel = float(input())
    cont+=1
    sumvel+= vel
    if(vel > mv):
        mv = vel
    if(ano>ma):
        ma = ano
if(cont!=0):
    print("%.2f"%mv)
    print(ma)
    media = sumvel/cont
    print("%.2f"%media)
else:
    print("zero")

