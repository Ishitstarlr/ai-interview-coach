from sklearn.feature_extraction.text import TfidfVectorizer


class InterviewVectorizer:

    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit(self, documents):
        return self.vectorizer.fit_transform(documents)

    def transform(self, documents):
        return self.vectorizer.transform(documents)

    def get_vocabulary(self):
        return self.vectorizer.vocabulary_