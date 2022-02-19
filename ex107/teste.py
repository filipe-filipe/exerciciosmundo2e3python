import moeda

num = int(input('Digite um numero: '))
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'Se aumentar 10% de R${num} ficará R${moeda.aumentar(num, 10)}')
print(f'Se diminuir 13% de R${num} ficará R${moeda.diminuir(num, 13)}')