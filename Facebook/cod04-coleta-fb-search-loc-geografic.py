import requests
import json

import csv

base_url = "https://graph.facebook.com/search"
q = "cafe"
tipo = "place"
centro = "-15.77972,-47.92972"
distancia = "50000"
access_token = "EAABZC6IpUAPgBAEyjfWKEFGx9HSMss0QnHzA4l1QlKG28rIYkjZAiHKUhckMal4lpbcZCX0HlgBr8PbWZAUwx430shZBFfhzLMpa0RIYP0mj2xOPGzgbB8j5oLDuitediEkZCanEXDkImw5Gp6rYPOtCrwZC6ZBvB0ReHnyDpkY3ypdpRgDj2xKKIhM67TWivxQZD"

url = "%s?q=%s&type=%s&center=%s&distance=%s&access_token=%s" % (base_url, q, tipo, centro, distancia, access_token)

dados = requests.get(url).json()
print (json.dumps(dados, indent=4))



meu_arquivo = open('facebook_data_geo.csv', mode='a', encoding='utf-8')
writer = csv.writer(meu_arquivo)

for dado in dados['data']:
    writer.writerow([dado['id'], dado['name']])
