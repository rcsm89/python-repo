r = (int(input()))
if(r==1):
    print("Nordeste")
elif(r==2):
    print("Norte")
elif(r==3) or (r==4):
    print("Centro-Oeste")
elif(r>=5) and (r<=9):
    print("Sul")
elif (r>=10) and (r<=15):
    print("Sudeste")