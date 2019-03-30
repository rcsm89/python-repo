qh = 0
qm = 0
sst = 0
ssh = 0
ms = 0
sms = ""
for i in range(10):
    sal = float(input())
    s = input()
    if (sal > ms):
        ms = sal
        sms = s
    if (s == "m"):
        qh += 1
        ssh += sal
    else:
        qm += 1
    sst += sal
print(qh)
print(qm)
print(round((sst / 10), 2))
print(sms)
print(round((ssh / qh), 1))
