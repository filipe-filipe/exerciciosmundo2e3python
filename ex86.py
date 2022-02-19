lista = [[], [], []]
for n in range(0, 9):
    num = int(input('Digite um valor para: '))
    if n <= 2:
        lista[0].append(num)
    elif n <= 5:
        lista[1].append(num)
    else:
        lista[2].append(num)
for v in(lista[0]):
    print(f'[{v:^5}]', end=' ')
print()
for b in lista[1]:
    print(f'[{b:^5}]', end=' ')
print()
for c in lista[2]:
    print(f'[{c:^5}]', end=' ')
