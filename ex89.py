aluno = []
nota1 = []
nota2 = []
temp = []
while True:
    nome = str(input('Nome: '))
    nota01 = int(input('Nota 1: '))
    nota02 = int(input('Nota 2: '))
    temp.append(nome)
    temp.append(nota01)
    temp.append(nota02)
    aluno.append(temp[:])
    temp.clear()
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [s/n]: ')).upper()
    if continua in 'N':
        break
print(f'No  Nome        Media')
for i, a in enumerate(aluno):
    print(f'{i}   {a[0]}        {(a[1] + a[2]) / 2}')
while True:
    saber = int(input('Quer ver as notas de qual aluno? (999 Interrompe): '))
    if saber == 999:
        break
    print(f'As notas de {aluno[saber][0]} são {aluno[saber][1:]}')
print('Fim do programa!')


