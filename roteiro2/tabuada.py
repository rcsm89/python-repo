a = int(input())
b = int(input())
while True:
    if not any(a == i for i in range(10)):
        print("Insira um número inicial entre 1 e 9")
        a = int(input())
    if not any(b == i for i in range(10)):
        print("Insira um número final entre 1 e 9")
        a = int(input())
    if (any(a == i for i in range(9))) and any(b == i for i in range(9)):
        break

# else:
#   tabuada = ""
#  for j in range(a, b + 1):
#     for g in range(1, 10):
#        linha = str(j) + " x " + str(g) + " = " + str(j * g)
#       tabuada += linha + "\n"
#  tabuada += "\n"
# print(tabuada)
