n = int(input())
for j in range(n):
    nome = input()
    good = False
    while(not good):
        for i in range(len(nome)):
            if(i+1 < len(nome)):
                if(nome[i]==nome[i+1]):
                    nome = nome[0:i] + nome [i+1:]
        if(nome)
