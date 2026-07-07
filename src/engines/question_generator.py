class QuestionGenerator:

    def generate_first_question(self, resume, jd, match_result):

        missing = match_result["missing_skills"]

        if missing:

            topic = missing[0]

            return {

                "id": 1,

                "topic": topic,

                "difficulty": "Easy",

                "reason": "Missing Skill",

                "source": "JD",

                "question": f"What is {topic}?"

            }

        return {

            "id": 1,

            "topic": None,

            "difficulty": "Easy",

            "reason": "General",

            "source": "Resume",

            "question": "Tell me about yourself."
        }