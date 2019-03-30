p = float(input())
print('Preço do pão: R$' + str(p) + "\nPanificadora Pão de Ontem - Tabela de preços",
      '\n'.join([str(n) + " - R$" + str("%.2f" % (n * p)) for n in range(1, 51)]), sep="\n")
