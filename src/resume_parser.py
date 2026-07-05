from utils.pdf_parser import PDFParser
from utils.preprocessor import preprocess
from utils.skill_extractor import SkillExtractor


class ResumeParser:

    def __init__(self):

        self.pdf_parser = PDFParser()
        self.skill_extractor = SkillExtractor()

    def parse(self, pdf_path):

        raw_text = self.pdf_parser.extract_text(pdf_path)

        cleaned_text = preprocess(raw_text)

        skills = self.skill_extractor.extract(cleaned_text)

        resume_data = {

            "raw_text": raw_text,

            "cleaned_text": cleaned_text,

            "skills": skills

        }

        return resume_data