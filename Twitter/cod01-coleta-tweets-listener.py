#Conjunto de importações do Tweepy
#Import da classe Listener do Streaming
from tweepy.streaming import StreamListener
#Import da biblioteca de autenticação
from tweepy import OAuthHandler
#Import da biblioteca de Streaming
from tweepy import Stream

#Implementação básica da classe TwitterListener. 
#Ela irá ouvir o canal e printar cada novo tweet que chegar.
class TwitterListener(StreamListener):
    #método para definir quais ações executar quando um novo tweet chegar
    def on_data(self, data):
        try:
            #escreve na tela o novo dado que chegou (o tweet)
            print (data)
        except BaseException as erro:
            print('Erro: ' + erro)

    #metodo para definir quais ações executar em caso de erro no Listener
    def on_error(self, status):
        #escreve na tela o status do erro
        print (status)   

def coletar_tweets():
    #Complete aqui com o valor da "access_token" gerada para você
    access_token = "915648814073176065-jApC4BsYhVBeOOpFRZxHa2XsC9IVM1D"
    #Complete aqui com o valor da "access_token_secret" gerada para você
    access_token_secret = "NxjgwZWG8iYvNcSTe4HkEpNQ9KDweomENRdwsITBXu8c8"
    #Complete aqui com o valor da "consumer_key" gerada para você
    consumer_key = "2JWCtF4oJkPNi7HufZx7ojtSe"
    #Complete aqui com o valor da "consumer_secret" gerada para você
    consumer_secret = "1U9pEeRc5TXyYLzhTFhseJZuASBteJdxzOIjYZpp5wkEpLAAOs"

    #Cria uma instancia da classe TwitterListener()
    tl = TwitterListener()
    #Criação do objeto oauth passando os valores das chaves como argumentos
    oauth = OAuthHandler(consumer_key, consumer_secret)
    #Definição dos tokens de acesso para o objeto oauth
    oauth.set_access_token(access_token, access_token_secret)

     #Cria uma instância da classe Stream passando os valores da autenticação e o objeto da classe Listener
    stream = Stream(oauth, tl)
    #Define as palavras-chave que irão formar o filtro de busca de tweets
    stream.filter(track=['eleitor','eleicao','politica'])

#chamada da função coletar_tweets()
coletar_tweets()
