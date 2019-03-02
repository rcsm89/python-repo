nome = input()
if(len(nome)>1):
    print('1 caractere, por favor!')
else:
    nome = nome.upper()
    if(nome=='A')or(nome=='E')or(nome=='I')or(nome=='O')or(nome=='U'):
        print("Eh vogal")
    else:
        print("Nao eh vogal")
