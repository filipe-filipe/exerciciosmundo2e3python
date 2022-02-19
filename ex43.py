peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * 2)
if imc < 18.5:
    print(f'Seu imc é {imc}, você está abaixo do peso')
elif imc < 25:
    print(f'Seu imc é {imc}, você está no peso ideal')
elif imc < 30:
    print(f'Seu imc é de {imc}, você esta com sobrepeso')
elif imc < 40:
    print(f'Seu imc cé de {imc}, você esta com obesidade')
else:
    print(f'Seu imc é de {imc}, você esta com obesidade morbita')