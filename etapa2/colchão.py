altp = int(input())
largport = int(input())
while (1):
    lc = int(input())
    if (lc == 0): break
    cc = int(input())
    ac = int(input())
    if (ac <= 0) or (cc <= 0):
        print("DIMENSOES INVALIDAS")
        continue
    if (altp >= ac) and ((largport >= lc) or (largport >= cc)):
        print("PASSA")
    elif (altp >= lc) and ((largport >= ac) or (largport >= cc)):
        print("PASSA")
    elif (altp >= cc) and ((largport >= ac) or (largport >= lc)):
        print("PASSA")
    else:
        print("EMPERRA ")
