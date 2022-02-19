dado = []
galera = []
maior = menor = cont = 0
while True:
    nome = str(input('Digite seu nome: '))
    dado.append(nome)
    peso = float(input('Digite seu peso: '))
    cont += 1
    dado.append(peso)
    galera.append(dado[:])
    dado.clear()
    if cont == 1:
        maior = menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).upper()
    if continua == 'N':
        break
print(f'Foram cadastradas {len(galera)} pessoa(s).')
print(f'O maior peso foi {maior}Kg de ', end='')
for p in galera:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso foi {menor}Kg de ', end='')
for p in galera:
    if p[1] == menor:
        print(p[0])
