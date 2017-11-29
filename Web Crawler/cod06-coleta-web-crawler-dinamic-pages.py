#Conjunto de importações
#Classe para definir condição de espera para o WebDriver.
from selenium.webdriver.support.ui import WebDriverWait

#Conjunto de funções que determinam condições para a manipulação de elementos
from selenium.webdriver.support import expected_conditions as EC

#Classe utilizada para definir a localização do elemento a ser raspado
from selenium.webdriver.common.by import By

from selenium import webdriver
from bs4 import BeautifulSoup

#Definição da url        
url = 'http://g1.globo.com/economia/noticia/brasil-registra-criacao-de-598-mil-empregos-formais-em-abril.ghtml'        


#Classes para os WebDrivers disponíveis.
#Descomente a linha referente ao seu navegador.
#wd = webdriver.Firefox()
wd = webdriver.Chrome()
#wd = webdriver.Safari()
#wd = webdriver.Edge()

#Carrega a página definida no url
wd.get(url)

#Durante 10s o WebDriver irá aguardar que a div 'glbComentarios-conteudo-interno' esteja clicável.
WebDriverWait(wd, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="glbComentarios-conteudo-interno"]')))

#Recupera o código-fonte da página
fonte_pagina = wd.page_source

#Encerra a instância aberta do navegador
wd.quit()

#Realiza a raspagem dos dados
soup = BeautifulSoup(fonte_pagina)
comentarios = soup.findAll('p', class_='glbComentarios-texto-comentario')

print(comentarios)
