def dobro(num, formato=False):
    d = num * 2
    return d if not formato else moeda(d)


def metade(num, formato=False):
    m = num / 2
    return m if not formato else moeda(m)

def aumentar(num, percento, formato=False):
    p = num + ((percento * num) / 100)
    return p if not formato else moeda(p)


def diminuir(num, porcento, formato=False):
    d = num - ((porcento * num) / 100)
    return d if not formato else moeda(d)

def moeda(preço, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'O dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(preço, taxa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)
