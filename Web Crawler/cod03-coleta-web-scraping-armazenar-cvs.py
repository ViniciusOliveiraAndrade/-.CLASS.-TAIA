#Conjunto de importações
import csv
import requests
from bs4 import BeautifulSoup

url = "https://exame.abril.com.br/carreira/as-20-melhores-escolas-de-negocios-em-2017-segundo-o-ft/"

fonte = requests.get(url)

#Cria uma instância de BeautifulSoup baseado no código coletado
fonte_bs = BeautifulSoup(fonte.text,"lxml")

#tabelas = fonte_bs.find('table')
tabela = fonte_bs.find('table')

#Cria e abre o arquivo dados_tabela.csv
arquivo_csv = open('dados_tabela.csv', mode='w', encoding='utf-8')

#Cria o objeto writer que será utilizado para escrever no arquivo
writer = csv.writer(arquivo_csv) 

#Escreve o cabeçalho no arquivo CSV
writer.writerow(['Ranking', 'Universidade', 'Pais', 'Nota'])

#Percorre cada linha tr da tabela
for linha in tabela.findAll('tr'):
    #Recupera todas as colunas td da linha tr
    celula = linha.findAll('td')
    #Se quatro células foram recuperadas
    if len(celula) == 4:
        #Extrai o texto (text=True) de cada célula
        #Remove as formatações existentes (strip())
        #O conteúdo da posição no ranking está na célula 0
        ranking = celula[0].find(text=True).strip('\t\r\nº')
        #O conteúdo do nome da universidade está na célula 1
        universidade = celula[1].find(text=True).strip('\t\r\n')
        #O conteúdo do nome do país está na célula 2
        pais = celula[2].find(text=True).strip('\t\r\n')
        #O conteúdo da nota está na célula 3
        nota = celula[3].find(text=True).strip('\t\r\n')
        
        #Escreve o conteúdo das variáveis em arquivo
        writer.writerow([ranking, universidade, pais, nota])

#Fecha o arquivo
arquivo_csv.close()
