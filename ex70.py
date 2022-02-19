print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)
total = mil = menor = 0
cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: '))
    total += preço
    cont += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    if preço >= 1000:
        mil += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).upper()
    if continua in 'N':
        break

print('Fim do programa')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {mil} produto(s) custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')