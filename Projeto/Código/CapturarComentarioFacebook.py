import requests
import json


def capcom(id_objeto,qt_comentario = 5000):
	
	base_url = "https://graph.facebook.com/"
	objeto = str(id_objeto)
	campos = "comments.limit("+str(qt_comentario)+")"
	versao = "v2.9/"
	access_token = "EAABZC6IpUAPgBABoVGRgZCIhPpR1X2n2uq5AXw2mI3SZAd9AocHUNC2QxiXTIZCR2vmBFLOhSktEKZAUdMleDnSp6YPM1IenPPShJNCwYE9wChgm6kQNWHooaCkG0lFtttnkCdgTFZBBRr6MsgGZArqIZAZBZBXmWZBzxGuHUgaXnb0SwZDZD"

	url = "%s%s%s?fields=%s&access_token=%s" % (base_url, versao, objeto, campos, access_token)

	dados = requests.get(url).json()

	return dados