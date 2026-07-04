from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download("wordnet")

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = [
    "playing",
    "played",
    "running",
    "studies",
    "better",
    "feet",
    "amazing"
]

print(f"{'Word':<12} {'Stem':<12} {'Lemma':<12}")

for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print(f"{word:<12} {stem:<12} {lemma:<12}")

print(lemmatizer.lemmatize("playing", pos="v"))
print(lemmatizer.lemmatize("played", pos="v"))
print(lemmatizer.lemmatize("running", pos="v"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("amazing", pos="v"))