from datetime import date
ano = int(input('Qual é o seu ano de nascimento? '))
atual = date.today().year - ano
if atual < 18:
    print(f'Você so vai se alistar no exercito em {18 - atual} anos.')
elif atual == 18:
    print('Você precisa se alistar esse ano!')
else:
    print(f'Você ja deveria ter se alistado a {atual - 18} ano(s)')
