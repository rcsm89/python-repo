tl1 = int(input())
if not (tl1 > 0):
    print("Erro - A lista deve ter pelo menos 1 elemento.")
else:
    lr = []
    for i in range(tl1):
        a = int(input())
        lr.append(a)
    tl2 = int(input())
    if not (tl2 > 0):
        print("Erro - A lista deve ter pelo menos 1 elemento.")
    else:
        for i in range(tl2):
            a = int(input())
            lr.append(a)
        print(' '.join(str(val) for val in lr))
