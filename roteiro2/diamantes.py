num = int(input())
diamante = ""
diamantec = ""
qe = 0
for i in range(num):
    if (i == 0):
        qe = 1
        qec = (num * 2) - 1
    else:
        qe += 2
        qec -= 2
    linha = ""
    linhac = ""
    for l in range(i + 1):
        linhac += "."
    for j in range(num - i):
        linha += "."
    for s in range(qec):
        linhac += "*"
    for k in range(qe):
        linha += "*"
    diamante += linha + "\n"
    diamantec += linhac + "\n"
print(diamante[:-1])
print(diamantec[:-1])
