def criar_tabuleiro(tamanho):
    tabuleiro = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(' ')
        tabuleiro.append(linha)
    return tabuleiro

tabuleiro = criar_tabuleiro(3)
print(tabuleiro)

def criar_tabuleiro(tabuleiro):
        print()
        cabecalho = "  "
        for j in range(len(tabuleiro)):
            cabecalho = cabecalho + str(j + 1) + " "
            print(cabecalho)