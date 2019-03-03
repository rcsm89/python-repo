psnr = (int(input()))
enq = input()
exp = input()
if (psnr >= 80) and (psnr <= 90):
    if (enq == "bom") or (enq == "excelente"):
        if (exp == "bem exposta"):
            print("para imprimir")
        else:
            print("boa")
    else:
        print("marromeno")
elif (psnr >= 50) and (psnr < 80):
    if (enq == "excelente") and (exp == "bem exposta"):
        print("boa")
    else:
        print("marromeno")
elif (psnr < 50) and ((enq == "excelente") and (exp == "bem exposta")):
    print("marromeno")
else:
    print("lixo")
