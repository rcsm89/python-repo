while True:
    a = int(input())
    if not any(a == i for i in range(1, 10)):
        print("Insira um n�mero inicial entre 1 e 9")
        continue
    else:
        break
while True:
    b = int(input())
    if not any(b == i for i in range(1, 10)) and any(a == i for i in range(1, 10)):
        print("Insira um n�mero final entre 1 e 9")
        continue
    if (any(a == i for i in range(1, 10))) and any(b == i for i in range(1, 10)):
        break
if (a > b):
    print("Nenhuma tabuada nesse intervalo")
else:
    tabuadatotal = ""
    for j in range(a, b + 1):
        tabuadaj = ""
        for g in range(1, 10):
            linha = str(j) + " x " + str(g) + " = " + str(j * g)
            tabuadaj += linha + "\n"
        print(tabuadaj)
        tabuadatotal += tabuadaj
