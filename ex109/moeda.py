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

