from random import randint
computador = randint(0, 10)
print('Sou seu computador e pensei em um numero entre 0 e 10!')
print('Tente adivinhar qual foi!')
palpite = int(input('Digite seu palpite: '))
tent = 1
while palpite != computador:
    if palpite < computador:
        print('Mais... tente novamente.')
    elif palpite > computador:
        print('Menos... tente novamente.')
    palpite = int(input('Digite seu palpite: '))
    tent += 1
print(f'Parabéns você acertou com {tent} tentativas!')