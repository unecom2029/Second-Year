"""Print a one-line index of every question in the Hardest Exam file.

usage: python3 index_hardest.py [target.html] > hardest_exam_question_index.txt

Each line is:  <n> | LO <tags> | <first sentence of the explanation = the diagnosis> | KEY: <answer>

This is the input to the card-coverage mapping described in QUIZ_BUILD_METHOD.md
("Hardest Exam — card coverage map"): read the index, decide which High-Yield
Checklist card each question tests, and write questions for the cards that come
back with no question against them.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SUMM = os.path.dirname(HERE) + os.sep
TARGET = sys.argv[1] if len(sys.argv) > 1 else SUMM + "Hardest exam/Jeevs Edition - Hardest Exam.html"

s = open(TARGET, encoding="utf-8").read()
qs = json.loads(json.loads('"' + re.search(r'var PRELOADED_QUESTIONS_JSON="(.*?)";\n', s, re.S).group(1) + '"'))

for i, q in enumerate(qs, 1):
    los = ",".join(str(l["n"]) for l in q.get("los", []))
    key = q["choices"][q["correct"]][3:][:46]
    dx = re.split(r'(?<=[.!])\s', q["explanation"].strip())[0][:70]
    print(f"{i:>3} | LO {los:<7} | {dx} | KEY: {key}")
