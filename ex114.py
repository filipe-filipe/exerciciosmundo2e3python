import urllib.request

try:
    site: urllib.request.urlopen("http://pudim.com.br/")
except:
    print('Não consegui acessar o site.')
else:
    print('Consegui acessar o site com sucesso.')