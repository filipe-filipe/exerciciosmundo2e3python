lista = []
while True:
    lista.append(int(input('Digite um numero para guardar: ')))
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).upper()
    if continua in 'N':
        break
print(f'Foram digitados {len(lista)} numero(s).')
lista.sort(reverse=True)
print(f'Os numeros em ordem descrescente foram {lista}.')
if 5 in lista:
    print('O numero 5 esta na lista.')
else:
    print('O numero 5 não esta na lista.')
