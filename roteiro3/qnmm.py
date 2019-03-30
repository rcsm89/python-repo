n = int(input())
notas = []
for i in range(n):
    nota = int(input())
    notas.append(nota)
media = sum(notas) / n
print("%.2f" % media)
maiores = sum(j >= media * 1.1 for j in notas)
menores = sum(j <= media * 0.9 for j in notas)
print(maiores)
print(menores)
