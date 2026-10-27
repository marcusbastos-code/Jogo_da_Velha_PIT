if sequencia_atual > maior_sequencia:
            maior_sequencia = sequencia_atual

    print("Maior sequência de vitórias consecutivas do mesmo jogador: "
          + str(maior_sequencia))


def jogar_partida(jogador1, jogador2, placar, historico):
    tabuleiro = criar_tabuleiro(3)
    casas_usadas = set()
    jogadores = (jogador1, jogador2)
    vez = 0
    resultado = ""

    while resultado == "":
        mostrar_tabuleiro(tabuleiro)
        jogador_atual = jogadores[vez]
        nome = jogador_atual[0]
        simbolo = jogador_atual[1]

        print("\nVez de " + nome + " (" + simbolo + ")")

        while True:
            linha = ler_numero("Escolha a linha (1 a 3): ", 1, 3) - 1
            coluna = ler_numero("Escolha a coluna (1 a 3): ", 1, 3) - 1
            posicao = (linha, coluna)

            if posicao in casas_usadas:
                print("Essa casa já está ocupada! Escolha outra.")
            else:
                casas_usadas.add(posicao)
                tabuleiro[linha][coluna] = simbolo
                break

        if verificar_vitoria(tabuleiro, simbolo):
            mostrar_tabuleiro(tabuleiro)
            print("\nParabéns, " + nome + "! Você venceu!")
            resultado = nome
            if simbolo == "X":
                placar["X"] = placar["X"] + 1
            else:
                placar["O"] = placar["O"] + 1
        elif contar_vazias(tabuleiro) == 0:
            mostrar_tabuleiro(tabuleiro)
            print("\nA partida terminou empatada!")
            placar["Empates"] = placar["Empates"] + 1
            resultado = "Empate"
        else:
            if vez == 0:
                vez = 1
            else:
                vez = 0

    historico.append(resultado)
    mostrar_placar(placar, jogador1, jogador2)


def menu():
    print("===== JOGO DA VELHA =====")
    nome1 = input("Nome do jogador 1 (X): ").strip()
    nome2 = input("Nome do jogador 2 (O): ").strip()

    if nome1 == "":
        nome1 = "Jogador 1"
    if nome2 == "":
        nome2 = "Jogador 2"

    jogador1 = (nome1, "X")
    jogador2 = (nome2, "O")

    # Dicionário com as vitórias e os empates.
    placar = {"X": 0, "O": 0, "Empates": 0}

    # Vetor que guarda o resultado de cada partida.
    historico = []

    # Conjunto de símbolos válidos.
    simbolos_validos = {"X", "O"}

    opcao = ""
    while opcao != "4":
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Jogar")
        print("2 - Ver placar")
        print("3 - Ver histórico")
        print("4 - Sair e ver estatísticas")

        opcao = input("Escolha uma opção: ").strip().upper()

        if opcao == "1":
            if jogador1[1] in simbolos_validos and jogador2[1] in simbolos_validos:
                jogar_partida(jogador1, jogador2, placar, historico)
        elif opcao == "2":
            mostrar_placar(placar, jogador1, jogador2)
        elif opcao == "3":
            mostrar_historico(historico)
        elif opcao == "4":
            mostrar_estatisticas(placar, historico, jogador1, jogador2)
            print("Obrigado por jogar!")
        else:
            print("Opção inválida! Escolha de 1 a 4.")


menu()