from googlesearch import search
from time import sleep

def buscas():

    print('='*50)
    print('buscas no google')
    print('='*50)
    sleep(2)
    query = str(input('o que deseja procurar?\n'))
    quantidade = int(input('quantidade de buscas: '))
    print('aqui estao alguns resultados de sua pesquisa:\n')
    sleep(1)

    for sites in search(query,stop=quantidade,):
        print(sites)
buscas()

while True:
    pergunta = int(input('\ndeseja buscar sobre algo mais ?\n[0]para sim\n[1]para nao\n'))

    if pergunta == 0:
        buscas()

    if pergunta ==1:
        print('saindo ...')
        break