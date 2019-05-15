def mdc(a,d):
    resto = a%d
    if(resto == 0):
        return d
    else:
        return mdc(d,resto)


n = int(input())
for i in range(n):
    a, d = [int(j) for j in input().split()]
    print("MDC("+str(a)+","+str(d)+") = "+str(mdc(a,d)))

