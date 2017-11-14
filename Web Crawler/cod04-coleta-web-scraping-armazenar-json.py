#Conjunto de importações
import csv
import requests
import json
from bs4 import BeautifulSoup

url = 'http://exame.abril.com.br/carreira/as-100-melhores-universidades-da-america-latina/'
fonte = requests.get(url)

#Cria uma instância de BeautifulSoup baseado no código coletado
fonte_bs = BeautifulSoup(fonte.text)

#tabelas = fonte_bs.find('table')
tabela = fonte_bs.find('table')

#O dicionário é iniciado
dic_tabela = []        

#A tabela é percorrida
for linha in tabela.findAll('tr'):
    celula = linha.findAll('td')    
    if len(celula) == 4:
        #O conteúdo de cada célula é extraído
        ranking = celula[0].find(text=True).strip('\t\r\nº')
        universidade = celula[1].find(text=True).strip('\t\r\n')
        pais = celula[2].find(text=True).strip('\t\r\n')
        nota = celula[3].find(text=True).strip('\t\r\n')

        #O dicionário é alimentado com os valores extraídos das células
        dic_tabela.append({
            "Ranking": ranking,
            "Universidade": universidade,
            "Pais": pais,
            "Nota": nota
        })

#Ao final do laço o dicionário é armazenado no arquivo JSON        
with open('dados_tabela.json', mode='a') as arquivo_json:
    json.dump(dic_tabela, arquivo_json, indent=4)
