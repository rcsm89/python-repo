def paresAteMim(num, res = ""):
    if num == 0:
        return ("0\n"+res)
    if(((num)%2) == 0):
        res = str(num)+"\n" + res
        return paresAteMim(num-1, res)
    else:
        return paresAteMim(num-1, res)

a = int(input())
print(paresAteMim(a))
