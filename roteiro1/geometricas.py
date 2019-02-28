tipo = input()
if(tipo!="Q") and (tipo!="R") and (tipo!="C"):
    print("Nenhuma figura selecionada")
else:
    if(tipo=="Q"):
        val = (float(input()))
        print("%.2f"%(val*val))
        print("%.2f"%(val*4))
    elif(tipo=="R"):
        val = (float(input()))
        val2  = (float(input()))
        print("%.2f"%(val*2+val2*2))
        print("%.2f"%val*val2)
    elif(tipo=="C"):
        val = (float(input()))
        print("%.2f"%(3.14*val**2))
        print("%.2f"%(2*3.14*val))
