# -*- coding: utf-8 -*-
#Conjunto de importa��es
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TwitterListener(StreamListener):  
    #m�todo de inicializa��o   
    def __init__(self):
        #contador de tweets
        self.cont_tweet = 0
        #valor m�ximo de tweets a ser coletado
        self.max_tweets = 10 
        
    def on_data(self, data):
        #incrementa o contador de tweets 
        self.cont_tweet = self.cont_tweet + 1
        try:
            print(data)
            #converte o tweet para o formato json
            tweet = json.loads(data) 
            #cria e carrega o arquivo 'twitter_data.json'
            #o argumento mode='a' indica que ser� realizada a opera��o append
            with open('twitter_data.json', mode='a') as meu_arquivo:
                #salva o tweet no arquivo com identa��o
                json.dump(tweet, meu_arquivo, indent=4) 
        except BaseException as erro:
            print('Erro: ' + erro)
        #condi��o de parada
        if self.cont_tweet >= self.max_tweets:
             #retorne false
             return False

def coletar_tweets():
   #Complete aqui com o valor da "access_token" gerada para voc�
    access_token = "915648814073176065-jApC4BsYhVBeOOpFRZxHa2XsC9IVM1D"
    #Complete aqui com o valor da "access_token_secret" gerada para voc�
    access_token_secret = "NxjgwZWG8iYvNcSTe4HkEpNQ9KDweomENRdwsITBXu8c8"
    #Complete aqui com o valor da "consumer_key" gerada para voc�
    consumer_key = "2JWCtF4oJkPNi7HufZx7ojtSe"
    #Complete aqui com o valor da "consumer_secret" gerada para voc�
    consumer_secret = "1U9pEeRc5TXyYLzhTFhseJZuASBteJdxzOIjYZpp5wkEpLAAOs"

    tl = TwitterListener()
    oauth = OAuthHandler(consumer_key, consumer_secret)
    oauth.set_access_token(access_token, access_token_secret)

    stream = Stream(oauth, tl)
    stream.filter(track=['eleitor','eleicao','politica'])

#chamada da fun��o coletar_tweets()
coletar_tweets()