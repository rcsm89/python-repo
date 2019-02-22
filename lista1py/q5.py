altura = (float(input("Digite sua altura (Entre 1M e 2.8M)")))
peso = (float(input("Digite seu peso (Entre 1Kg e 500Kg)")))
if (altura <1) or (altura > 2.8) or (peso<1 ) or (peso >500):
	print("ERROR: Valores invalidos!")
imc = peso/(altura**2)
print("Seu IMC é de:", imc)
