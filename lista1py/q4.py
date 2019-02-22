ladoM = (int(input("Digite o lado maior do retangulo: ")))
ladoMen = (int(input("Digite o lado menor do retangulo: ")))
if(ladoM > 1000) or (ladoM <1) or (ladoMen > 1000) or (ladoM < 1):
	print("Error: Os valores precisam estar entre 1 e 1000")
print("A area do retangulo é: ", (ladoM*ladoMen))
