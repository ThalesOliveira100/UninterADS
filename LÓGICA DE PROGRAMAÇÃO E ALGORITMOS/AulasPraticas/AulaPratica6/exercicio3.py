# Criar JokenpÔ
# Usuário VS Computador
# 0 - Encerrar Disputa, 1 - Pedra, 2 - Papel, 3 - Tesoura
# Todos os resultados serão armazenados em uma lista e no final apresenta o vencedor
# Encerra o programa ao digitar zero
from random import randint

vitoriasPlayer = 0
vitoriasComputador = 0
empates = 0
resultados_lista = []
jogadas = []


def encerrar_partida():
    print('|  Jogos: {}  |  Vitórias Player: {}  |  Vitórias Computador: {}  |  Empates: {}  |'
          .format(len(jogadas), vitoriasPlayer, vitoriasComputador, empates).center(69))


def define_vencedor(jogador1, jogador2):
    global empates, vitoriasPlayer, vitoriasComputador

    if jogador1 == 1:  # Pedra
        if jogador2 == 1:
            empates += 1

        elif jogador2 == 2:
            vitoriasComputador += 1

        elif jogador2 == 3:
            vitoriasPlayer += 1

    elif jogador1 == 2:  # Papel
        if jogador2 == 1:
            vitoriasPlayer += 1

        elif jogador2 == 2:
            empates += 1

        elif jogador2 == 3:
            vitoriasComputador += 1

    elif jogador1 == 3:  # Tesoura
        if jogador2 == 1:
            vitoriasComputador += 1

        elif jogador2 == 2:
            vitoriasPlayer += 1

        elif jogador2 == 3:
            empates += 1

    return [vitoriasPlayer, vitoriasComputador, empates]


# Programa principal
print('-' * 79)
print('-' * 30, 'JOKENPÔ DO THALES', '-' * 30)
print('-' * 79)

while True:
    print('\nFaça a sua jogada:\n'
          '1 - Pedra\n'
          '2 - Papel\n'
          '3 - Tesoura\n\n'
          '0 - Encerrar disputa')
    jogada_player = int(input('>> '))

    if jogada_player == 0:
        encerrar_partida()
        exit('Encerrando o programa....')

    elif jogada_player in [1, 2, 3]:
        jogada_computador = randint(1, 3)
        jogadas.append([jogada_player, jogada_computador])
        resultados_lista = define_vencedor(jogada_player, jogada_computador)

        for jogada in jogadas:
            for dado in jogada:
                print(dado, end=' ')
                print()

    else:
        print('\nJogada inválida! Tente novamente.\n')
