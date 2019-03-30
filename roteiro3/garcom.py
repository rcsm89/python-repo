n = int(input())
cq = 0
for i in range(n):
    l, c = map(int, input().split(" "))
    if (l > c):
        cq += c
print(cq)
