aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Media do aluno: '))
if aluno['media'] < 7:
    aluno['nota'] = 'Reprovado'
if aluno['media'] >= 7:
    aluno['nota'] = 'Aprovado'
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["nota"]}')

print(aluno.items())