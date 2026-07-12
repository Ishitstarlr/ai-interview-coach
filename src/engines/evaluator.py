class Evaluator:

    def evaluate(self, question, answer):

        topic = question["topic"]

        answer = answer.lower()

        if topic and topic.lower() in answer:

            score = 8
            feedback = "Good! You mentioned the key topic."

        else:

            score = 3
            feedback = "The answer does not mention the expected topic."

        return {

            "score": score,

            "feedback": feedback,

            "topic": topic

        }