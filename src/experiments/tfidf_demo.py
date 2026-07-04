from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I love Python",
    "Python is amazing",
    "I love Machine Learning"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(documents)

print("Vocabulary:")
print(vectorizer.vocabulary_)

print("\nTF-IDF Matrix:")
print(X.toarray())