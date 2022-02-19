lista = []
while True:
    num = (int(input('Digite um numero: ')))
    if num not in lista:
        lista.append(num)
    else:
        print('Numero ja esta na lista, tente novamente.')
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).upper()
    if continua in 'N':
        break
print(f'Os valores unicos digitados foram {sorted(lista)}')
