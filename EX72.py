contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenovo', 'vinte')
while True:
    num = int(input('Digite um numero de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Opção invalida, tente novamente.', end=' ')
print(f'Você digitou o numero {contagem[num]}')
