from models.interview_session import InterviewSession


class InterviewEngine:

    def __init__(self, question_generator):

        self.question_generator = question_generator

    def start_interview(self, resume, jd, match_result):

        session = InterviewSession()

        question = self.question_generator.generate_first_question(
            resume,
            jd,
            match_result
        )

        session.current_question = question

        return session