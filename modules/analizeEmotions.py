
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

class TweetAnalizer:
    def __init__(self):
        self.translator = GoogleTranslator()
        self.sentiment = SentimentIntensityAnalyzer()

    def analize(self, tweet):
        # O tradutor só consegue lidar com traduções de até 5000 caracteres. Define para 4990 caracteres e coloca reticências no final.
        tweet_text = (tweet.text[:4990] + '..') if len(tweet.text) > 4990 else tweet.text
        tweet_text = GoogleTranslator(source='pt', target='en').translate(tweet_text)
        score = self.sentiment.polarity_scores(tweet_text)
        return max(score, key=score.get)