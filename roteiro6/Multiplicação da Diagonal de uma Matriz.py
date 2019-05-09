k, mat = int(input()), [[],[],[],[]]
for i in range(4):
    for j in range(4):
        val = int(input())
        mat[i].append(val)
res = ""
for p in range(4):
    for v in range(4):
        res += str(mat[v][p]*k if p==v else mat[v][p] )+" "
    res = res+"\n"
print(res[:-1])
