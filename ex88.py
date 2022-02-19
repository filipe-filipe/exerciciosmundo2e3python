from random import randint
quant = int(input('Digite a quantidade de jogos que quer ver: '))
numeros = []
jogos = []
jogada = 1
while jogada <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
            cont += 1
        if cont == 6:
            break
    numeros.sort()
    jogada += 1
    jogos.append(numeros[:])
    numeros.clear()
print('*' * 3, f'Sorteando {quant} jogos', '*' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i}: {l}')

