from datetime import date
atual = date.today().year
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Nascimento: '))
pessoa['carteira'] = int(input('CTPS: (0  nao tem) '))
pessoa['idade'] = atual - nasc
if pessoa['carteira'] != 0:
    pessoa['contratacao'] = int(input('Ano da contratação: '))
    pessoa['salario'] = int(input('Salario: '))
    pessoa['aposento'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - atual)
print('-=' * 15)
for i, v in pessoa.items():
    print(f'{i} tem o valor {v}')
