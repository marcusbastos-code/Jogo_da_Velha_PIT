#criação do tabuleiro base do jogo da velha
def criar_tabuleiro(tamanho):
    tabuleiro = []
    for i in range(tamanho):
        linha = []  # vetor: uma linha do tabuleiro
        for j in range(tamanho):
            linha.append(" ")
        tabuleiro.append(linha)
    return tabuleiro