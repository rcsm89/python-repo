def fat(n):
    if (n <= 1):
        return 1
    else:
        return n * fat(n - 1)


a = 0
while (True):
    a = int(input())
    if (a <= -1):
        break
    print(fat(a))
