import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

class NaturalLanguageProcessing:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def tokenize_text(self, text):
        tokens = word_tokenize(text)
        return tokens

    def analyze_sentiment(self, text):
        sentiment = self.sia.polarity_scores(text)
        return sentiment
