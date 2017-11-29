import requests
import json

#caminho base para requisitar a Graph API
base_url = "https://graph.facebook.com/"

#objeto para a requisição. representa o seu perfil pessoal no Facebook
#objeto = "me"
objeto = "100010367028666"


#versão padrão é a v2.5
versao = "v2.9/"

#preencha aqui com o valor do seu token de acesso
access_token = "EAABZC6IpUAPgBAEyjfWKEFGx9HSMss0QnHzA4l1QlKG28rIYkjZAiHKUhckMal4lpbcZCX0HlgBr8PbWZAUwx430shZBFfhzLMpa0RIYP0mj2xOPGzgbB8j5oLDuitediEkZCanEXDkImw5Gp6rYPOtCrwZC6ZBvB0ReHnyDpkY3ypdpRgDj2xKKIhM67TWivxQZD"

#Definição dos campos que iremos coletar
campos = "id,name,first_name,last_name,gender,website,cover"
#campos = "id,name,likes"
#campos = "id,name,posts"
#campos = "reactions"
#campos = "comments"
#campos = "sharedposts"

#A URL agora terá a variável campos
#url = "%s%s?fields=%s&access_token=%s" % (base_url, objeto, campos, access_token)

#URL para versão 2.8
url = '%s%s%s?fields=%s&access_token=%s' % (base_url, versao, objeto, campos, access_token)

#definição da URL de requisição
#cada %s será substituído por uma das variáveis listadas entre parênteses, na ordem em que foram definidas
#url = "%s%s?access_token=%s" % (base_url, objeto, access_token)

#envia a requisição
#recebe a resposta no formato JSON
dados = requests.get(url).json()

#apresenta a resposta identada
print(json.dumps(dados, indent=4))
