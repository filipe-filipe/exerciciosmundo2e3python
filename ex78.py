lista = []
for c in range(0, 5):
    lista.append(int(input('Digite um numero para guardar: ')))
print(f'O maior numero foi {max(lista)} na posição ', end='')
for n, v in enumerate(lista):
    if v == max(lista):
        print(n, end='... ')
print(f'\nO menor numero foi {min(lista)} na posição', end=' ')
for pos, num in enumerate(lista):
    if num == min(lista):
        print(pos, end='... ')