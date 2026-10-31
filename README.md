# Raspagem de produtos do Mercado Livre

Script em Python que pesquisa um produto no Mercado Livre, percorre todas as páginas de resultados e mostra o nome, o preço e o link de cada anúncio, salvando os links em um arquivo de texto.

## Funcionalidades

- Busca por qualquer produto digitado pelo usuário
- Paginação automática até acabarem os resultados
- Exibe nome, preço e link de cada anúncio no terminal, com cores
- Ignora links patrocinados
- Salva os links encontrados em `links.txt`

## Tecnologias

- Python 3.12+
- [requests](https://pypi.org/project/requests/) para as requisições HTTP
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) para ler o HTML das páginas

## Como executar

```bash
git clone https://github.com/LucasSPCunha/raspagem_site.git
cd raspagem_site
pip install requests beautifulsoup4 pyshorteners
python raspagem.py
```

Depois é só digitar o nome do produto quando o programa pedir, por exemplo: `notebook gamer`.

## Autor

Lucas Cunha — [LinkedIn](https://www.linkedin.com/in/lucasspcunha)
