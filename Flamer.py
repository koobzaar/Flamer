import sys
from time import sleep

# Instânciando as classes que manuzeiam o bot
from modules.twitterAuth import *
from modules.twitterHandler import *
from modules.analizeEmotions import *
from modules.insultingHandler import *

TwitterAPI = TwitterAuth().getAPI()
Twitter = TwitterHandler(TwitterAPI)

Credenciais = TwitterAuth().returnCredentials()
Insultador = InsultingHandler()


# Listener que aguarda os tweets, analisa as emoções e responde.
class Flamer(tweepy.Stream):
    def on_status(self, status):
        # Verifica se o tweet é um retweet
        emocao = str(TweetAnalizer().analize(status))
        xingamento = Insultador.getInsult(emocao)
        Twitter.reply(status, xingamento)
        Twitter.favorite(status)
        sleep(2)

    def on_error(self, status_code):
        if status_code == 420:
            return False

    def on_timeout(self):
        print("Timeout, reconnecting...")
        return True

    def on_exception(self, exception):
        print(exception)
        return True

# Inicia o listener usando as credenciais do Twitter API, sendo elas respectivamente:
#                    API Key   |   API Secret  |   Acess Token  |  Secret Token
listener = Flamer(Credenciais[0], Credenciais[1], Credenciais[2], Credenciais[3])

# Define quem vai ser o target do listener
listener.filter(follow=[os.getenv('TWITTER_TARGET_USER_ID')])