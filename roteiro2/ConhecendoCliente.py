cond = "S"
contVenda = 0
contVendaVista = 0
valVV = 0
totalVendas = 0
valVC = 0
clienteJovem = 0
maiorCompra = 0
while (cond == "S"):
    idade = int(input())
    val = float(input())
    pag = input()
    cond = input()
    if (contVenda == 0):
        clienteJovem = idade
    if (val > maiorCompra):
        maiorCompra = val
    if (pag == "V"):
        valVV += val
        contVendaVista += 1
    elif (pag == "C"):
        valVC += val
    if (idade < clienteJovem):
        clienteJovem = idade
    contVenda += 1
    totalVendas += val
print(round(contVenda, 2))
print(round(valVV, 2))
print(round(valVC, 2))
print(clienteJovem)
print(round(maiorCompra, 2))
media = 0
if (valVV > 0):
    media = valVV / contVendaVista

print(round(media, 2))
