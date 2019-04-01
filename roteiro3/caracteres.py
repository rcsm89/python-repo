# Questão Caracteres
while (1):
    n = int(input())
    if (n < 1):
        break
    nome = str(input())
    nome = nome[0: n]
    print(nome[::-1])
