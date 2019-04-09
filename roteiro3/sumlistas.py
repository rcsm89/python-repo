tl1 = int(input())
if (tl1 <= 0):
    print("Erro - A lista deve ter pelo menos 1 elemento.")
else:
    lr, res = [], ""
    for i in range(tl1):
        a = int(input())
        lr.append(a)
        res += str(a)+" "
    tl2 = int(input())
    if (tl2 == 0):
        print("Erro - A lista deve ter pelo menos 1 elemento.")
    else:
        for i in range(tl2):
            a = int(input())
            res += str(a)+" "
            lr.append(a)
        print(res[:-1])
