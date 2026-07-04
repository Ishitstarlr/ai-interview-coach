import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.preprocessor import preprocess
from utils.vectorizer import InterviewVectorizer

documents = [
    "I love Python and Machine Learning.",
    "Python is amazing for AI.",
    "Machine Learning uses Python."
]

cleaned_documents = [
    preprocess(document)
    for document in documents
]

print("Cleaned Documents:")

for document in cleaned_documents:
    print(document)

vectorizer = InterviewVectorizer()

X = vectorizer.fit(cleaned_documents)

print("\nVocabulary:")
print(vectorizer.get_vocabulary())

print("\nTF-IDF Matrix:")
print(X.toarray())