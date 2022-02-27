
from fileinput import filename
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente
load_dotenv()

class TwitterHandler:
    def __init__(self, api):
        self.api = api
        self.targetUser = os.getenv("TWITTER_TARGET_USER")
        self.targetUserID = os.getenv("TWITTER_TARGET_USER_ID")

    def get_tweets(self, user):
        tweets = self.api.user_timeline(user)
        print(tweets)
        return tweets
    
    def tweet(self, text):
        self.api.update_status(text)
        print("Tuítado: " + text)
        return True

    def retweet(self, tweet):
        self.api.retweet(str(tweet.id))
        print("Retweetado: " + tweet.text)
        return True
    
    def favorite(self, tweet):
        self.api.create_favorite(str(tweet.id))
        print("Favoritado: " + tweet.text)
        return True
    
    def reply(self, tweet, text):
        print("Respondendo a: " + str(tweet.text))
        self.api.update_status(status=text, in_reply_to_status_id=str(tweet.id), auto_populate_reply_metadata=True)
        print("Respondido: " + tweet.text)
        return True
    
    # Tweet media e reply with media, no atributo media, deve conter a url LOCAL do arquivo.
    def tweetMedia(self, tweet, media):
        self.api.update_status_with_media(filename=media, status=tweet)
        print("Tuítado: " + tweet)
        return True
    
    def replyWithMedia(self, tweet, text, media):
        print("Respondendo a: " + str(tweet.text))
        self.api.update_status_with_media(status=text, in_reply_to_status_id=str(tweet.id), auto_populate_reply_metadata=True, filename=media)
        print("Respondido: " + tweet.text)
        return True
    
    def getTweets (self):
        return self.api.user_timeline(screen_name=self.targetUser)