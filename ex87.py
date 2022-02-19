lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = terc = 0
for c in range(0, 3):
    for l in range(0, 3):
        lista[c][l] = int(input(f'Digite um valor para [{c} {l}]: '))
        if lista[c][l] % 2 == 0:
            spar += lista[c][l]
        if lista[c][2]:
            terc += lista[c][2]
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{lista[c][l]:^5}]', end=' ')
    print()
print(f'A soma dos valores pares é {spar}.')
print(f'A soma da terceira coluna é {terc}.')
print(f'O maior valor da segunda linha é {max(lista[1])}.')