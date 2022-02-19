nota1 = float(input('Digite sua nota: '))
nota2  = float(input('Digite sua outra nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Media foi de {media}, você foi reprovado!')
elif 5 < media <= 6.9:
    print(f'Media de {media}, voce esta de recuperação!')
else:
    print(f'media de {media}, você foi aprovado!')