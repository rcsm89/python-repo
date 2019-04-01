num = int(input())
txt = ""
linha = ""
for i in range(1, num + 1):
    linha += str(i) + " "
    txt += linha[:-1] + "\n"
txt = txt[:-1]
print(txt)
