sexo = str(input('Digite seu sexo: [M/F] ')).upper()
while sexo not in 'MF':
    print('Sexo invalido, tente novamente.')
    sexo = str(input('Digite seu sexo: [M/F] ')).upper()
print('Fim')