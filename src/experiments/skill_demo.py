import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.pdf_parser import PDFParser
from utils.skill_extractor import SkillExtractor

parser = PDFParser()
extractor = SkillExtractor()

text = parser.extract_text("data/resumes/sample_resume.pdf")

skills = extractor.extract(text)

print("Detected Skills:\n")

for skill in skills:
    print("-", skill)