"""Rebalance answer-choice lengths in the built quiz, and in the source modules.

usage: python3 rebalance_options.py ["Target File.html"]

Why this exists: an audit of all 154 questions found the keyed answer was the SHORTEST option in
28.6% of items (chance is about 19%) — the mirror image of the classic "longest answer is correct"
tell, and just as exploitable. EDITS below fixes the worst offenders, preferring to trim a wordy
distractor over padding the key.

In the built file the options are already lettered and `correct` is an index, so this script
re-sorts the edited option set alphabetically and remaps both `correct` and the `wrongExplanations`
keys. It also applies the same text substitutions to the questions_hardest*.py modules, so a
rebuild from source reproduces the change.
"""
import re, json, os, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
SUMM = os.path.dirname(HERE) + os.sep
TARGET = SUMM + (sys.argv[1] if len(sys.argv) > 1 else "Hardest exam/Jeevs Edition - Hardest Exam.html")

# {question number: {old option text: new option text}}
EDITS = {
    1:  {"Marrow of the axial skeleton": "Axial skeleton marrow",
         "Marrow of the long bones": "Long bone marrow"},
    40: {"Production of a polysaccharide capsule": "Production of a capsule",
         "Survival within resting macrophages": "Survival inside macrophages"},
    44: {"Increased numbers of megakaryocytes": "Increased numbers of megakaryocytes in the marrow"},
    45: {"Development of antibodies against transfused platelets": "Antibodies against transfused platelets",
         "Recurrent infection stimulating antibody production": "Infection stimulating antibody production"},
    47: {"Autoantibody inhibition of ADAMTS13": "Autoantibody inhibition of ADAMTS13 activity"},
    48: {"Corticosteroids and intravenous immunoglobulin": "Corticosteroids and immunoglobulin",
         "Supportive care with dialysis alone": "Dialysis and supportive care",
         "Eculizumab": "Eculizumab therapy"},
    49: {"Urinary loss of antithrombin": "Loss of antithrombin in the urine",
         "Antibodies against heparin-platelet factor 4 complexes": "Antibodies to platelet factor 4 complexes",
         "A lupus anticoagulant interfering with the assay": "A lupus anticoagulant affecting the assay",
         "Rapid hepatic clearance of unfractionated heparin": "Rapid hepatic clearance of heparin"},
    66: {"Infection or hemorrhage": "Overwhelming infection or hemorrhage"},
    92: {"Elevation of the limb above the level of the heart": "Elevation of the limb",
         "Observation with serial neurovascular checks": "Serial neurovascular checks",
         "Compression ultrasonography of the leg": "Compression ultrasonography",
         "Measurement of serum creatine kinase": "Serum creatine kinase level"},
    102: {"Bone marrow aspiration with Prussian blue staining": "Marrow aspiration with iron staining"},
    103: {"Transfuse 1 unit now and reassess before giving any further units": "Transfuse 1 unit now and reassess",
          "Transfuse 2 units because her coronary disease requires a higher threshold": "Transfuse 2 units for her coronary disease",
          "Transfuse 2 units to a target hemoglobin above 10 g/dL": "Transfuse 2 units to a hemoglobin above 10 g/dL",
          "Withhold transfusion and start an erythropoiesis-stimulating agent": "Withhold transfusion and start epoetin alfa"},
    111: {"Echinocytes, indicating uremia": "Echinocytes, indicating renal failure",
          "Acanthocytes, indicating severe liver disease": "Acanthocytes, indicating liver disease"},
    139: {"Deferral of antiretroviral therapy for 3 months": "Deferral of antiretroviral therapy"},
    143: {"Apply the PE rule-out criteria and discharge if negative": "Apply the PE rule-out criteria"},
    152: {"Radiation to the retroperitoneal nodes": "Radiotherapy"},
    153: {"Intravenous furosemide for circulatory overload": "Intravenous furosemide",
          "Permanent discontinuation of retinoic acid and arsenic": "Permanent withdrawal of retinoic acid",
          "Platelet and cryoprecipitate transfusion": "Cryoprecipitate transfusion"},
}

MODULE_FOR = lambda n: f"questions_hardest0{min((n - 1) // 20 + 1, 8)}.py"

s = open(TARGET, encoding="utf-8").read()
mq = re.search(r'var PRELOADED_QUESTIONS_JSON="(.*?)";\n', s, re.S)
qs = json.loads(json.loads('"' + mq.group(1) + '"'))

changed = 0
for n, sub in sorted(EDITS.items()):
    q = qs[n - 1]
    bodies = [c[3:] for c in q["choices"]]
    key = bodies[q["correct"]]
    wrong = {bodies[int(i)]: t for i, t in q["wrongExplanations"].items()}
    for old, new in sub.items():
        assert old in bodies, f"Q{n}: option not found: {old!r}"
        bodies[bodies.index(old)] = new
        if key == old:
            key = new
        if old in wrong:
            wrong[new] = wrong.pop(old)
    assert len(set(bodies)) == len(bodies), f"Q{n}: duplicate option text after edit"
    order = sorted(bodies, key=str.lower)                      # keep the alphabetisation discipline
    q["choices"] = [f"{chr(65 + i)}. {b}" for i, b in enumerate(order)]
    q["correct"] = order.index(key)
    q["wrongExplanations"] = {str(i): wrong[b] for i, b in enumerate(order) if i != q["correct"]}
    changed += 1

s = s[:mq.start()] + 'var PRELOADED_QUESTIONS_JSON=' + \
    json.dumps(json.dumps(qs, ensure_ascii=False), ensure_ascii=False) + ';\n' + s[mq.end():]
open(TARGET, "w", encoding="utf-8").write(s)
print(f"rebalanced {changed} questions in {os.path.basename(TARGET)}")

# ── keep the source modules in step ──────────────────────────────────────────
for n, sub in sorted(EDITS.items()):
    path = os.path.join(HERE, MODULE_FOR(n))
    src = open(path, encoding="utf-8").read()
    for old, new in sub.items():
        hits = src.count('"' + old + '"')
        if hits == 0:
            print(f"  ! {MODULE_FOR(n)}: {old!r} not found verbatim (line-wrapped?) — edit by hand")
            continue
        src = src.replace('"' + old + '"', '"' + new + '"')
    open(path, "w", encoding="utf-8").write(src)
print("source modules updated where the option text was on one line")
