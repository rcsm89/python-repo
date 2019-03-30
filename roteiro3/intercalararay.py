n = int(input())
l1, l2, lr = [], [], []
for i in range(2):
    for j in range(n):
        a = int(input())
        if i == 0:
            l1.append(a)
        else:
            l2.append(a)
for i in range(n):
    lr.append(l1[i])
    lr.append(l2[i])
print(" ".join(map(str, lr)))
