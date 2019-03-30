a = 2
while (True):
    a = int(input())
    if (a >= 0 and a < 10):
        continue
    else:
        print("ERROR: Numero invalido!")
