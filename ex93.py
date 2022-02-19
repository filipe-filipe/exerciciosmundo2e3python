jogador = {}
marcados = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas jogou: '))
for p in range(partidas):
    marcados.append(int(input(f'Quantos gols fez na partida {p + 1}:  ')))
    jogador['gols'] = marcados.copy()
    jogador['total'] = sum(marcados)
print('~~^^' * 10)
for i, c in jogador.items():
    print(f'O campo {i} tem o valor {c}.')
print('~~^^' * 10)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for i, c in enumerate(marcados):
    print(f'    Na partida {i + 1}, fez {c} gols.')