peso = (float(input()))
altura = (float(input()))
#if (altura <1) or (altura > 2.8) or (peso<1 ) or (peso >500):
#	print("ERROR: Valores invalidos!")
imc = peso/(altura**2)
print("%.2f" % imc)
