ent = str(input()).split()
n, m, o = int(ent[0]), int(ent[1]), int(ent[2])
m1, m2, mr = [], [], [[0 for i in range(o)] for j in range(o)]
for i in range(n):
    row = [int(j) for j in str(input()).split()]
    m1.append(row)
for j in range(m):
    row = [int(i) for i in str(input()).split()]
    m2.append(row)
res = ""

for k in range(o):
    for l in range(o):
        print(k, l)
        mr[k][l] += m1[k][l]*m2[l][k]

for x in mr:
    print(*x, sep=" ")

