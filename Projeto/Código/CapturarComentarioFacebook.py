import requests
import json


def capcom(id_objeto,qt_comentario = 5000):
	
	base_url = "https://graph.facebook.com/"
	objeto = str(id_objeto)
	campos = "comments.limit("+str(qt_comentario)+")"
	versao = "v2.9/"
	access_token = "EAABZC6IpUAPgBAOfIIyOD38qzKLWRE1ggGnwErbaIZB62e9Pe9BKW8wmGhTCc8o0gvJEvs0TBIfLRLk0wTCu6Y1j1eMSUIZABcy9byhfgLFxoDZAKiFZCgcphlBBrsF9UIq6FNKsA0UPzNA08ZAyNuJNsWBf3uuIMZD"

	url = "%s%s%s?fields=%s&access_token=%s" % (base_url, versao, objeto, campos, access_token)

	dados = requests.get(url).json()

	return dados