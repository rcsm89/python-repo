n = int(input())
res = ""
for i in range(n):
    if (i * (i + 1) * (i + 2)) == n:
        res = str(i) + " * " + str(i + 1) + " * " + str(i + 2) + " = " + str(n)
        break;
if (res == "") or (n == 0):
    print("Falso")
else:
    print(res)
    print("Verdadeiro")
