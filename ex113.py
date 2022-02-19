def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero valido.')
            continue
        except (KeyboardInterrupt):
            print('Usurio preferiu não  digitar esse numero.')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um n umero real valido.')
            continue
        except  (KeyboardInterrupt):
            print('Usuario preferiu não digitar esse numero.')
            return 0
        else:
            return n


n1 = leiaint('Digite um numero inteiro: ')
n2 = leiafloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}.')

