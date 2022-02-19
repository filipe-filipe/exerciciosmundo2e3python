from random import randint


def sorteio(lista):
    for cont in range(0, 5):
        n = randint(0, 10)
        numeros.append(n)
    print(f'Sorteando 5 valores da lista: {lista}')


def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma de todos os valores pares de {lista} temos {soma}')


numeros = list()
sorteio(numeros)
somapar(numeros)

