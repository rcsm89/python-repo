tT = ((input("Digite as taxas de transmissao de video, audio e dados separadas por virgula: ")))
capC = (float(input("Digite a capacidade do canal: ")))
taxas = [float(i) for i in tT.split(",")]
if(len(taxas)!=3):
	print("ERROR: Entrada invalida!")
else:
	print(taxas)
	qmax = (taxas[0]*5.2+taxas[1]*3.4+taxas[2]*1.5)/capC
	print("Quantidade maxima de dados a ser transmitida: ","%.2f" % qmax)

