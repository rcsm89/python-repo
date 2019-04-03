n = int(input())
for i in range(n):
    nome = input()
    nomer = ""
    for i in range(1, len(nome)+1):
        nomer += nome[-i]
    print(nomer)
