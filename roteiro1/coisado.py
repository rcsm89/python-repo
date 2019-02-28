carnes = input()
if(carnes !="C") and (carnes!="BF") and (carnes!="BS"):
    print("Opção inválida.")
else:
    pa = input()
    cachaca = input()
    todinho = input()
    qcachaca = int(input())
    qtodinho = int(input())
    precoCachaca = 0
    precoTodinho = 0
    valorCarne = 0
    if(cachaca=="S"):
        precoCachaca = qcachaca*8*2
    if(todinho=="S"):
        precoTodinho = (qtodinho*6)/2
    if(carnes=="C"):
        pesoBovino = (250 * qcachaca + 200 * qtodinho) / 1000
        pesoFrango = (100 * qcachaca) / 1000
        pesoSuino = (100 * qcachaca) / 1000
        valorCarne = 32 * pesoBovino + 18 * pesoFrango + 15 * pesoSuino
    elif(carnes=="BF"):
        pesoSuino = 0
    else:
        valorCarne = 32*((qcachaca*250)/1000)+15*((qcachaca*150)/1000)+32*((qtodinho*200)/1000)
    valorTotal = valorCarne + precoTodinho + precoCachaca

    print("R$:", "%.2f" % valorTotal)




