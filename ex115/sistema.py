from ex115.lib.interface import *

from time import sleep
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquiv(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema, ate logo.')
        break
    else:
        print('\033[31mERRO: Digite uma opção valida.\033[m')
    sleep(1)
