nome1 = (str(input("Digite o nome do primeiro produto: ")))
preco1 = (float(input("Digite o preco do primeiro produto: ")))

nome2 = (str(input("Digite o nome do segundo produto: ")))
preco2 = (float(input("Digite o preco do segundo produto: ")))

if (preco1 > 20):
    print(nome1, "tem o preço superior a 20")
elif (preco1 < 10):
    print(nome1, "tem o preço inferior a 10")

if (preco2 > 20):
    print(nome2, "tem o preço superior a 20")
elif (preco1 < 10):
    print(nome2, "tem o preço inferior a 10")
