k, mat = int(input()), []
for i in range(4):
    row = []
    for j in range(4):
        val = int(input())
        row.append(val if (i!=j) else val*k)
    mat.append(row)
res = ""
for p in range(4):
    for v in range(4):
        res += str(mat[v][p])+" "
    res = res+"\n"
print(res[:-1])
