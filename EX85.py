lista_unica = []
lista_par = []
lista_impar = []
for p in range(1, 8):
    pergunta = int(input(f'Digite o {p}o. valor: '))
    if pergunta % 2 == 0:
        lista_par.append(pergunta)
    else:
        lista_impar.append(pergunta)
lista_unica.append(lista_par[:])
lista_unica.append(lista_impar[:])
print(f'Os valores pares digitados foram: {sorted(lista_par)}')
print(f'Os valores impares digitados foram: {sorted(lista_impar)}')
