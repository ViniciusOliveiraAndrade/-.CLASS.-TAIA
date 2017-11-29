# -*- coding: utf-8 -*-
#Conjunto de importações do Tweepy 
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
class TwitterListener(StreamListener):  
    #método de inicialização   
    def __init__(self):
        #contador de tweets
        self.cont_tweet = 0
        #valor máximo de tweets a ser coletado 
        self.max_tweets = 10 
        
    def on_data(self, data):
        #incrementa o contador de tweets
        self.cont_tweet = self.cont_tweet + 1
        try:
            #carrega e codifica os dados para o formato JSON
            tweet = json.loads(data)
            #Escreve o campo de data de publicação do tweet
            print("Data da publicacao do tweet")            
            print(tweet.get('created_at'))
            #Escreve o campo referente ao conteúdo do tweet
            print("Conteudo do tweet")
            print(tweet.get('text'))
            #Escreve o campo referente ao idioma do tweet
            print("Idioma do tweet")
            print(tweet.get('lang'))
            #Escreve o campo referente ao total de likes que o tweet recebeu
            print("Total de likes do tweet")
            print(tweet.get('favorite_count'))
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
    stream.filter(track=['eleitor', 'eleicao', 'bolsanaro'])

#chamada da função coletar_tweets()
coletar_tweets()