sexo = (str(input("Digite seu sexo (M - para masculino e F - para feminino): ")))
altura = (float(input("Digite sua altura: ")))
if (sexo == 'M'):
    pesoIdeal = (72.7 * altura) - 58
    print("Seu peso ideal:", pesoIdeal)
elif (sexo == 'F'):
    pesoIdeal = (62.1 * altura) - 44.7
    print("Seu peso ideal:", "%.2f" % pesoIdeal)
