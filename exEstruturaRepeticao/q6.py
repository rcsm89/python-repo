a = int(input())
b = int(input())
res = a
for i in range(b - 1):
    res *= a
print(res)
