
import requests
import json
import csv

#1 - PT na Camara - 1009026819197921
#2 - Midia Ninja - 637898533034962
#3 - Midia Ninja - 954646961360116

base_url = "https://graph.facebook.com/"
objeto = "954646961360116"
campos = "comments.limit(5000)"
versao = "v2.9/"
access_token = "EAABZC6IpUAPgBABoVGRgZCIhPpR1X2n2uq5AXw2mI3SZAd9AocHUNC2QxiXTIZCR2vmBFLOhSktEKZAUdMleDnSp6YPM1IenPPShJNCwYE9wChgm6kQNWHooaCkG0lFtttnkCdgTFZBBRr6MsgGZArqIZAZBZBXmWZBzxGuHUgaXnb0SwZDZD"

url = "%s%s%s?fields=%s&access_token=%s" % (base_url, versao, objeto, campos, access_token)

dados = requests.get(url).json()

max_caracteres = 200
min_caracteres = 16

qt_com = 0



#Salvar os dados coletados no arquivo facebook_data.csv
meu_arquivo = open('results/facebook_data.csv', mode='a', encoding='utf-8')
writer = csv.writer(meu_arquivo)

writer.writerow(["ID Comentario", "Nome do usuário","Mensagem","Ándre","Vinícius"])

for dado in dados['comments']['data']:
    
    if "bolsonaro" in dado['message'].lower():
    	if len(dado['message']) <= max_caracteres and len(dado['message']) > min_caracteres:
            writer.writerow([dado['id'], dado['from']['name'],dado['message']])
            qt_com += 1

meu_arquivo.close()
print("Quantidades de commentarios pegos: %i"%(qt_com))