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
