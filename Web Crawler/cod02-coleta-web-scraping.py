#Adicionar ao conjunto de importações
import requests

#Importação da biblioteca BeautifulSoup
#pip install beautifulsoup4
from bs4 import BeautifulSoup

url = "https://exame.abril.com.br/carreira/as-20-melhores-escolas-de-negocios-em-2017-segundo-o-ft/"

fonte = requests.get(url)

#Cria uma instância de BeautifulSoup baseado no código coletado
fonte_bs = BeautifulSoup(fonte.text)

#Recupera todos os parágrafos da instância de BeautifulSoup
paragrafos = fonte_bs.find_all('p')

#Apresente todos os parágrafos coletados
#print(paragrafos)

#Apresenta o primeiro parágrafo do ResultSet paragrafos
#print(paragrafos[1].text)

'''
#Apresenta o todos os parágrafos
for paragrafo in paragrafos:
    print(paragrafo.text)
    print("\n")

#Apresenta o parágrafo que contém o título
paragrafo_caption = fonte_bs.find('p', class_ = 'caption')
print(paragrafo_caption.text)

#Apresenta as imagens
imagens = fonte_bs.find_all('img')
for imagem in imagens:
    print(imagem)
    print("\n")

#Apresenta as tabelas
tabelas = fonte_bs.find('table')
for tabela in tabelas:
    print(tabela)
    print("\n")
'''

tabela = fonte_bs.find('table', class_='exameTable')
print(tabela.prettify())

