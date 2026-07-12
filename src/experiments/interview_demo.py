import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from engines.evaluator import Evaluator
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
evaluator = Evaluator()

engine = InterviewEngine(
    generator,
    evaluator
)

# Parse resume and JD
resume = resume_parser.parse("data/resumes/sample_resume.pdf")
jd = jd_parser.parse("data/job_descriptions/software_engineer.txt")

# Match them
match_result = matcher.match(resume, jd)
# Start interview
session = engine.start_interview(
    resume,
    jd,
    match_result
)
print("=" * 50)
print("INTERVIEW STARTED")
print("=" * 50)

while session.current_question is not None:

    question = session.current_question

    print("\n" + "=" * 60)

    print(f"Question {question['id']} / {len(match_result['missing_skills'])}")
    print(f"Topic      : {question['topic']}")

    print(f"Difficulty : {question['difficulty']}")

    print(f"Reason     : {question['reason']}")

    print("-" * 60)

    print(question["question"])

    print("=" * 60)

    answer = input("\nYour Answer: ")

    result = engine.submit_answer(
        session,
        answer,
        resume,
        jd,
        match_result
    )

    print("\n" + "-" * 60)
    print("Evaluation")
    print("-" * 60)

    
    print(f"Similarity : {result['evaluation']['similarity']:.2f}")
    print(f"Score      : {result['evaluation']['score']}")
    print(f"Feedback   : {result['evaluation']['feedback']}")

    print("-" * 60)
    session.current_question = result["next_question"]

print("\n" + "=" * 50)
print("INTERVIEW FINISHED")
print("=" * 50)