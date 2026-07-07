from utils.preprocessor import preprocess
from utils.skill_extractor import SkillExtractor


class JDParser:

    def __init__(self):
        self.extractor = SkillExtractor()

    def parse(self, filepath):

        with open(filepath, "r") as file:
            raw_text = file.read()

        cleaned_text = preprocess(raw_text)

        skills = self.extractor.extract(cleaned_text)

        jd_data = {
            "raw_text": raw_text,
            "cleaned_text": cleaned_text,
            "skills": skills,
            "company": None,
            "role": None
        }

        return jd_data