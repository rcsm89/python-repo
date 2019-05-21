def calcMoedas(nn):
    if (nn == 1):
        return ['C', 'K']
    else:
        moedas = ['C', 'K']
        return [m + i for m in moedas for i in calcMoedas(nn - 1)]

n, d = input().split()
print(len([x for x in calcMoedas(int(n)) if (abs(x.count("C") - x.count("K"))) == int(d)]))
