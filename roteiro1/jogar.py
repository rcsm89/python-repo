idade = (int(input()))
jogo = input()
if (idade > 130) or (idade < 0):
    print("Idade invalida.")

elif (jogo != "azar") and (jogo != "mmorpg") and (jogo != "casual") and (jogo != "moba"):
    print("Jogo invalido.")
else:
    if (jogo == "azar"):
        if (idade >= 21):
            print("Pode entrar!")
        else:
            print("Volte daqui há alguns anos.")

    elif (jogo == "moba"):
        if (idade >= 10):
            print("Pode entrar!")
        else:
            print("Volte daqui há alguns anos.")

    elif (jogo == "casual"):
            print("Pode entrar!")

    elif (jogo == "mmorpg"):
        if (idade >= 14):
            print("Pode entrar!")
        else:
            print("Volte daqui há alguns anos.")
