def pedraPapel(jogada1, jogada2):
    jogada1, jogada2 = map(
        str,
        input(
            "Digitem suas jogadas, Pedra, Papel ou Tesoura? '\nDigite Sair para fechar o programa '\n>>>>>"
        ).split(),
    )
    if jogada1 or jogada2 != "Sair":
        if jogada1 == jogada2:
            "Empate"
        elif jogada1 == "Pedra":
            if jogada2 == "Tesoura":
                print("Jogador 1 venceu!")
            else:
                print("Jogador 2 venceu!")
        elif jogada1 == "Papel":
            if jogada2 == "Pedra":
                print("Jogador 1 venceu!")
            else:
                print("Jogador 2 venceu!")
        elif jogada1 == "Tesoura":
            if jogada2 == "Papel":
                print("Jogador 1 venceu!")
            else:
                print("Jogador 2 venceu!")

        pedraPapel(1, 2)


pedraPapel(1, 2)
