tabuleiro = [0 for i in range(9)]
def imprimir_tabuleiro():    
    for i in range(3):
        print(tabuleiro[i*3:(i+1)*3])



jogo = True
jogador = 1
while jogo:
    if jogador == 1: 
        imprimir_tabuleiro()   
        jogada = int(input("jogador 1, digite a posição da sua jogada (0-8): "))
        if tabuleiro[jogada] == 0 or tabuleiro[jogada] == 2:
             tabuleiro[jogada] = 1
             jogador = 2
        else:
            print("Posição já ocupada, tente novamente.")
            continue

    # Verificar se o jogador venceu
    if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == 1 or
        tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == 1 or
        tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == 1 or
        tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == 1 or
        tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == 1 or
        tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == 1 or
        tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == 1 or
        tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == 1):
        print("Parabéns! Você venceu! 1")
        jogo = False

    elif jogador == 2:
        imprimir_tabuleiro()
        jogada = int(input("jogador 2, digite a posição da sua jogada (0-8): "))
    if tabuleiro[jogada] == 0 or tabuleiro[jogada] == 1:
        tabuleiro[jogada] = 2
        jogador = 1
    else:
        print("Posição já ocupada, tente novamente.")
        continue
    if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == 1 or
        tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == 1 or
        tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == 1 or
        tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == 1 or
        tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == 1 or
        tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == 1 or
        tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == 1 or
        tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == 1):
        print("Parabéns! Você venceu! 2")
        jogo = False