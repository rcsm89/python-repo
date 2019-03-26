qn = int(input())
if qn > 5 or qn <= 0:
    print("Numero de notas invalido.")
else:
    notas = []
    for i in range(1, qn + 1):
        nota = float(input())
        notas.append(nota)
        print("Nota " + str(i) + ": " + str(notas[i - 1]))
    print("Media: " + "%.2f" % (sum(notas) / qn))
