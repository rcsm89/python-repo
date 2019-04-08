n = int(input())
l = []
s = 0
for i in range(n):
    l.append(int(input()))
print(n//2)
for j in range(n//2):
    s+= (l[j]-l[(n-(j+1))])**2
print(s)
