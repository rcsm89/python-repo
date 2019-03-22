mpreco = 0
mren = 0
cmren = " "
while True:
    nc = input()
    if nc.upper() == "FIM":
        break
    km = int(input())
    val = float(input())
    if (km / val * 2 > mren) and (val * 2 <= 300):
        mren = km / val * 2
        mpreco = val * 2
        cmren = nc.upper()
if (cmren == " "):
    print("SEM DESTINO")
else:
    print(cmren)