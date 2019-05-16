import math

def WillyFunc(n, i =0):
    if(i == len(str(n))):
        nn = int(str(n)[-1])
        return nn * (2 if nn%2 == 0 else 3)
    else:
        nn = int(str(n)[i])
        i+=1
        return WillyFunc(n, i) + (nn * (len(str(n)) - (i-1)) * (2 if nn%2 == 0 else 3))



while True:
    a = int(input())
    if(a==0):
        break
    else:
        print(WillyFunc(a))

