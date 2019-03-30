primeiro = (int(input()))
segundo = (int(input()))
terceiro = (int(input()))

if (terceiro < segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

if (segundo < primeiro):
    aux = segundo
    segundo = primeiro
    primeiro = aux

if (terceiro < segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

print(primeiro)
print(segundo)
print(terceiro)
