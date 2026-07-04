import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess(text):

    tokens = word_tokenize(text)

    tokens = [word.lower() for word in tokens]

    tokens = [
        word
        for word in tokens
        if word.isalpha()
    ]

    tokens = [
        word
        for word in tokens
        if word not in stop_words
    ]

    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return " ".join(tokens)

sentence = "I love learning NLP with Python! It is amazing."

print(preprocess(sentence))