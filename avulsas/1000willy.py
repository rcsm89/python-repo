l = []
c = True
while (c):
    for i in range(1000):
        a = int(input())
        l.append(a)
        if (a < 0):
            break
            c = False
    print(l.count(int(input())))
