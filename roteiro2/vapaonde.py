mpreco = 0
mren = None
cmren = " "
while True:
    nc = input()
    if (nc.upper() == "FIM"):
        break
    km = int(input())
    val = float(input())
    if not mren or ((km / val * 2 > mren) and (val * 2 <= 300)):
        mren = km / val * 2
        mpreco = val * 2
        cmren = nc.upper()

if (cmren == " ") or (mpreco > 300):
    print("SEM DESTINO")
else:
    print(cmren)
