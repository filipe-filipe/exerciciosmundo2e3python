def escreva(txt):
    quant = len(txt) + 4
    print('^' * quant)
    print(f'  {txt}')
    print('.' * quant)


escreva('Olá Mundo!')

