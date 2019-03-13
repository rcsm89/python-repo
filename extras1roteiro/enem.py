sem = str(input())
# CLD, CVC, CSC, NCC
encejab = str(input())
# s ou n
nenceja = int(input())
te = str(input())
renda = float(input())
if (sem == "CVC"):
    if (te == "PUB"):
        print("Voce terah direito a isencao")
    else:
        print("Infelizmente voce nao tem direito a isencao")
elif (sem == "CLD"):
    if (te == "PUB") or (te == "PCB") or (te == "PPB"):
        if (renda <= 1431):
            print("Voce terah direito a isencao")
        else:
            print("Infelizmente voce nao tem direito a isencao")
    else:
        print("Infelizmente voce nao tem direito a isencao")
elif (sem == "CSC") or (sem == "NCC"):
    if (te == "PSB") or (te == "PPS") or (te == "NFE"):
        print("Infelizmente voce nao tem direito a isencao")
elif (encejab == "s") and ((sem == "CSC") or (sem =="CLD") or (sem =="CVC") or (sem == "NCC")):
    if (nenceja >= 400):
        print("Voce terah direito a isencao")
    else:
        print("Infelizmente voce nao tem direito a isencao")
else:
    print ("Informacao sobre ensino medio invalida")
