
# Convert similarity to score
...
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.preprocessor import preprocess


def compute_similarity(expected_answer, candidate_answer):

    expected = preprocess(expected_answer)

    candidate = preprocess(candidate_answer)

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([
        expected,
        candidate
    ])

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    return similarity