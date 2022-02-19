def calculo(num1, num2):
    prod = num1 * num2
    print(f'A area do terreno é de {prod:5.2f}m²')


largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
calculo(largura, comprimento)
