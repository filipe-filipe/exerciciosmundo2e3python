tot = 0
num = int(input('Digite um numero para saber se ele é primo ou não: '))
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
    else:
        print(f'{c}', end=' ')
print(f'\nO numero {num} foi divisivel {tot} vezes.')
if tot  == 2:
    print('Por isso ele é  primo!')
else:
    print('Ele nao é primo.')

