def moverFrota(matrix):
    for row in range(len(matrix)):
        for col in range(len(row)):
            if(matrix[row][col] == 1 and matrix[row-1][col+1] == 0) and (row-1 >= 0 and col+1 < len(row)):
                matrix[row][col], matrix[row] = 0, 1
                

            

def jogarBomba(matrix, x,, y):





n, m = [int (i) for i in str(input()).split()]
k = int(input())
malha_espacial = [[0 for j in range(m)] for i in range(n)]
#coordenadas iniciais da nave
for i in range(k):
    x, y = [int (l) for l in str(input().split())]
    malha_espacial[x][y] = 1
#h = num de ataques
#b = num de bombas por ataque
h, b = [int(j) for j in str(input().split())]
#printar matrix
for j in range(h):
    for l in range(b):
        x, y = [int(h) for h in str(input()).split()]
        matrix = jogarBomba(matrix, x, y)
    matrix = moverFrota(matrix)
    #printar matrix
