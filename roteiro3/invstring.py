n = 1
while (n > 0):
    n = int(input())
    nome = " " * n
    for i in range(n):
        nome = nome[:i] + input() + nome[i + 1:]
    print(nome)
