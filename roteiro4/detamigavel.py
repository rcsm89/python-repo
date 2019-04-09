#Questão: Detecção amigavel de inteiros
amigaveis = ["0", "1", "2","3","4","5","6","7","8","9","0","O","L"]
while(1):
    amigavel = True
    ent = str(input()).upper()
    if(ent.upper()=="FIM"):
        break
    if("L" in ent):
        ent = ent.replace("L", "1")
    if("O" in ent):
        ent = ent.replace("O", "0")
    for i in range(len(ent)):
        if not (ent[i] in amigaveis):
            amigavel = False
    if(amigavel): print(int(ent))
    else: print("ERRO")
