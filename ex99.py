def lin():
    print('-=' * 24)
def maior(* num):
    cont = maior = 0
    lin()
    print('Analisando os valores informados: ')
    print(num)
    for n in num:
        if cont == 0:
            maior = n
            cont += 1
        elif n > maior:
            maior = n
    print(f'O maior valor informado foi {maior}.')


maior(9, 88, 45, 23, 100, 99, 1000)
maior(6)
maior(9, 8, 0, 2, 9)
maior()
