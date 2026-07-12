class QuestionGenerator:

    def get_next_question(self, session, resume, jd, match_result):

        missing = match_result["missing_skills"]

        asked_topics = {
            interaction["question"]["topic"]
            for interaction in session.history
        }

        remaining = [
            skill
            for skill in missing
            if skill not in asked_topics
        ]

        if not remaining:
            return None

        topic = remaining[0]

        return {

            "id": len(session.history) + 1,

            "topic": topic,

            "difficulty": "Easy",

            "reason": "Missing Skill",

            "source": "JD",

            "question": f"What is {topic}?"

        }