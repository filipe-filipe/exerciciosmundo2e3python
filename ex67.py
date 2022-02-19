while True:
    escolha = int(input('Digite um numero para ver sua tabuada: '))
    if escolha < -1:
        break
    for numero in range(1, 11):
        print(f'{escolha} x {numero} = {escolha * numero}')
print('Programa encerrado, volte sempre!')


