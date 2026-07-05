class SkillExtractor:

    def __init__(self):

        self.skills = {
            "python",
            "java",
            "c++",
            "sql",
            "machine learning",
            "deep learning",
            "tensorflow",
            "pytorch",
            "docker",
            "kubernetes",
            "aws",
            "azure",
            "gcp",
            "react",
            "nodejs",
            "flask",
            "django",
            "git",
            "linux",
            "mongodb",
            "mysql",
            "postgresql",
            "pandas",
            "numpy",
            "scikit-learn",
            "nlp"
        }

    def extract(self, text):

        text = text.lower()

        found = []

        for skill in self.skills:

            if skill in text:
                found.append(skill)

        return sorted(found)