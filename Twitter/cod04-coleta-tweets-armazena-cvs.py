# -*- coding: utf-8 -*-
#Conjunto de importação
import csv
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TwitterListener(StreamListener):  
    #método de inicialização   
    def __init__(self):
        self.cont_tweet = 0
        self.max_tweets = 100 
        
    def on_data(self, data):
        #incrementa o contador de tweets
        self.cont_tweet = self.cont_tweet + 1
        try:
            print(data)
            #converte o tweet para o formato json
            tweet = json.loads(data) 

            #cria e carrega o arquivo 'twitter_data_csv.csv'
            meu_arquivo = open('twitter_data.csv', mode='a', encoding='utf-8')
            #cria o objeto writer para escrever no arquivo
            writer = csv.writer(meu_arquivo) 
            #escreve os dados dos campos 'created_at' e 'text' no arquivo csv
            writer.writerow([tweet.get('id'),tweet.get('user').get('id'),tweet.get('created_at'), tweet.get('text')])
 
            #fecha a referência para o arquivo
            meu_arquivo.close()
        except BaseException as erro:
            print('Erro: ' + erro)
        #condição de parada
        if self.cont_tweet >= self.max_tweets:
            #retorne false
            return False

def coletar_tweets():
    #Complete aqui com o valor da "access_token" gerada para você
    access_token = "915648814073176065-jApC4BsYhVBeOOpFRZxHa2XsC9IVM1D"
    #Complete aqui com o valor da "access_token_secret" gerada para você
    access_token_secret = "NxjgwZWG8iYvNcSTe4HkEpNQ9KDweomENRdwsITBXu8c8"
    #Complete aqui com o valor da "consumer_key" gerada para você
    consumer_key = "2JWCtF4oJkPNi7HufZx7ojtSe"
    #Complete aqui com o valor da "consumer_secret" gerada para você
    consumer_secret = "1U9pEeRc5TXyYLzhTFhseJZuASBteJdxzOIjYZpp5wkEpLAAOs"

    tl = TwitterListener()
    oauth = OAuthHandler(consumer_key, consumer_secret)
    oauth.set_access_token(access_token, access_token_secret)

    stream = Stream(oauth, tl)
    stream.filter(track=['eleitor','eleicao','bolsonaro','doria'])

#chamada da função coletar_tweets()
coletar_tweets()
