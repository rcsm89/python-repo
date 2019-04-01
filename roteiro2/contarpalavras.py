# Questão: Contar Palavras
nome = str(input())
if (nome.find(" ")):
    print(len(nome.split(" ")))
else:
    print(1)
