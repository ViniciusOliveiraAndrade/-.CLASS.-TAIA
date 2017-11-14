import requests

url = "https://exame.abril.com.br/carreira/as-20-melhores-escolas-de-negocios-em-2017-segundo-o-ft/"

fonte = requests.get(url)

print(fonte.text)

  