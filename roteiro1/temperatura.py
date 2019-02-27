ti = input()
val = (float(input()))
if (ti == "C"):
    if (val < -273):
        print("Valor de temperatura abaixo do minimo")
    else:
        fa = 1.8*val + 32
        kel = val + 273.15
        print("%.2f"%fa, "F" )
        print("%.2f"%kel,"K")

elif (ti == "K"):
    if (val < 0):
        print("Valor de temperatura abaixo do minimo")
    else:
        cel = val - 273.15
        fa = (val - 273.15)*1.8+(32)
        print("%.2f"%cel, "C" )
        print("%.2f"%fa, "F" )

elif (ti == "F"):
    if(val < -459.67):
        print("Valor de temperatura abaixo do minimo")
    else:
        cel  = (val - 32)/1.8
        kel = (val +459.67)/1.8
        print("%.2f"%cel, "C" )
        print("%.2f"%kel,"K")



