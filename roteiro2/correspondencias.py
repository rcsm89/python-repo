dm = 0
sum = 0
for i in range(7):
    c = int(input())
    if (c >= 100):
        dm += 1
    sum += c
print(dm)
print(sum // 7)
