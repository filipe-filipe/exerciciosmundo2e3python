impar = soma = 0
for impar in range(1, 500):
    if impar % 3 == 0:
        impar += impar
        soma += impar
print(soma)
