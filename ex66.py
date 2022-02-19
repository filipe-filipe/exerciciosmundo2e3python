soma = quant = 0
while True:
    num = int(input('Digite um numero: [999] para parar] '))
    if num == 999:
        break
    soma += num
    quant += 1
print(f'Voce digitou {quant} numero(s) e a soma entre eles foi {soma}.')