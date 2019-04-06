#Questão: Mapeamento Genetico
dna = input()
b = input()
mc,indc = 0, 0
if not(b in dna):
    print("ERRO")
else:
    cad = 0
    for i in range(len(dna)):
        if dna[i]==b:
            cad += 1
           # if i+1<len(dna) and dna[i+1] == b:
            #    cad+=1
        else:
            cad = 0
        if(cad>mc):
            mc, indc = cad, i
    print(indc-(mc-1))
    print(mc)
