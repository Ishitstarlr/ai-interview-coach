from models.interview_session import InterviewSession


class InterviewEngine:

    def __init__(self, question_generator, evaluator):

        self.question_generator = question_generator
        self.evaluator = evaluator

    def start_interview(self, resume, jd, match_result):

        session = InterviewSession()

        session.current_question = self.question_generator.get_next_question(
            session,
            resume,
            jd,
            match_result
        )

        return session

    def submit_answer(self, session, answer, resume, jd, match_result):

        evaluation = self.evaluator.evaluate(
            session.current_question,
            answer
        )

        interaction = {

            "question": session.current_question,

            "answer": {
                "text": answer
            },

            "evaluation": evaluation

        }

        session.add_interaction(interaction)

        next_question = self.question_generator.get_next_question(
            session,
            resume,
            jd,
            match_result
        )

        session.current_question = next_question

        return {

            "evaluation": evaluation,

            "next_question": next_question

        }