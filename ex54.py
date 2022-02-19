count = countmenor = 0
for pessoa in range(0, 7):
    ano = int(input('Qual é o ano do seu nascimento? '))
    if ano < 2003:
        count += 1
    elif ano > 2003:
        countmenor += 1
print(f'{count} pessoas ja atingiram a maioridade.')
print(f'{countmenor} pessoas ainda nao atingiram a maioridade.')