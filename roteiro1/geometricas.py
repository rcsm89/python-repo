tipo = input()
if(tipo!="Q") and (tipo!="R") and (tipo!="C"):
    print("Nenhuma figura selecionada")
else:
    val = (float(input()))
    if(tipo=="Q"):
        print("%.2f"%(val*val))
        print("%.2f"%(val*4))
    elif(tipo=="R"):
        val2  = (float(input()))
        print("%.2f"%(val*2+val2*2))
        print("%.2f"%(val*val2))
    elif(tipo=="C"):
        print("%.2f"%(3.14*val**2))
        print("%.2f"%(2*3.14*val))
