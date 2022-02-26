import tweepy,os
from dotenv import load_dotenv
load_dotenv()

class TwitterAuth:
    # Credenciais da API do Twitter retiradas do .env
    def __init__(self):
        self.__twitterKeyAPI = os.getenv("TWITTER_API_KEY")
        self.__twitterSecretAPI = os.getenv("TWITTER_API_SECRET")
        self.__twitterAcessToken = os.getenv("TWITTER_ACESS_TOKEN")
        self.__twitterSecretToken = os.getenv("TWITTER_SECRET_TOKEN")

    # Método privado para autenticação da API do Twitter
    def __authAPI(self):
        print("Logando utilizando a chave de API: " + self.__twitterKeyAPI)
        auth = tweepy.OAuthHandler(self.__twitterKeyAPI, self.__twitterSecretAPI)
        auth.set_access_token(self.__twitterAcessToken, self.__twitterSecretToken)
        return auth

    # Método de retorno da API do Twitter para uso externo à classe
    def getAPI(self):
        api = tweepy.API(self.__authAPI())
        return api
    
    def returnCredentials(self):
        return self.__twitterKeyAPI, self.__twitterSecretAPI, self.__twitterAcessToken, self.__twitterSecretToken