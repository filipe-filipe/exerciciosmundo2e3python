pessoa = {}
lista = []
media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        continua = str(input('Quer continuar? [S/N]: ')).upper()
        if continua in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continua == 'N':
        break
print('-=' * 14)
print(f'O grupo tem {len(lista)} pessoas.')
print(f'A media de idade é de {media / len(lista):5.2f}')
print(f'As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(p['nome'], end=' ')
print()
print(f'Lista das pessoas que estao acima da media: ', end='')
for p  in lista:
    if p['idade'] > media / len(lista):
        print(p['nome'], end=' ')