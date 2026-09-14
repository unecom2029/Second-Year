"""Append a batch of questions to an EXISTING Jeevs Edition quiz file, in place.

usage: FIGDIR=figs python3 append_quiz.py QUESTIONS_PY TAGS_PY ["Target File.html"]

Unlike build_quiz.py (which clones the template and writes a NEW quiz), this script
edits one live quiz file: it merges new questions into PRELOADED_QUESTIONS_JSON and new
figures into QUIZ_FIGURES, leaving everything else — including the builder's LO-block,
normalizer and CSS patches — untouched. A timestamped .bak is written first.

Same authoring rules as build_quiz.py: LO tags come from the tags module, lab blocks are
rewritten into the template's native row syntax, figures are read from FIGDIR/<key>.jpg.
"""
import re, json, base64, importlib.util, os, sys, shutil, time
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
SUMM = os.path.dirname(HERE) + os.sep
REVIEW = SUMM + "OMK_2A_Heme_Summative_3_Objective_Review.html"
LOMAP_PATH = SUMM + "heme_summative3_lo_question_map.json"

QUESTIONS_PY = sys.argv[1]
TAGS_PY      = sys.argv[2]
TARGET       = SUMM + (sys.argv[3] if len(sys.argv) > 3 else "Jeevs edition _ summative review.html")
FIGDIR       = os.environ.get("FIGDIR", os.path.join(HERE, "figs"))


def load(name, path):
    sp = importlib.util.spec_from_file_location(name, os.path.join(HERE, path))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m


Q = load("questions", QUESTIONS_PY).Q
TAGS = load("tags", TAGS_PY).LO_TAGS
LOMAP = json.load(open(LOMAP_PATH))["objectives"]
assert len(TAGS) == len(Q), f"{len(Q)} questions but {len(TAGS)} LO tag entries"

# ── 1. LO tags → q["los"] (identical semantics to build_quiz.py) ──────────────
REV = open(REVIEW, encoding="utf-8").read()
SECNUM = {}
for m in re.finditer(r'<section class="section" id="([^"]+)">', REV):
    lab = re.search(r'<p class="section-label">Section (\d+)', REV[m.end():m.end() + 1500])
    if lab: SECNUM[m.group(1)] = "§" + lab.group(1)

for i, q in enumerate(Q, 1):
    q["los"] = []
    seen = set()
    for tag in TAGS[i]:
        lo, anc = tag if isinstance(tag, (tuple, list)) else (tag, None)
        assert lo not in seen, f"Q{i}: LO {lo} tagged twice"
        seen.add(lo)
        e = LOMAP[str(lo)]
        a = anc or (e["anchors"][0] if e["anchors"] else "")
        assert a in SECNUM, f"Q{i}: anchor {a!r} not found in review file"
        q["los"].append({"n": lo, "t": e["objective"], "a": a, "s": SECNUM[a]})

# ── 2. Lab blocks → the template's native lab-panel row syntax ────────────────
LAB_LINE = re.compile(r'^(.*?)\s((?:[<>]?\d).*)$')
LAB_BLOCK = re.compile(r'(Laboratory studies[^\n:]*:)\n((?:[^\n]+\n?)+?)(?=\n|$)')


def _native(block, qn):
    rows = []
    for ln in block.strip().split("\n"):
        ln = ln.strip()
        if not ln: continue
        mm = LAB_LINE.match(ln)
        if not mm: raise ValueError(f"Q{qn}: unparseable lab line: {ln!r}")
        if "(N=" not in mm.group(2): raise ValueError(f"Q{qn}: lab line has no (N=…) range: {ln!r}")
        rows.append(f"  {mm.group(1).strip()}  {mm.group(2).strip()}")
    if len(rows) < 2: raise ValueError(f"Q{qn}: native lab panel needs ≥2 rows")
    return "\n".join(rows)


for i, q in enumerate(Q, 1):
    q["stem"] = LAB_BLOCK.sub(lambda mo: mo.group(1) + "\n" + _native(mo.group(2), i), q["stem"])

# ── 3. Read the target quiz and assert it is a built Jeevs Edition file ───────
s = open(TARGET, encoding="utf-8").read()
for feature, why in [("loBlockHTML", "LO block patch"), ("los:Array.isArray", "question normalizers"),
                     ("formatStemText", "native stem formatting"), ("lab-row", "native lab panels")]:
    assert feature in s, f"target file lacks {why} — is it a built Jeevs Edition quiz?"

mq = re.search(r'var PRELOADED_QUESTIONS_JSON="(.*?)";\n', s, re.S)
assert mq, "PRELOADED_QUESTIONS_JSON not found"
existing = json.loads(json.loads('"' + mq.group(1) + '"'))
mf = re.search(r'var QUIZ_FIGURES=(\{.*?\});\n', s, re.S)
assert mf, "QUIZ_FIGURES not found"
figs = json.loads(mf.group(1))

# ── 4. Merge ─────────────────────────────────────────────────────────────────
old_stems = {q["stem"][:120] for q in existing}
for i, q in enumerate(Q, 1):
    if q["stem"][:120] in old_stems:
        raise SystemExit(f"Q{i} looks already appended (duplicate opening) — aborting, nothing written")

for k in sorted({q[k] for q in Q for k in ("image", "explanationImage") if q.get(k)}):
    if k in figs: continue
    p = os.path.join(FIGDIR, k + ".jpg")
    assert os.path.exists(p), f"figure file missing: {p}"
    figs[k] = "data:image/jpeg;base64," + base64.b64encode(open(p, "rb").read()).decode()

merged = existing + Q
s = s[:mq.start()] + 'var PRELOADED_QUESTIONS_JSON=' + \
    json.dumps(json.dumps(merged, ensure_ascii=False), ensure_ascii=False) + ';\n' + s[mq.end():]
mf = re.search(r'var QUIZ_FIGURES=(\{.*?\});\n', s, re.S)   # offsets moved
s = s[:mf.start()] + 'var QUIZ_FIGURES=' + json.dumps(figs) + ';\n' + s[mf.end():]

shutil.copy2(TARGET, TARGET + "." + time.strftime("%Y%m%d-%H%M%S") + ".bak")
open(TARGET, "w", encoding="utf-8").write(s)
print(f"appended {len(Q)} questions to {os.path.basename(TARGET)} "
      f"(now {len(merged)}), {len(figs)} figures, {len(s)/1e6:.2f} MB")
