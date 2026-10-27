#criação do tabuleiro base do jogo da velha
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

---------- RANKING (desafio de lógica) ----------

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

