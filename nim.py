def computador_escolhe_jogada(n, m):
    resto = 0
    jogada = 0
    
    resto = n%(m+1)
    if (resto <= m):
        jogada = resto
    else:
        jogada = m
    print("Computador jogou!")
    return (jogada)

def usuario_escolhe_jogada(n, m):
    valido = 0
    
    while (not valido):
        jogada = int(input("Digite sua jogada, deve ser inteiro positivo não-nulo menor ou igual a m = {}: ".format(m)))
        if (0 < jogada <= m):
            valido = 1
        if (not valido):
            print("Jogada inválida!")
    return (jogada)

def partida():

    n = 0
    m = 0
    n_atual = 0
    jogador = 0
    jogada = 0
    
    while n <= 0:
        n = int(input("Digite um número n total de peças (inteiro positivo não-nulo): "))
    while m <= 0:
        m = int(input("Digite um número m máximo de peças a ser retirado por jogada (inteiro positivo não-nulo): "))

    if (n_atual % (m + 1) == 0):
        jogador = 2
        print("Você começa!")
    else:
        jogador = 1 #1 eh o pc, 2 eh o user
        print("Computador começa!")

    n_atual = n
    while (n_atual > 0):
        if (jogador == 1):
            jogada = computador_escolhe_jogada(n_atual, m)
            jogador = 2
        else:
            jogada = usuario_escolhe_jogada(n_atual, m)
            jogador = 1
        n_atual -= jogada
        print("Peças removidas = {}, Peças restantes {}".format(jogada, n_atual))
    if (jogador == 2):
        print("O computador ganhou!")
        return (1)
    else:
        print("Você ganhou!")
        return (2)

def campeonato():
    n_partida = 0
    score_pc = 0
    score_user = 0
    ganhador = 0 #se 1 eh pq o pc ganhou, se 2 eh pq o user ganhou

    while (n_partida < 3):
        if (partida() == 1)
            score_pc++
        else
            score_user++
        n_partida++
    print("Placar: Você {} X {} Computador".format(score_user, score_pc))
    if (score_pc > score_user):
        print("Computador ganhou o campeonato!")
    else
        print("Você ganhou o campeonato!")
    print("Fim do campeonato!")






