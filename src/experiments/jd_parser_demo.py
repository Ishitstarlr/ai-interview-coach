import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.jd_parser import JDParser

parser = JDParser()

jd_data = parser.parse("data/job_descriptions/software_engineer.txt")

for key, value in jd_data.items():
    print(f"{key}:\n")
    print(value)
    print("-" * 40)