def decParaBin(n):
    if (n < 2):
        return str(n)
    else:
        return decParaBin(n//2) +"\n"+ (str(n%2))


n = int(input())
print(decParaBin(n))
