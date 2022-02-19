num = (int(input('Digite um numero: ')), int(input('Digite um numero: ')),
       int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(f'Você digitou os numeros {num}')
print(f'O valor 9 foi digitado {num.count(9)} vez(es).')
if 3 in num:
    print(f'O valor 3 apareceu {num.index(3)} vez(es).')
else:
    print('O valor 3 nao foi digitado.')
print(f'Os numeros pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')




