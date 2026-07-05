import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.pdf_parser import PDFParser

parser = PDFParser()

text = parser.extract_text("data/resumes/sample_resume.pdf")

print(text)