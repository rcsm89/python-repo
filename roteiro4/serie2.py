n = int(input())
soma = 0
res = ""
ct = 0
for i in range(n):
    if(i%2==0):
        val = (i+1)/(4*(ct+1))
        soma += val
        res+= str(i+1)+"/"+str(4*(ct+1))+" + "
        ct +=1
    else:
        soma += 1
        res+="1 + "
print("%.2f"%soma)
print(res[:-2])
