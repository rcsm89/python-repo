preco = (float(input("Digite o preco a vista do produto: ")))
meses = (int(input("Em quantos meses voce quer parcelar?")))
if (meses == 3):
    preco *= 1.1
    prest = preco / 3
elif (meses == 5):
    preco *= 1.2
prest = preco / 3
print("Novo preço total:", preco)
print("Valor das",meses," prestações:", "%.2f"%prest)
