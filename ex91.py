from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}

jogadores['Jogador 1'] = randint(1, 6)
jogadores['Jogador 2'] = randint(1, 6)
jogadores['Jogador 3'] = randint(1, 6)
jogadores['Jogador 4'] = randint(1, 6)

rank = list()

print('Valores sorteados: ')
sleep(1)
for j, v in jogadores.items():
    print(f'    O {j} tirou {v}')
    sleep(1)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores: ')
for i, v in enumerate(rank):
    print(f'    O {i+1} lugar: {v[0]} tirou {v[1]}')