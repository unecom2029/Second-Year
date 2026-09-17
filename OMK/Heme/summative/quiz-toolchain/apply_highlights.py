"""Merge Key Findings (vignette highlights) into an existing Jeevs Edition quiz file.

usage: python3 apply_highlights.py HIGHLIGHTS_PY ["Target File.html"]

The quiz engine already supports highlights — getStemHTMLForDisplay() marks each phrase in the
stem, but only after questionIsSubmitted(index) is true, so nothing shows until the learner has
answered. This script only supplies the data: it sets q["highlights"] on the numbered questions
and leaves every other field, and the rest of the file, untouched.

Before writing anything it verifies that every phrase actually occurs in its stem, using the same
whitespace-normalised comparison the browser makes. A phrase that would silently fail to mark is
a hard error, not a warning — the whole point of the feature is that the highlight appears.
"""
import re, json, importlib.util, os, sys, shutil, time
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
SUMM = os.path.dirname(HERE) + os.sep

HL_PY  = sys.argv[1]
TARGET = SUMM + (sys.argv[2] if len(sys.argv) > 2 else "Jeevs edition _ summative review.html")

sp = importlib.util.spec_from_file_location("hl", os.path.join(HERE, HL_PY))
mod = importlib.util.module_from_spec(sp); sp.loader.exec_module(mod)
HIGHLIGHTS = mod.HIGHLIGHTS

VH_CATS = ["finding", "mechanism", "term", "pattern", "workup"]


def flat(stem):
    """Approximate the browser's vhTextMap(): the lab panel renders as a table whose cells are
    test / result / reference range, so the literal "(N=…)" wrapper disappears and every run of
    whitespace collapses to one space."""
    return re.sub(r"\s+", " ", re.sub(r"\(N=[^)]*\)", " ", stem)).strip()


s = open(TARGET, encoding="utf-8").read()
for feature, why in [("getStemHTMLForDisplay", "highlight renderer"),
                     ("questionIsSubmitted", "reveal-after-answer gate"),
                     ("vh-cat-finding", "highlight CSS"),
                     ("vhPanel", "highlight detail panel")]:
    assert feature in s, f"target is missing the {why} — this file cannot show Key Findings"

mq = re.search(r'var PRELOADED_QUESTIONS_JSON="(.*?)";\n', s, re.S)
assert mq, "PRELOADED_QUESTIONS_JSON not found"
qs = json.loads(json.loads('"' + mq.group(1) + '"'))

# ── verify before touching anything ───────────────────────────────────────────
errs, applied, marks = [], 0, 0
for n, hl in sorted(HIGHLIGHTS.items()):
    if not 1 <= n <= len(qs):
        errs.append(f"Q{n}: out of range (file has {len(qs)} questions)"); continue
    stem = flat(qs[n - 1]["stem"])
    seen = set()
    for i, h in enumerate(hl):
        for k in ("text", "cat", "title", "body"):
            if not h.get(k): errs.append(f"Q{n} highlight {i+1}: empty {k}")
        if h.get("cat") not in VH_CATS:
            errs.append(f"Q{n} highlight {i+1}: unknown category {h.get('cat')!r}")
        phrase = re.sub(r"\s+", " ", h["text"]).strip()
        if phrase not in stem:
            errs.append(f"Q{n} highlight {i+1}: phrase not found in stem — {phrase[:70]!r}")
        elif phrase in seen:
            errs.append(f"Q{n} highlight {i+1}: duplicate phrase — {phrase[:50]!r}")
        else:
            # an earlier phrase that contains this one would swallow it before it could be marked
            for prev in seen:
                if phrase in prev or prev in phrase:
                    errs.append(f"Q{n} highlight {i+1}: overlaps another phrase — {phrase[:50]!r}")
                    break
            seen.add(phrase)

if errs:
    print(f"{len(errs)} problem(s); nothing written:")
    for e in errs: print("  •", e)
    sys.exit(1)

for n, hl in sorted(HIGHLIGHTS.items()):
    qs[n - 1]["highlights"] = [
        {"text": h["text"], "cat": h["cat"], "eyebrow": h.get("eyebrow", "KEY FINDING"),
         "title": h["title"], "body": h["body"]} for h in hl]
    applied += 1; marks += len(hl)

bak = TARGET + "." + time.strftime("%Y%m%d-%H%M%S") + ".prehl.bak"
shutil.copy2(TARGET, bak)
s = s[:mq.start()] + 'var PRELOADED_QUESTIONS_JSON=' + \
    json.dumps(json.dumps(qs, ensure_ascii=False), ensure_ascii=False) + ';\n' + s[mq.end():]
open(TARGET, "w", encoding="utf-8").write(s)

chk = json.loads(json.loads('"' + re.search(r'var PRELOADED_QUESTIONS_JSON="(.*?)";\n', s, re.S).group(1) + '"'))
assert len(chk) == len(qs), "question count changed"
for n, hl in HIGHLIGHTS.items():                       # this batch landed, verbatim
    assert chk[n - 1].get("highlights") == qs[n - 1]["highlights"], f"Q{n} did not round-trip"
total = sum(1 for q in chk if q.get("highlights"))
print(f"highlights applied to {applied} questions ({marks} marks) in {os.path.basename(TARGET)}"
      f" — {total}/{len(chk)} questions now carry highlights")
print(f"backup: {os.path.basename(bak)}")
