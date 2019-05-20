def superDigito(x):
    if (x<=9):
        return x
    else:
        soma  = sum([int(i) for i in list(str(x))])
        return superDigito(soma)


x, k = input().split()
print(superDigito(int(x*k)))
