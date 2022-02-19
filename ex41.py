from datetime import date
nasc = int(input('Em que ano você nasceu: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('Você esta na categoria mirim')
elif idade <= 14:
    print('Você esta na categoria infantil')
elif idade <= 19:
    print('Você esta na categoria junior')
elif idade <= 20:
    print('Você esta na categoria sênior')
else:
    print('Você está na categoria master')
