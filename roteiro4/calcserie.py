#Questao: Calcular a serie
n = int(input())
soma = 0
res = ""
for i in range(1, n+1):
    soma += i/(i*3)
    res += str(i)+"/"+str(i*3)+ " + "
print(res[:-3])
print("%.2f"%soma)
