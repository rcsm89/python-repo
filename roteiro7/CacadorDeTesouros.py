def cercado(x, y):
    # BAIXO, DIREITA, CIMA, ESQUERDA
    return [x + 1 >= m or mat[x + 1][y] == "#", y + 1 >= n or mat[x][y + 1] == "#", x - 1 < 0 or mat[x - 1][y] == "#",
            y - 1 < 0 or mat[x][y - 1] == "#"]


def caminho(x=0, y=0, pont=0):
    ca = mat[x][y]
    if all(cercado(x, y)) or ca == '#':
        pont += dic[mat[x][y]]
        return pont
    else:
        pont += dic[ca]
        mat[x][y] = "#"
        pm = max([
            0 if x+1==m or mat[x+1][y] == "#" else caminho(x + 1, y, pont),  # Baixo
            0 if x-1<0 or mat[x-1][y] == "#" else caminho(x - 1, y, pont),  # Cima
            0 if y+1==n or mat[x][y+1] == "#" else caminho(x, y + 1, pont),  # Direita
            0 if y-1<0 or mat[x][y-1] == "#" else caminho(x, y - 1, pont)  # Esquerda
        ], key=int)
        mat[x][y] = ca
        return pm 


m, n = [int(i) for i in input().split()]
mat = [list(input()) for j in range(m)]
# 1 = Bronze, 5 = Prata, 10 = Ouro, 50 = Diamante
dic = dict([('b', 1), ('p', 5), ('o', 10), ('d', 50), ('.', 0), ('#', 0)])
print(caminho())
