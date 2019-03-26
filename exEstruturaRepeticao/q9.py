a = 80000
b = 200000
ca = 1
while (a * 1.03 <= b * 1.015):
    a *= 1.03
    b *= 1.015
    ca += 1
print(ca)
