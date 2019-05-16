def SerieMiguelito(n):
    if(n==1):
        return 3
    else:
        return SerieMiguelito(n-1) + (4 if n%2 == 0 else 1)


a = int(input())
print(SerieMiguelito(a))
