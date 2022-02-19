time = list()
jogador = {}
marcados = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas jogou: '))
    for p in range(partidas):
        marcados.append(int(input(f'Quantos gols fez na partida {p + 1}:  ')))
    jogador['gols'] = marcados.copy()
    jogador['total'] = sum(marcados)
    time.append(jogador.copy())
    marcados.clear()
    while True:
        continua = str(input('Quer continuar? [S/N]: ')).upper()
        if continua in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continua == 'N':
        break
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 15)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('-=' * 15)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jhogador com codigo {busca}!')
    else:
        print(f'  -- Levantamento do  jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-=' * 15)
print('VOLTE  SEMPRE')

