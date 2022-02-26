import random


# Instanciando todos os insultos
with open('./insults/forNegativeTweets.fodase', 'r') as negInsults:
    negativeInsults = negInsults.read().splitlines()
with open('./insults/forPositiveTweets.fodase', 'r') as posInsults:
    positiveInsults = posInsults.read().splitlines()
with open('./insults/forNeutralTweets.fodase', 'r') as neutralInsults:
    neutralInsults = neutralInsults.read().splitlines()


# Função para retornar um insulto aleatório com base na emoção do tweet
class InsultingHandler:
    def __init__(self):
        self.negativeInsults = negativeInsults
        self.positiveInsults = positiveInsults
        self.neutralInsults = neutralInsults

    def getInsult(self, insultType):
        print(insultType)
        if(insultType == 'pos'):
            return positiveInsults[random.randint(0, len(positiveInsults) - 1)]
        elif(insultType == 'neg'):
            return negativeInsults[random.randint(0, len(negativeInsults) - 1)]
        elif(insultType == 'neu'):
            return neutralInsults[random.randint(0, len(neutralInsults) - 1)]
        else:
            return 'Tipo de insulto não encontrado'