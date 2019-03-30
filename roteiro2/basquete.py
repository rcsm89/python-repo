nomeMp = ""
mp = 0
nomeMep = ""
mep = 0
count = 0
sum = 0

while True:
    nome = str(input())
    if (nome == "sair"):
        break
    pont = int(input())
    if (count == 0):
        mp = pont
        mep = pont
        nomeMep = nome
        nomeMp = nome
    if (pont >= mp):
        mp = pont
        nomeMp = nome
    if (pont <= mep):
        mep = pont
        nomeMep = nome
    count += 1
    sum += pont
if (count == 0):
    print("Nenhum jogador foi registrado.")
else:
    print(nomeMep)
    print(nomeMp)
    media = sum / count
    print("%.2f" % media)
