#Questão: Inverter com 4 algarismos
a = int(input())
b = list(reversed([int(i) for i in str(a)]))
print(''.join(map(str, b)))
