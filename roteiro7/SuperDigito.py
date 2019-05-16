import time

def superDigito(x):
    if (x<=9):
        return x
    else:
        soma  = sum([int(i) for i in list(str(x))])
        return superDigito(soma)


x, k = [int (i) for i in input().split()]
start = time.time()
print(superDigito(int(str(x)*k)))
print(time.time() - start)
