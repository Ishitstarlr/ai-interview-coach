import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parsers.resume_parser import ResumeParser
from parsers.jd_parser import JDParser
from engines.jd_matcher import JDMatcher

resume_parser = ResumeParser()
jd_parser = JDParser()
matcher = JDMatcher()

resume_data = resume_parser.parse("data/resumes/sample_resume.pdf")

jd_data = jd_parser.parse("data/job_descriptions/software_engineer.txt")

result = matcher.match(resume_data, jd_data)

print("=" * 50)
print("MATCH RESULT")
print("=" * 50)

for key, value in result.items():
    print(f"\n{key}:")

    if isinstance(value, list):
        for item in value:
            print("-", item)
    else:
        print(value)