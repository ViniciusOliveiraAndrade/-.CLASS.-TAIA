import requests
import json

#Função para capturar comentaios do facebook, recebe como parametro o id do post e opcionalmente a quantidade de comentarios
def capcom(id_objeto,qt_comentario = 5000):
	
	base_url = "https://graph.facebook.com/" #A url do api do facebook
	objeto = str(id_objeto) #id do post
	campos = "comments.limit("+str(qt_comentario)+")" #campo que quer e quantidade
	versao = "v2.9/" #versão da api
	access_token = "EAABZC6IpUAPgBAOfIIyOD38qzKLWRE1ggGnwErbaIZB62e9Pe9BKW8wmGhTCc8o0gvJEvs0TBIfLRLk0wTCu6Y1j1eMSUIZABcy9byhfgLFxoDZAKiFZCgcphlBBrsF9UIq6FNKsA0UPzNA08ZAyNuJNsWBf3uuIMZD" #token de aceo

	url = "%s%s%s?fields=%s&access_token=%s" % (base_url, versao, objeto, campos, access_token) #junção e formação da url completa

	dados = requests.get(url).json() #resultados em json da que foi passado pela url

	return dados #retorna os dados