dia  = input()
preco = (float(input()))
op = (input())
nome = input()
if(dia == "seg") or (dia=="ter") or (dia=="qua"):
	if(op=="ouro"):
		preco = preco/2
	else:
		preco = preco*2
elif(dia=="qui")or(dia=="sex")and(preco>=10)and(preco<=100):
	preco = preco/3
elif(dia=="sab")and(op=="prata"):
	preco = preco*3
else:
	preco = preco*2

print("O preco do produto", nome,"no dia",dia,"eh", "%.2f"%preco)
