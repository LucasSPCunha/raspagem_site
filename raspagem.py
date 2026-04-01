import requests
from bs4 import BeautifulSoup

# USER AGENT
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
}

# PESQUISAR PRODUTO
produto = input('Digite o produto: ')
produto = produto.replace(' ', '-')

# URL BASE
url = f'https://lista.mercadolivre.com.br/{produto}_Desde_'

# CONTAGEM
start = 1

# LOOP DE RASPAGEM
while True:
    url_final = url + str(start) + '_NoIndex_True'

    #FAZER A REQUISIÇÃO
    r = requests.get(url_final, headers=headers)
    site = BeautifulSoup(r.content, 'html.parser')

    # ENCONTRAR RESULTADOS
    descricoes = site.find_all('h3', class_='poly-component__title-wrapper')
    precos = site.find_all('span', class_='andes-money-amount__fraction')
    links = site.find_all('a', class_='poly-component__title')

    # VERIFICAR SE HA MAIS RESULTADOS
    if not descricoes:
        print('Sem itens')
        break

    #CAPTURAR DADOS
    for descricoes, precos, links in zip(descricoes, precos, links):
        print('\033[mProduto: ' + descricoes.get_text())
        print('\033[32mValor: R$' + precos.get_text())
        print(f'\033[34mLink: {links.get('href')}\n' )
    # INDEX DAS PAGINAS
    start += 47