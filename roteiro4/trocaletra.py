erros, certos = ['1', '3', '4', '5'], ['i', 'e', 'a', 's']
while (True):
    pal = input()
    res = " " * len(pal)
    for i in range(len(pal)):
        if (pal[i] in erros):
            for j in range(len(erros)):
                if (pal[i] == erros[j]):
                    res = res[0:i] + certos[j] + res[i:]
                    break
        else:
            res = res[0:i] + pal[i] + res[i:]
    res = res.upper()
    res = res[:len(pal)]
    if (res == "FIM") or (res == "SAIR"):
        break
    else:
        print(res)
