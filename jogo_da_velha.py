def exibir_tabuleiro(tabuleiro):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(tabuleiro[i][j], "|", end=" ")
        print("\n-------------")

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
    # Verificar colunas
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] == jogador:
            return True
    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        print("É a vez do jogador", jogador_atual)

        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            if verificar_vitoria(tabuleiro, jogador_atual):
                print("O jogador", jogador_atual, "venceu!")
                break
            elif " " not in tabuleiro[0] and " " not in tabuleiro[1] and " " not in tabuleiro[2]:
                print("Empate!")
                break
            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Essa posição já está ocupada. Tente novamente.")

jogar()
