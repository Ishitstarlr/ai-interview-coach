from utils.tfidf_similarity import compute_similarity


class Evaluator:

    def evaluate(self, question, answer):

        topic = question["topic"]

        similarity = compute_similarity(
            question["expected_answer"],
            answer
        )

        score = round(similarity * 10)

        if score >= 8:
            feedback = "Excellent answer."

        elif score >= 6:
            feedback = "Good answer."

        elif score >= 4:
            feedback = "Partial understanding."

        else:
            feedback = "Needs improvement."

        return {

            "score": score,

            "feedback": feedback,

            "topic": topic,

            "similarity": similarity

        }