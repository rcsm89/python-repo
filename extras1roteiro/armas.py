nac = (input())
oc = input()
qa = int(input())
calibre = int(input())
if(nac =="B"):
    if(oc =="M"):
        print("Liberado")
    elif(oc == "T") or (oc == "O"):
        if(qa <=1) and (calibre <= 22):
            print("Liberado")
        else:
            print("Barrado")
    else:
        if(qa <=2) and (calibre <= 38):
            print("Liberado")
        else:
            print("Barrado")
elif(nac == "E") and (qa > 0):
    print("Barrado")
else:
    print("Liberado")
