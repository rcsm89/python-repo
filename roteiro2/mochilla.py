pt = 0
countl = 0
while True:
    p = int(input())
    if (pt + p >= 18):
        print(countl)
        break
    pt += p
    countl += 1
