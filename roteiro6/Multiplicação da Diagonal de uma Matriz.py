k, mat = int(input()), []
for i in range(4):
    row = []
    for j in range(4):
        val = int(input())
        row.append(val if (i!=j) else val*k)
    mat.append(row)
print('\n'.join([' '.join([str(item) for item in row])
      for row in mat]))

