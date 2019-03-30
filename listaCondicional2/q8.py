freq = (float(input("Digite sua frequencia em porcentagem: ")))
nota = (float(input("Digite sua nota: ")))
if(freq <= 75):
	print("Reprovado por frequencia")
else:
	if(nota <= 3):
		print("Reprovado")
	elif(nota > 3) and (nota < 7):
		print("Prova final")
	else:
		print("Parabens! Aprovado!")
