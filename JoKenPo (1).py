import random

quantidadeJogadas = 1
placarJogador1 = 0
placarJogador2 = 0

while quantidadeJogadas >= 1:

    escolhaJogador1 = int(input('Jogador 1 será: 1-Jogador, 2-Computador: '))
    escolhaJogador2 = int(input('Jogador 2 será: 1-Jogador, 2-Computador: '))
    #escolher o tipo de Jogador, humano ou maquina

    if escolhaJogador1 > 2 or escolhaJogador1 <= 0 or escolhaJogador2 > 2 or escolhaJogador2 <= 0:
        print('O valor não é permitido')

    if escolhaJogador1 == 1 and escolhaJogador2 == 1:
        escolhaMao1 = int(input('Escolha sua mão: 1-pedra, 2-papel, 3-tesoura: '))
        escolhaMao2 = int(input('Escolha sua mão: 1-pedra, 2-papel, 3-tesoura: '))
        if escolhaMao1 <= 0 or escolhaMao1 > 3 or escolhaMao2 <= 0 or escolhaMao2 > 3:
            print('Valor não permitido')
        elif escolhaMao1 == escolhaMao2:
            print('Empate')
            placarJogador1 += 1
            placarJogador2 += 1
        elif escolhaMao1 == 1 and escolhaMao2 == 2:
            print('O jogador 2 ganhou!')
            placarJogador2 += 1
        elif escolhaMao1 == 1 and escolhaMao2 == 3:
            print('O jogador 1 ganhou!')
            placarJogador1 += 1
        elif escolhaMao1 == 2 and escolhaMao2 == 1:
            print('O jogador 1 ganhou!')
            placarJogador1 += 1
        elif escolhaMao1 == 2 and escolhaMao2 == 3:
            print('O jogador 2 ganhou!')
            placarJogador2 += 1
        elif escolhaMao1 == 3 and escolhaMao2 == 1:
            print('O jogador 2 ganhou!')
            placarJogador2 += 1
        elif escolhaMao1 == 3 and escolhaMao2 == 2:
            print('O jogador 1 ganhou!')
            placarJogador1 += 1
    #humano x humano

    elif escolhaJogador1 == 1 and escolhaJogador2 == 2:
        escolhaMao1 = int(input('Escolha sua mão: 1-pedra, 2-papel, 3-tesoura: '))
        escolhaMao2 = int(random.randint(1,3))
        if escolhaMao1 <= 0 or escolhaMao1 > 3:
            print('Valor não permitido')
        elif escolhaMao2 == 1:
            print('O jogador 2 escolheu: Pedra')
        elif escolhaMao2 == 2:
            print('O jogador 2 escolheu: Papel')
        elif escolhaMao2 == 3:
            print('O jogador 2 escolheu: Tesoura')

        if escolhaMao1 == escolhaMao2:
            print('Empate')
            placarJogador1 += 1
            placarJogador2 += 1
        elif escolhaMao1 == 1 and escolhaMao2 == 2:
            print('O jogador 2 ganhou!')
            placarJogador2 += 1
        elif escolhaMao1 == 1 and escolhaMao2 == 3:
            print('O jogador 1 ganhou!')
            placarJogador1 += 1
        elif escolhaMao1 == 2 and escolhaMao2 == 1:
            print('O jogador 1 ganhou!')
            placarJogador1 += 1
        elif escolhaMao1 == 2 and escolhaMao2 == 3:
            print('O jogador 2 ganhou!')
            placarJogador2 += 1
        elif escolhaMao1 == 3 and escolhaMao2 == 1:
            print('O jogador 2 ganhou!')
            placarJogador2 += 1
        elif escolhaMao1 == 3 and escolhaMao2 == 2:
            print('O jogador 1 ganhou!')
            placarJogador1 += 1
    #humano x computador

    elif escolhaJogador1 == 2 and escolhaJogador2 == 1:
        escolhaMao1 = int(random.randint(1, 3))
        escolhaMao2 = int(input('Escolha sua mão: 1-pedra, 2-papel, 3-tesoura: '))
        if escolhaMao2 <= 0 or escolhaMao2 > 3:
            print('Valor não permitido')
        elif escolhaMao1 == 1:
            print('O jogador 1 escolheu: Pedra')
        elif escolhaMao1 == 2:
            print('O jogador 1 escolheu: Papel')
        elif escolhaMao1 == 3:
            print('O jogador 1 escolheu: Tesoura')

        if escolhaMao1 == escolhaMao2:
            print('Empate')
            placarJogador1 += 1
            placarJogador2 += 1
        elif escolhaMao1 == 1 and escolhaMao2 == 2:
            print('O jogador 2 ganhou!')
            placarJogador2 += 1
        elif escolhaMao1 == 1 and escolhaMao2 == 3:
            print('O jogador 1 ganhou!')
            placarJogador1 += 1
        elif escolhaMao1 == 2 and escolhaMao2 == 1:
            print('O jogador 1 ganhou!')
            placarJogador1 += 1
        elif escolhaMao1 == 2 and escolhaMao2 == 3:
            print('O jogador 2 ganhou!')
            placarJogador2 += 1
        elif escolhaMao1 == 3 and escolhaMao2 == 1:
            print('O jogador 2 ganhou!')
            placarJogador2 += 1
        elif escolhaMao1 == 3 and escolhaMao2 == 2:
            print('O jogador 1 ganhou!')
            placarJogador1 += 1
    #computador x humano

    elif escolhaJogador1 == 2 and escolhaJogador2 == 2:
        escolhaMao1 = int(random.randint(1,3))
        escolhaMao2 = int(random.randint(1,3))

        if escolhaMao1 == 1:
            print('O jogador 1 escolheu: Pedra')
        elif escolhaMao1 == 2:
            print('O jogador 1 escolheu: Papel')
        elif escolhaMao1 == 3:
            print('O jogador 1 escolheu: Tesoura')

        if escolhaMao2 == 1:
            print('O jogador 2 escolheu: Pedra')
        elif escolhaMao2 == 2:
            print('O jogador 2 escolheu: Papel')
        elif escolhaMao2 == 3:
            print('O jogador 2 escolheu: Tesoura')

        if escolhaMao1 == escolhaMao2:
            print('Empate')
            placarJogador1 += 1
            placarJogador2 += 1
        elif escolhaMao1 == 1 and escolhaMao2 == 2:
            print('O jogador 2 ganhou!')
            placarJogador2 += 1
        elif escolhaMao1 == 1 and escolhaMao2 == 3:
            print('O jogador 1 ganhou!')
            placarJogador1 += 1
        elif escolhaMao1 == 2 and escolhaMao2 == 1:
            print('O jogador 1 ganhou!')
            placarJogador1 += 1
        elif escolhaMao1 == 2 and escolhaMao2 == 3:
            print('O jogador 2 ganhou!')
            placarJogador2 += 1
        elif escolhaMao1 == 3 and escolhaMao2 == 1:
            print('O jogador 2 ganhou!')
            placarJogador2 += 1
        elif escolhaMao1 == 3 and escolhaMao2 == 2:
            print('O jogador 1 ganhou!')
            placarJogador1 += 1
    #computador x computador

    print('O placar atual é: Jogador 1 -', placarJogador1, 'X', placarJogador2, '- Jogador 2' )
    continuar = int(input('O jogador deseja continuar? 1- sim, 2-não: '))

    if continuar == 1:
        quantidadeJogadas + 1

    elif continuar == 2:
        quantidadeJogadas = 0
        print('O placar final foi: Jogador 1 -', placarJogador1, 'X', placarJogador2, '- Jogador 2')
        print('Muito obrigado por jogar!')
        print('Desenvolvido por Lucas Cunha')
        break
