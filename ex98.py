from time import sleep

def linha():
    print('-=' * 16)

def contador(inicio, fim, passo):
    linha()
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}.')
    sleep(1)
    linha()
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont += passo
        print('... Fim.')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont -= passo
        print('... Fim.')
contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez!')
ini = int(input('Digite o inicio: '))
fi = int(input('Digite o fim:  '))
pas = int(input('Digite o passo: '))
contador(ini, fi, pas)