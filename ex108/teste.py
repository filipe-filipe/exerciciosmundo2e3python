import moeda

num = int(input('Digite um numero: '))
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'Se aumentar 10% de {moeda.moeda(num)} ficará {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'Se diminuir 13% de {moeda.moeda(num)} ficará {moeda.moeda(moeda.diminuir(num, 13))}')
