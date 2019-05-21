def cercado(x, y):
    # CIMA, DIREITA, BAIXO, ESQUERDA
    return [x + 1 >= m or mat[x + 1][y] == "#", y + 1 >= n or mat[x][y + 1] == "#", x - 1 < 0 or mat[x - 1][y] == "#",
            y - 1 < 0 or mat[x][y - 1] == "#"]


def caminho(mat, x=0, y=0, pont=0):
    if all(cercado(x, y)):
        pont += dic[mat[x][y]]
        return pont
    else:
        pont += dic[mat[x][y]]
        mat[x][y] = "#"
        ponts = [
            0 if cercado(x, y)[0] else caminho(mat, x + 1, y, pont),  # Cima
            0 if cercado(x, y)[2] else caminho(mat, x - 1, y, pont),  # Baixo
            0 if cercado(x, y)[1] else caminho(mat, x, y + 1, pont),  # Direita
            0 if cercado(x, y)[3] else caminho(mat, x, y - 1, pont)  # Esquerda
        ]

        return max(ponts, key=int)


m, n = [int(i) for i in input().split()]
mat = [list(input()) for j in range(m)]
# 1 = Bronze, 5 = Prata, 10 = Ouro, 50 = Diamante
dic = dict([('b', 1), ('p', 5), ('o', 10), ('d', 50), ('.', 0), ('#', 0)])
print(caminho(mat))
