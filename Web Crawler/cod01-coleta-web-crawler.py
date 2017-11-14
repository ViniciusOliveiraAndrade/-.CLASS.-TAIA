#Conjunto de importações
import requests

#URL da pagina que será acessada pelo Web crawler
url = "https://exame.abril.com.br/carreira/as-20-melhores-escolas-de-negocios-em-2017-segundo-o-ft/"

#Recupera o conteúdo da página
fonte = requests.get(url)

if fonte.status_code == 200:
    #Apresenta todo o conteúdo da página
    print(fonte.text)

    #Apresenta a url da página
    print("URL ", fonte.url)

    #Apresenta o tipo de encoding utilizado
    print("Encoding", fonte.encoding)

    #Apresenta o código do status da requisição
    print("Status", fonte.status_code)
else:
    #Apresenta a mensagem de erro
    print(fonte.raise_for_status())
