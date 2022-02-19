import moeda

num = int(input('Digite um numero: '))
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'Se aumentar 10% de {moeda.moeda(num)} ficará {moeda.aumentar(num, 10, True)}')
print(f'Se diminuir 13% de {moeda.moeda(num)} ficará {moeda.diminuir(num, 13, True)}')
