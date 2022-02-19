n1 = int(input('Digite o  primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('-=' * 15)
print('''Escolha uma opção:
[1] SOMAR
[2] MULTTIPLICAR
[3] MAIOR NUMERO
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA''')
print('-=' * 15)
opção = int(input('Digite sua opção: '))
print('-=' * 15)
while opção != 5:
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {produto}.')
    elif  opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior numero entre {n1} e {n2} é {maior}')
    elif opção == 4:
        n1 = int(input('Digite o  primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando')
    else:
        print('Opção invalida tente novamente.')
    print('-=' * 15)
    opção = int(input('Digite sua opção: '))
    print('-=' * 15)
print('Fim do programa.')
