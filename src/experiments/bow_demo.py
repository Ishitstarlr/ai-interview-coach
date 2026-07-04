from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "I love Python",
    "Python is amazing",
    "I love Machine Learning"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(documents)

print("Vocabulary:")
print(vectorizer.vocabulary_)

print("\nFeature Matrix:")
print(X.toarray())