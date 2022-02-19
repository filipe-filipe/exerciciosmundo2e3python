from datetime import date

def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'


nasc = int(input('Em que anos você nasceu? '))
print(voto(nasc))
