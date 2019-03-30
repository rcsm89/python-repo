res = ""
while True:
    n = int(input())
    if (n == -1):
        break
    divs = 0
    for i in range(1, n):
        if (n % i == 0):
            divs += 1
        if (divs > 1):
            break
    if (divs == 1):
        print("1")
    else:
        print("0")
