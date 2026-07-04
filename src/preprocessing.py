import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")

text = "I love learning NLP with Python! It is amazing."

# Tokenization
tokens = word_tokenize(text)

# Lowercase
lower_tokens = [word.lower() for word in tokens]

# Remove stopwords & punctuation
stop_words = set(stopwords.words("english"))

filtered_tokens = [
    word
    for word in lower_tokens
    if word.isalpha() and word not in stop_words
]

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [
    stemmer.stem(word)
    for word in filtered_tokens
]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [
    lemmatizer.lemmatize(word)
    for word in filtered_tokens
]

print("Filtered Tokens:")
print(filtered_tokens)

print("\nStemmed Tokens:")
print(stemmed_tokens)

print("\nLemmatized Tokens:")
print(lemmatized_tokens)