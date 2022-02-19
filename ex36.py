valor = int(input('Qual o valor da casa: R$'))
salario = int(input('Qual é o seu salario: R$'))
prazo = int(input('Em quantos meses quer financiar? '))
resultado = valor / prazo
if resultado > (30 * salario) / 100:
    print('O emprestimo foi negado')
else:
    print('O emprestimo foi aprovado')