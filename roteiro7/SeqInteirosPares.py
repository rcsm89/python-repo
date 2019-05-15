def paresAteMim(num, res = ""):
    if num == 0:
        #Crescente
        return (res+"0\n")
        #Decrescente
        #return ("0\n"+res)
    if(((num)%2) == 0):
        #Crescente
        #res = str(num)+"\n" + res
        #Decrescente
        res = res + str(num)+"\n"
        return paresAteMim(num-1, res)
    else:
        return paresAteMim(num-1, res)

a = int(input())
print(paresAteMim(a))
