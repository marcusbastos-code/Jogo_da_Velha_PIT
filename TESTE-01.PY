# =============================================================
# JOGO DA VELHA NO TERMINAL
# Trabalho da 3ª Avaliação - Lógica, Algoritmos e Programação
# Desafio de lógica escolhido: RANKING DE JOGADORES (Intermediário)
#   -> funções: garantir_registro(), registrar_resultado() e mostrar_ranking()
# Usa apenas o conteúdo permitido (sem import, lambda, try/except,
# list comprehension, classes).
# =============================================================


# ---------- TABULEIRO (matriz) ----------

# Recebe o tamanho e devolve uma matriz (lista de listas) de casas vazias.
def criar_tabuleiro(tamanho):
    tabuleiro = []
    for i in range(tamanho):
        linha = []  # vetor: uma linha do tabuleiro
        for j in range(tamanho):
            linha.append(" ")
        tabuleiro.append(linha)
    return tabuleiro


# Mostra o tabuleiro com os números das linhas e colunas visíveis.
def mostrar_tabuleiro(tab):
    print()
    cabecalho = "    "
    for j in range(len(tab)):
        cabecalho = cabecalho + str(j + 1) + "   "
    print(cabecalho)
    for i in range(len(tab)):  # for aninhado: percorre linhas e colunas
        texto = " " + str(i + 1) + "  "
        for j in range(len(tab[i])):
            texto = texto + tab[i][j]
            if j < len(tab[i]) - 1:
                texto = texto + " | "
        print(texto)
        if i < len(tab) - 1:
            print("   ---+---+---")
    print()


# Conta quantas casas vazias restam (for aninhado). Devolve um inteiro.
def contar_vazias(tab):
    vazias = 0
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == " ":
                vazias = vazias + 1
    return vazias


# Recebe o tabuleiro e o símbolo; devolve True se o símbolo completou
# uma linha, uma coluna ou uma diagonal (tudo com laços, sem if manual).
def verificar_vitoria(tab, simbolo):
    tamanho = len(tab)

    # linhas
    for i in range(tamanho):
        completa = True
        for j in range(tamanho):
            if tab[i][j] != simbolo:
                completa = False
        if completa:
            return True

    # colunas (trocamos o índice que varia)
    for j in range(tamanho):
        completa = True
        for i in range(tamanho):
            if tab[i][j] != simbolo:
                completa = False
        if completa:
            return True

    # diagonal principal
    completa = True
    for k in range(tamanho):
        if tab[k][k] != simbolo:
            completa = False
    if completa:
        return True

    # diagonal secundária
    completa = True
    for k in range(tamanho):
        if tab[k][tamanho - 1 - k] != simbolo:
            completa = False
    if completa:
        return True

    return False


# ---------- LEITURA COM VALIDAÇÃO ----------

# Lê um número entre minimo e maximo; repete até a entrada ser válida.
def ler_numero(mensagem, minimo, maximo):
    while True:
        entrada = input(mensagem).strip()  # tira espaços extras
        if entrada.isdigit():  # só dígitos? (letra/vazio/símbolo = False)
            numero = int(entrada)  # conversão segura
            if numero >= minimo and numero <= maximo:
                return numero
        print("Entrada inválida! Digite de " + str(minimo)
              + " a " + str(maximo) + ".")


# Lê uma resposta S/N padronizada com strip() e upper().
def ler_sim_nao(mensagem):
    validas = {"S", "N"}  # conjunto de respostas válidas
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in validas:
            return resposta
        print("Resposta inválida! Digite S ou N.")


# Lê o nome do jogador (padronizado em maiúsculas, sem espaços extras).
# 'proibidos' é um vetor com nomes que não podem ser repetidos.
def ler_nome(mensagem, proibidos):
    while True:
        nome = input(mensagem).strip().upper()
        if nome == "":
            print("O nome não pode ficar vazio!")
        elif nome in proibidos:
            print("Esse nome já está em uso nesta partida!")
        else:
            return nome


# Lê a jogada (linha e coluna) e só aceita uma casa livre.
# Devolve a posição como tupla (linha, coluna) com índices da matriz.
def ler_jogada(tamanho, casas_usadas):
    while True:
        # o "- 1" transforma a escolha (1 a 3) no índice da matriz (0 a 2)
        linha = ler_numero("Escolha a linha (1 a " + str(tamanho) + "): ",
                           1, tamanho) - 1
        coluna = ler_numero("Escolha a coluna (1 a " + str(tamanho) + "): ",
                            1, tamanho) - 1
        posicao = (linha, coluna)  # tupla com a jogada
        if posicao in casas_usadas:  # consulta rápida no conjunto
            print("Essa casa já está ocupada! Escolha outra.")
        else:
            return posicao


# ---------- RANKING (desafio de lógica) ----------

# Cria o registro do jogador no ranking se ele ainda não existir.
# O ranking é um dicionário de dicionários (como uma tabela de banco de dados).
def garantir_registro(ranking, nome):
    if nome not in ranking:
        ranking[nome] = {"vitorias": 0, "derrotas": 0, "empates": 0}


# Atualiza o ranking ao fim de uma partida.
# 'vencedor' é o nome do vencedor ou "EMPATE".
def registrar_resultado(ranking, nome1, nome2, vencedor):
    if vencedor == "EMPATE":
        ranking[nome1]["empates"] = ranking[nome1]["empates"] + 1
        ranking[nome2]["empates"] = ranking[nome2]["empates"] + 1
    elif vencedor == nome1:
        ranking[nome1]["vitorias"] = ranking[nome1]["vitorias"] + 1
        ranking[nome2]["derrotas"] = ranking[nome2]["derrotas"] + 1
    else:
        ranking[nome2]["vitorias"] = ranking[nome2]["vitorias"] + 1
        ranking[nome1]["derrotas"] = ranking[nome1]["derrotas"] + 1


# Mostra o ranking ordenado pelo número de vitórias (maior primeiro).
def mostrar_ranking(ranking):
    print("\n===== RANKING DE JOGADORES =====")
    if len(ranking) == 0:
        print("Ainda não há jogadores no ranking.")
        return
    lista = []  # vetor de tuplas (vitorias, nome)
    for nome in ranking:
        lista.append((ranking[nome]["vitorias"], nome))
    lista.sort()     # ordena do menor para o maior número de vitórias
    lista.reverse()  # inverte: maior número de vitórias primeiro
    for i in range(len(lista)):
        nome = lista[i][1]
        print(str(i + 1) + "º " + nome
              + " - Vitórias: " + str(ranking[nome]["vitorias"])
              + " | Derrotas: " + str(ranking[nome]["derrotas"])
              + " | Empates: " + str(ranking[nome]["empates"]))


# ---------- PLACAR E HISTÓRICO ----------

# Mostra o placar acumulado (dicionário) com porcentagens.
def mostrar_placar(placar):
    total = placar["X"] + placar["O"] + placar["Empates"]
    print("\n===== PLACAR DA SESSÃO =====")
    print("Vitórias de X: " + str(placar["X"]))
    print("Vitórias de O: " + str(placar["O"]))
    print("Empates: " + str(placar["Empates"]))
    if total > 0:
        pct_x = int(placar["X"] * 1000 / total) / 10
        pct_o = int(placar["O"] * 1000 / total) / 10
        print("Aproveitamento de X: " + str(pct_x) + "%")
        print("Aproveitamento de O: " + str(pct_o) + "%")


# Mostra o histórico (vetor) com o resultado de cada partida.
def mostrar_historico(historico):
    print("\n===== HISTÓRICO DE PARTIDAS =====")
    if len(historico) == 0:
        print("Nenhuma partida jogada ainda.")
    for i in range(len(historico)):
        print("Partida " + str(i + 1) + ": " + historico[i])


def mostrar_regras():
    print("\n===== REGRAS DO JOGO DA VELHA =====")
    print("1. O tabuleiro tem 3 linhas e 3 colunas.")
    print("2. Os jogadores se alternam; cada um marca seu símbolo (X ou O)")
    print("   em uma casa vazia, informando a linha e a coluna.")
    print("3. Vence quem completar primeiro uma linha, uma coluna ou")
    print("   uma diagonal com o seu símbolo.")
    print("4. Se o tabuleiro encher sem vencedor, a partida empata.")


# ---------- PARTIDA ----------

# Joga uma partida completa. Recebe as tuplas (nome, símbolo) dos dois
# jogadores e devolve a tupla do vencedor, ou ("EMPATE", "-") se empatar.
def jogar_partida(jogador1, jogador2):
    tab = criar_tabuleiro(3)       # tabuleiro novo a cada partida
    casas_usadas = set()           # conjunto: posições já jogadas
    jogadas = []                   # vetor: lista das jogadas feitas
    vez_do_primeiro = True         # booleano: de quem é a vez

    while True:
        mostrar_tabuleiro(tab)
        if vez_do_primeiro:
            atual = jogador1
        else:
            atual = jogador2
        print("Vez de " + atual[0] + " (" + atual[1] + ")")

        posicao = ler_jogada(len(tab), casas_usadas)
        linha = posicao[0]
        coluna = posicao[1]
        tab[linha][coluna] = atual[1]
        casas_usadas.add(posicao)
        jogadas.append(posicao)

        if verificar_vitoria(tab, atual[1]):
            mostrar_tabuleiro(tab)
            print("Parabéns, " + atual[0] + " venceu a partida!")
            return atual
        if contar_vazias(tab) == 0:
            mostrar_tabuleiro(tab)
            print("Deu empate!")
            return ("EMPATE", "-")

        vez_do_primeiro = not vez_do_primeiro


# ---------- PROGRAMA PRINCIPAL ----------

def main():
    placar = {"X": 0, "O": 0, "Empates": 0}  # dicionário: placar acumulado
    historico = []                           # vetor: resultado de cada partida
    ranking = {}                             # dicionário de registros

    print("=== JOGO DA VELHA ===")
    while True:
        print("\n----- MENU -----")
        print("1 - Jogar")
        print("2 - Ver regras")
        print("3 - Ver placar")
        print("4 - Ver ranking")
        print("5 - Ver histórico")
        print("0 - Sair")
        opcao = ler_numero("Escolha uma opção: ", 0, 5)

        if opcao == 1:
            nome1 = ler_nome("Nome do jogador 1 (X): ", [])
            nome2 = ler_nome("Nome do jogador 2 (O): ", [nome1])
            jogador1 = (nome1, "X")  # tupla: dados fixos do jogador
            jogador2 = (nome2, "O")
            garantir_registro(ranking, nome1)
            garantir_registro(ranking, nome2)

            jogando = True
            while jogando:
                vencedor = jogar_partida(jogador1, jogador2)

                if vencedor[0] == "EMPATE":
                    placar["Empates"] = placar["Empates"] + 1
                else:
                    placar[vencedor[1]] = placar[vencedor[1]] + 1
                historico.append(vencedor[0])
                registrar_resultado(ranking, nome1, nome2, vencedor[0])

                mostrar_placar(placar)
                mostrar_ranking(ranking)

                resposta = ler_sim_nao("\nJogar novamente? (S/N): ")
                if resposta == "N":
                    jogando = False
        elif opcao == 2:
            mostrar_regras()
        elif opcao == 3:
            mostrar_placar(placar)
        elif opcao == 4:
            mostrar_ranking(ranking)
        elif opcao == 5:
            mostrar_historico(historico)
        else:
            mostrar_placar(placar)
            mostrar_ranking(ranking)
            print("\nAté a próxima!")
            break


main()