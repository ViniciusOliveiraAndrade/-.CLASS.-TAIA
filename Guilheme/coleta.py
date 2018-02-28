import csv
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


class TwitterListener(StreamListener):
    def __init__(self):
        self.cont_tweet = 0
        self.max_tweets = 650

    def on_data(self, data):
        tweet = json.loads(data)
        user = tweet.get('user')
        if user.get('lang') == 'pt':
            self.cont_tweet = self.cont_tweet + 1
            try:
                print("%i id: %i lang: %s texto: %s" % (self.cont_tweet, tweet.get('id'), user.get('lang'),
                                                        tweet.get('text')))
                file = open('twitter_data.csv', mode='a', encoding='utf-8')
                writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([tweet.get('id'), tweet.get('created_at'), tweet.get('text'), user.get('id_str'),
                                 user.get('name'), user.get('screen_name'), user.get('followers_count'),
                                 user.get('location'), user.get('lang')])
            except BaseException as exception:
                print('Erro: ' + exception)
        if self.cont_tweet >= self.max_tweets:
            file.close()
            return False


def coletar_tweets():
    access_token = "862079649320513536-g5otIX51xpbxYHDTxTkMhH5DXjOsBCb"
    access_token_secret = "22x2svzcLJqt9s6z55LDuwBqY1B1HEmh6zLB6AKPJ3yKB"
    consumer_key = "KlMCixdJcunVAa4pMLgV90gBl"
    consumer_secret = "KqMabppknibQjXTFeRcWvelWHETM7RqE7DiVJ8mDEBYc03dfMz"

    tl = TwitterListener()
    oauth = OAuthHandler(consumer_key, consumer_secret)
    oauth.set_access_token(access_token, access_token_secret)

    stream = Stream(oauth, tl)
    stream.filter(track=['trump'])


coletar_tweets()
