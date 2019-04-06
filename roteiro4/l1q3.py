#Questao L1Q3: Falha no codigo
cod = input()
if(cod[6]!="c") and (cod[6]!="b") and (cod[6]!="s"):
    print("Codigo Invalido")
elif (cod[6] == "c"): print("Charmander")
elif (cod[6] == "b"): print("Bulbassauro")
else: print("Squirtle")
