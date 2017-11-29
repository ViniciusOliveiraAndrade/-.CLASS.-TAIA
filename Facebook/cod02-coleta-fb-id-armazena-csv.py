import requests
import json
import csv

base_url = "https://graph.facebook.com/"
objeto = "1026767537475962"
campos = "reactions"
versao = "v2.9/"
access_token = "EAABZC6IpUAPgBAEyjfWKEFGx9HSMss0QnHzA4l1QlKG28rIYkjZAiHKUhckMal4lpbcZCX0HlgBr8PbWZAUwx430shZBFfhzLMpa0RIYP0mj2xOPGzgbB8j5oLDuitediEkZCanEXDkImw5Gp6rYPOtCrwZC6ZBvB0ReHnyDpkY3ypdpRgDj2xKKIhM67TWivxQZD"

url = "%s%s%s?fields=%s&access_token=%s" % (base_url, versao, objeto, campos, access_token)

dados = requests.get(url).json()

#Salvar os dados coletados no arquivo facebook_data.csv
meu_arquivo = open('facebook_data.csv', mode='a', encoding='utf-8')
writer = csv.writer(meu_arquivo)

for dado in dados['reactions']['data']:
    writer.writerow([dado['id'], dado['name'], dado['type']])
meu_arquivo.close()
