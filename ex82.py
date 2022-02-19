lista1 = []
par = []
impar = []
while True:
    num = int(input('Digite um numero para guardar: '))
    lista1.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).upper()
    if continua in 'N':
        break
print(f'A lista completa é {lista1}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')