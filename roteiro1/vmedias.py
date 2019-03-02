n1 = (int(input()))
n2 = (int(input()))
n3 = (int(input()))
p1 = (int(input()))
p2 = (int(input()))
p3 = (int(input()))
mediaa = (n1 + n2 + n3) / 3
mediap = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3)
mediah = 3 / (1 / n1 + 1 / n2 + 1 / n3);
print("a:","%.1f" % mediaa)
print("p:","%.1f" % mediap)
print("h:","%.1f" % mediah)

