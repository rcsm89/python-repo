import math

raio = (float(input("Digite um raio entre 1 e 50: ")))
angulo = (float(input("Digite um angulo (em graus) entre 0.1 e 359: ")))
if(raio>50) or (raio<1) or (angulo>359) or (angulo <0 ):
	print("ERROR: Entrada invalida!")
else:
	comp=(raio*math.pi*angulo)/180
	area = (math.pi*raio**2*angulo)/360
	print("Comprimento:","%.2f" % comp)
	print("Area:","%.2f" % area)
