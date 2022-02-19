
menor = homem = mulher = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper()
    print('-' * 30)
    continua = ' '
    while continua not in 'SsNn:':
        continua = str(input('Quer continuar? [S/N] ')).upper()
    if continua in 'Nn':
        break
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher += 1
    if idade > 18:
        menor += 1
print(f'Total de pessoas com mais de 18 anos: {menor}')
print(f'Ao todo temos {homem} homem(ns) cadastrados')
print(f'E temos {mulher} mulher(es) com menos de 20 anos')

