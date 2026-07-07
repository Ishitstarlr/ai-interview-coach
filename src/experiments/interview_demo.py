import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parsers.resume_parser import ResumeParser
from parsers.jd_parser import JDParser
from engines.jd_matcher import JDMatcher
from engines.question_generator import QuestionGenerator
from engines.interview_engine import InterviewEngine

# Create objects
resume_parser = ResumeParser()
jd_parser = JDParser()
matcher = JDMatcher()
generator = QuestionGenerator()
engine = InterviewEngine(generator)

# Parse resume and JD
resume = resume_parser.parse("data/resumes/sample_resume.pdf")
jd = jd_parser.parse("data/job_descriptions/software_engineer.txt")

# Match them
match_result = matcher.match(resume, jd)
print(match_result)
# Start interview
session = engine.start_interview(
    resume,
    jd,
    match_result
)

print("=" * 50)
print("INTERVIEW STARTED")
print("=" * 50)

question = session.current_question

print(f"Question ID : {question['id']}")
print(f"Topic       : {question['topic']}")
print(f"Difficulty  : {question['difficulty']}")
print(f"Reason      : {question['reason']}")
print(f"Source      : {question['source']}")
print()
print(question["question"])