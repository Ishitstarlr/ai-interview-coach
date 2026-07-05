import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from resume_parser import ResumeParser

parser = ResumeParser()

resume = parser.parse("data/resumes/sample_resume.pdf")

print("\nResume Dictionary:\n")

for key, value in resume.items():

    print(f"{key}:\n")

    print(value)

    print("-" * 50)