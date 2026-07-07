class InterviewSession:

    def __init__(self):

        self.history = []

        self.current_question = None

        self.weak_topics = set()

        self.strong_topics = set()

    def add_interaction(self, interaction):

        self.history.append(interaction)

    def get_progress(self, total_questions):

        return len(self.history) / total_questions * 100