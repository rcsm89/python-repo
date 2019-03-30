carnes = input()
if (carnes != "C") and (carnes != "BF") and (carnes != "BS"):
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

    if (cachaca == "S"):
        precoCachaca = (qcachaca * 8) * 2
    if (todinho == "S"):
        precoTodinho = (qtodinho / 2) * 6

    if (carnes == "C"):
        pesoBovino = ((200 * qcachaca) + (200 * qtodinho)) / 1000

        pesoFrango = (100 * qcachaca) / 1000

        pesoSuino = (100 * qcachaca) / 1000

        valorCarne = (32 * pesoBovino) + (18 * pesoFrango) + (15 * pesoSuino)

    elif (carnes == "BF"):
        pesoBovino = ((250 * qcachaca) + (200 * qtodinho)) / 1000
        pesoFrango = (150 * qcachaca) / 1000
        valorCarne = (32 * pesoBovino) + (18 * pesoFrango)
    elif (carnes == "BS"):
        pesoBovino = ((250 * qcachaca) + (200 * qtodinho)) / 1000
        pesoSuino = (150 * qcachaca) / 1000
        valorCarne = (32 * pesoBovino) + (15 * pesoSuino)

    valorTotal = valorCarne + precoTodinho + precoCachaca
    if (pa == "N"):
        valorTotal = valorTotal * 0.98
    print("R$:", "%.2f" % valorTotal)
