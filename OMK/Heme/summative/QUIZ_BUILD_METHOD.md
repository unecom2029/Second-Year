# How the "Jeevs Edition" quizzes are built

Handoff document. Written so a fresh Claude session (or a human) can produce the next
batch without re-deriving anything. Everything here was used to build
`Jeevs Edition - Hematopoiesis and Marrow Quiz.html` (batch 01, 20 questions).

Paths are absolute because the figure library lives outside the repo.

---

## 1. What this is

A series of self-contained HTML quizzes for the **OMK 2A Hematology Summative Exam 3**
(exam date 21 September 2026). Each batch covers one topic block, sourced from the
consolidated objective review file, tagged to the course learning objectives, and
saved into `OMK/Heme/summative/`.

Batches are built one topic block at a time, ~20 questions each.

---

## 2. Source of truth — read this before writing anything

**The authoritative source is:**

```
OMK/Heme/summative/OMK_2A_Heme_Summative_3_Objective_Review.html
```

This is a 59-section consolidation of every lecture, rebuilt against the
**21 September 2026 study guide (83 objectives)**. Questions are written **from its
numbered sections**, not from the raw lecture notes. The raw notes in
`week 10/Notes/`, `week 11/notes/`, `week 12/notes/` are useful for checking *what the
lecturer actually said* (see §7, "in-house vs board"), but the review file is what the
questions must map onto.

**Section → objective mapping lives in:**

```
OMK/Heme/summative/heme_summative3_lo_question_map.json
```

Structure:

```json
{
  "_meta": { "total_objectives": 83, "objectives_without_questions": [30, 47, 73] },
  "objectives": {
    "29": {
      "objective": "Given a clinical vignette with a presentation of anemia, ...",
      "sections": ["§2", "§3", "§5"],
      "anchors": ["s2-marrow", "s3-anemia-eval"],
      "coverage": "covered",
      "questions": [4, 17, 88],
      "needs_questions": false
    }
  }
}
```

`anchors` are the HTML `id`s of sections inside the review file. They are what the
LO chips deep-link to.

### Finding a block's native objectives

Each section of the review file carries `lo-badge` chips naming the objectives it
serves. To get a block's *native* objectives:

```bash
python3 - <<'PY'
import re
s=open("OMK_2A_Heme_Summative_3_Objective_Review.html",encoding="utf-8").read()
for sid in ["s1-hematopoiesis","s2-marrow"]:          # <- the block you are writing
    m=re.search(r'<section class="section" id="%s">\s*<div class="badge-row">(.*?)</div>'%sid,s,re.S)
    print(sid, re.findall(r'<span class="lo-badge(?: alt)?">LO (\d+)</span>', m.group(1)))
PY
```

For batch 01 this returned `s1-hematopoiesis → [2, 81, 83]` and `s2-marrow → [29, 65]`.

> **This step is not optional.** On the first build I skipped it and tagged questions
> with objectives from neighbouring blocks (anemia, iron, pharmacology), which made a
> Hematopoiesis & Marrow quiz look like it was testing half the course. See §9.

---

## 3. Question-writing rules

The house style spec is embedded in `OMK/Heme/summative/index.html` — search for
`function buildPrompt()`. It is a ~9,000-word NBME/NBOME item-writing brief. Read it
in full before writing. The parts that matter most:

- **Silent planning protocol** — pick the testing point, the correct answer, the TRAP
  (what a hurried reader picks), and the BURIED CLUE (the one quiet fact that decides
  it). Clue and decoy must be *different details*.
- **Distractor architecture** — build the option set as one homogeneous family. Twelve
  named families (differential set, same-pathway molecular set, factorial grid,
  direction-swap, ordered series, anatomic path, matched-set table, next-step set, …).
  Pick one per item and rotate across the batch.
- **Counterfactual test** — for every distractor you must be able to finish:
  *"This would be the answer if the vignette had said ___ instead."* That sentence is
  what goes into `wrongExplanations`.
- **Cover-the-options test** — a competent student reading the stem with options hidden
  should be able to state the answer.
- **Alphabetical option order** (or numeric/anatomic for ordered series). Never order
  by correctness.

### The heme data-consistency rules (mandatory — this is where machine-written items fail)

From the same prompt spec, section `HEMATOLOGY / ONCOLOGY MODULE`:

- **Hematocrit ≈ 3 × hemoglobin.** Write 8.9 g/dL with 27%, never with 41%.
- **MCV must match the described morphology** (micro <80, normo 80–100, macro >100).
- **Reticulocyte count is the master switch.** Destruction/loss with intact marrow →
  corrected retic >2–3%. Production defect → <2%.
  `corrected retic = retic% × (Hct ÷ 45)`
- **The hemolysis panel moves as a unit**: ↑LDH, ↓haptoglobin, ↑indirect bilirubin.
  If one is out of line, *that* is the testing point and the explanation must say so.
- **Iron studies form one coherent row.** Iron deficiency = ↓iron, **↑TIBC**, ↓ferritin,
  ↑RDW. Anemia of chronic disease = ↓iron, **↓TIBC**, normal/↑ferritin.
- **B12 vs folate**: both raise homocysteine; **only B12 raises methylmalonic acid**.
- Never write a "normal" value the chosen disease makes impossible — unless that is the trap.

---

## 4. Formatting requirements (Jeevs-specific, not in the base spec)

### Lab panels render as a three-column table

Lab values are **not** run together in a paragraph and **not** left as plain stacked
lines. They render as a bordered `TEST | RESULT | REFERENCE RANGE` table with zebra
striping and a footnote:

```
┌──────────────────────────────────────────────────────────────────────────┐
│ TEST                          RESULT            REFERENCE RANGE          │
├──────────────────────────────────────────────────────────────────────────┤
│ Hemoglobin                    8.6 g/dL          13.5–17.5 g/dL           │
│ Hematocrit                    26%               41%–53%                  │
│ Mean corpuscular volume       92 µm3            80–100 µm3               │
│ Leukocyte count               2,100/mm3         4,500–11,000/mm3         │
├──────────────────────────────────────────────────────────────────────────┤
│ Typical educational ranges are shown. Actual reference intervals vary by  │
│ laboratory, age, sex, and clinical context.                              │
└──────────────────────────────────────────────────────────────────────────┘
```

**You write it as plain text; the build converts it.** In the question `stem`, keep
writing the simple stacked form with real `\n` characters:

```
Laboratory studies show:
Hemoglobin 8.6 g/dL (N=13.5–17.5 g/dL)
Hematocrit 26% (N=41%–53%)
Mean corpuscular volume 92 µm3 (N=80–100 µm3)
Reticulocyte count 0.3% (N=0.5%–1.5%)
```

At build time `build_quiz.py`:

1. Finds any block starting `Laboratory studies…:` and running to the next blank line.
2. Parses each line into `{t: test, r: result, n: reference range}`. The split between
   test name and result is **the first token beginning with a digit, `<` or `>`** — which
   is why `Serum vitamin B12 480 pg/mL` and `Haptoglobin <10 mg/dL` both parse correctly.
3. Stores the structured panel on `q["labs"]` and replaces the block in the stem with a
   `[[LABS]]` marker.
4. At run time `getStemHTML()` swaps `[[LABS]]` for the rendered table via
   `labTableHTML(q)`.

Resulting question object:

```jsonc
"labs": {
  "title": "Laboratory studies show:",
  "rows": [
    { "t": "Hemoglobin", "r": "8.6 g/dL", "n": "13.5–17.5 g/dL" },
    { "t": "Hematocrit", "r": "26%",      "n": "41%–53%" }
  ]
}
```

If a line fails to parse the build **raises** rather than silently dropping it — fix the
line and rerun. You can also hand-write the `labs` object directly if a panel has an
unusual shape; the builder leaves an existing `labs` field alone as long as there is no
`Laboratory studies…:` block left in the stem.

CSS classes: `.labt` (container), `.labt-row`, `.labt-head`, `.labt-t` / `.labt-v` /
`.labt-n` (the three cells), `.labt-foot`. Collapses to a two-line stacked layout under
620 px. The table sets `white-space:normal` because the surrounding stem runs
`white-space:pre-line`.

### Prose line breaks

Everything outside the lab table still relies on real newlines in `stem`, so
`build_quiz.py` patches `white-space:pre-line` into **both** stem styles (`.qstem` for
the Study Hub UI, `.nb-question-stem` for the NBME UI). If you change templates,
re-apply this or the paragraph breaks silently disappear.

### Reference ranges on everything

The NBME convention is to give `(N=…)` only for analytes *not* on the standard lab
table. **Jeevs wants ranges on every value**, because he is studying from these, not
sitting them blind.

The canonical ranges are in `index.html` → `var LAB_SECTIONS = [...]` (sections: Serum,
CSF, Hematologic, Urine, BMI). Pull them from there so the numbers stay consistent with
the app's own built-in "Lab Values" reference panel:

```bash
python3 -c "
import re,json
s=open('index.html',encoding='utf-8').read()
d=json.loads(re.search(r'var\s+LAB_SECTIONS\s*=\s*(\[.*?\]);',s,re.S).group(1))
for sec in d:
    if sec['title']=='Hematologic':
        for r in sec['rows']:
            print(re.sub('<[^>]+>','',r.get('name','')), '|', re.sub('<[^>]+>','',r.get('us','')))
"
```

Note: ferritin, iron, TIBC, transferrin, LDH and bilirubin **are** on the table.
Haptoglobin, erythropoietin, B12, folate, methylmalonic acid and homocysteine are not.

---

## 5. Images

### Where they come from

Two libraries, both outside the repo:

| Library | Path | Notes |
|---|---|---|
| **AMBOSS** | `/Users/jeeval/Documents/Board Study/figures/amboss/` | ~2,970 files. Flat directory. Each figure is a `.png` **plus a matching `.txt`** containing the official caption, the anatomical description, and the source/licence line. |
| **UWorld** | `/Users/jeeval/Documents/Board Study/figures/Uworld images/` | Organised into 32 subject folders, e.g. `COMLEX 1 (Step1 + OMT1) - Hematology & Oncology/`, numbered `.jpg` files. |

**Always read the `.txt` sidecar before writing a caption.** It gives the stain, the
magnification, and what is actually visible — which is what the `imageCaption` must
describe. Example (`Aplastic anemia.txt`):

> Photomicrograph of a bone marrow biopsy specimen (H&E stain; medium power
> magnification). The marrow is hypocellular and shows fatty replacement.
> Source: … licensed under CC BY 4.0.

These are copyrighted third-party study figures embedded in a personal study file.
Fine for private revision; do not redistribute.

### Figures used in batch 01

| Key | AMBOSS source file | Used in |
|---|---|---|
| `fig_hematopoiesis` | `Hematopoiesis.png` | Q1, Q5 — explanation |
| `fig_cytokines` | `Hematopoiesis and important cytokines.png` | Q9 — explanation |
| `fig_retics` | `Reticulocytes in peripheral blood.png` | Q10 — explanation |
| `fig_aplastic` | `Aplastic anemia.png` | Q12 — stem |
| `fig_sideroblast` | `Sideroblasts.png` | Q14 — stem |
| `fig_erythropoiesis` | `Erythropoiesis.png` | unused in final build, kept in `figs/` |
| `fig_flow` | `Flow cytometry.png` | **dropped** — see §9 |

### Resizing and embedding

Originals are 0.2–3 MB PNGs. Resize to ~1100 px wide JPEG before base64, or the HTML
balloons. macOS `sips` does this with no dependencies:

```bash
sips -s format jpeg -s formatOptions 72 -Z 1100 "Aplastic anemia.png" --out fig_aplastic.jpg
```

That took the batch from ~8.5 MB of PNG to ~820 KB of JPEG (~1.06 MB once base64'd).
`build_quiz.py` reads `figs/<key>.jpg` and inlines them into `var QUIZ_FIGURES = {...}`
as `data:image/jpeg;base64,…`.

**Always eyeball the resized image before shipping.** Use the Read tool on the `.jpg`.
A marrow biopsy at 72% quality is fine; a fine-detail smear may need quality 85.

---

## 6. The quiz template

Clone this file — do not write a player from scratch:

```
OMK/Heme/week 11/quiz/UWorld Edition/Hematopoiesis and Neoplastic Disorders Quiz.html
```

5.6 MB (most of it is that quiz's own embedded figures, which get replaced). It was
chosen over the summative Question Bank template because **it supports images natively**.

### Question JSON schema

```jsonc
{
  "stem": "…vignette, ending in the lead-in question",
  "choices": ["A. …", "B. …", "C. …", "D. …", "E. …"],   // 4–6, alphabetical, letter-prefixed
  "correct": 2,                                           // 0-based index AFTER alphabetising
  "explanation": "Why the key is right. Arrows (→) for mechanism.",
  "wrongExplanations": { "0": "…", "1": "…", "3": "…", "4": "…" },  // keyed by ACTUAL choice index
  "eli5": "Plain language, max 3 sentences.",
  "image": "fig_aplastic",                    // optional — figure in the stem
  "imageCaption": "…",
  "explanationImage": "fig_retics",           // optional — figure in the explanation
  "explanationImageCaption": "…",
  "los": [                                    // added by build_quiz.py, do not hand-write
    { "n": 29, "t": "objective text", "a": "s2-marrow", "s": "§2" }
  ],
  "labs": {                                   // added by build_quiz.py from the stem, see §4
    "title": "Laboratory studies show:",
    "rows": [ { "t": "Hemoglobin", "r": "8.6 g/dL", "n": "13.5–17.5 g/dL" } ]
  }
}
```

`los` and `labs` are **derived** fields — write the question with a plain stacked lab
block and let the builder produce both. The `stem` that ships contains a `[[LABS]]`
marker where the panel goes.

### Template internals worth knowing

- Questions live in `var PRELOADED_QUESTIONS_JSON = "…"` — a JSON string inside a JS
  string literal (double-encoded).
- Figures live in `var QUIZ_FIGURES = { key: "data:image/jpeg;base64,…" }`.
- Quiz name: `PRELOADED_QUIZ_NAME = "…"` plus the `<title>` tag.
- **Three separate normalizer functions** strip unknown fields off question objects
  (the base one, the shuffle path, and the import path). Any new field — `los`, `labs` —
  must be added to all three or it vanishes at runtime. `build_quiz.py` patches all three.
  This is the single most common way a new field appears to work in testing and then
  disappears once choices shuffle.
- `buildFigureHTML(index)` takes an **index**; `buildExplanationFigureHTML(q)` takes the
  **question object**. Easy to get wrong when testing.
- The app **reshuffles choices at run time**, so the letter you see on screen won't match
  `correct` in the JSON. That is expected.

---

## 7. LO tagging in the answers

Every answer opens with a **"🎯 Learning Objective(s) tested"** block: a coral `LO n`
chip that hyperlinks into the review file at the owning section, the full objective
text, and the `§` number.

`build_quiz.py` injects `loBlockHTML(q)` at the top of `buildExplanationHTML()` and adds
the `.exs.exlo` / `.lo-chip` / `.lo-row` CSS. Tags come from `lo_tags_batch01.py`:

```python
LO_TAGS = {
 1:  [81],        # §1 sites across a lifetime / embryologic progression
 2:  [2, 29],     # §1 primary sites of adult hematopoiesis · §2 sampling
 ...
}
```

**Rule: the first LO in each list must be native to the block being written.** A second,
cross-block LO may follow where the vignette genuinely serves both.

---

## 8. Build and validate

```bash
cd "OMK/Heme/summative/quiz-toolchain"
FIGDIR=figs python3 build_quiz.py \
    questions_batch01_hematopoiesis_marrow.py \
    lo_tags_batch01.py \
    "Jeevs Edition — Hematopoiesis & Marrow" \
    "Jeevs Edition - Hematopoiesis and Marrow Quiz.html"
```

Then run the validation sweep — every one of these caught a real bug at least once:

```bash
python3 - <<'PY'
import re,json
s=open("../Jeevs Edition - Hematopoiesis and Marrow Quiz.html",encoding="utf-8").read()
qs=json.loads(json.loads('"'+re.search(r'var PRELOADED_QUESTIONS_JSON="(.*?)";\n',s,re.S).group(1)+'"'))
figs=json.loads(re.search(r'var QUIZ_FIGURES=(\{.*?\});\n',s,re.S).group(1))
ids=set(re.findall(r'\sid="([^"]+)"',open("../OMK_2A_Heme_Summative_3_Objective_Review.html",encoding="utf-8").read()))
native={2,29,65,81,83}                       # <- change per block
errs=[]
for i,q in enumerate(qs,1):
    ch,c=q["choices"],q["correct"]
    if [x[:2] for x in ch]!=[chr(65+j)+"." for j in range(len(ch))]: errs.append(f"Q{i} letter prefixes")
    if [x[3:] for x in ch]!=sorted([x[3:] for x in ch],key=str.lower): errs.append(f"Q{i} not alphabetical")
    if {str(j) for j in range(len(ch))}-{str(c)} != set(q["wrongExplanations"]): errs.append(f"Q{i} wrongExpl keys")
    if not q.get("los"): errs.append(f"Q{i} no LO")
    elif q["los"][0]["n"] not in native: errs.append(f"Q{i} first LO not native to block")
    for l in q.get("los",[]):
        if l["a"] not in ids: errs.append(f"Q{i} dead anchor {l['a']}")
    for k in ("image","explanationImage"):
        if q.get(k) and q[k] not in figs: errs.append(f"Q{i} missing figure {q[k]}")
    if q.get("labs"):
        if "[[LABS]]" not in q["stem"]: errs.append(f"Q{i} labs present but no [[LABS]] marker")
        for r in q["labs"]["rows"]:
            if not r.get("n"): errs.append(f"Q{i} lab row missing reference range: {r['t']}")
    if re.search(r'Laboratory studies[^\n:]*:\n\S', q["stem"]): errs.append(f"Q{i} raw lab block left in stem")
    hb=re.search(r'Hemoglobin ([\d.]+) g/dL',q["stem"]); hc=re.search(r'Hematocrit ([\d.]+)%',q["stem"])
    if hb and hc:
        r=float(hc.group(1))/float(hb.group(1))
        if not 2.85<=r<=3.15: print(f"  Q{i}: Hct/Hgb = {r:.2f} — deliberate? (MCHC items legitimately differ)")
print("ERRORS:",errs or "none")
PY
```

Note the alphabetical check produces a **false positive on ordered numeric series**
(`16.0%` sorts before `4.0%`). That is correct behaviour for those items — numeric order
wins.

### Browser check

Serve the folder and drive it — the file has a client-side login gate that blanks the
body, so injecting this style is needed to inspect it:

```js
const st=document.createElement('style');
st.textContent='html[data-note-auth="locked"] body>*:not(#noteAuthGate){display:revert!important}#noteAuthGate{display:none!important}';
document.head.appendChild(st);
```

Then verify: no JS errors, `questions.length` is right, every
`buildExplanationHTML(q,{r:'c',i:q.correct})` contains `lo-chip`, and every figure
resolves via `buildFigureHTML(i)` / `buildExplanationFigureHTML(q)`.

---

## 9. Mistakes made on batch 01 — do not repeat

1. **Wrote from the lecture notes instead of the review file.** The content happened to
   line up, but the LO tagging drifted as a result. Start from the review file's
   sections.

2. **Included an out-of-block question.** Q18 was flow cytometry (forward/side scatter,
   CD45). That content is in **§23 Laboratory Foundations**, not §1/§2 — it does not
   belong in a Hematopoiesis & Marrow batch. Replaced with an acute-blood-loss item
   built on §2's own "Acute blood loss is a different clinical animal" callout.
   *Check every question's topic against the block's sections before shipping.*

3. **Tagged cross-block objectives as primary.** Fixed by the native-LO rule in §7.

4. **Got a lab direction backwards.** Originally wrote lipemia causing a *falsely low*
   hemoglobin. Lipemia raises it — turbidity adds absorbance. The internal check
   (Hct ≈ 3 × Hgb) is what exposed it.

5. **MCHC arithmetic didn't compute.** Stated MCHC 37.8 with Hgb 8.8 / Hct 25%, which is
   35.2. Fixed to Hgb 8.7 / Hct 23%. **Recompute every derived index by hand.**

---

## 10. Progress tracker

Batch 01 — **Hematopoiesis & Marrow** (§1, §2) — 20 questions — done.
Topics: fetal→adult hematopoietic sites, red marrow retreat and biopsy site, self-renewal
vs pluripotency, HSC quiescence, CMP/CLP branch point, EPO source, HIF oxygen sensing,
TPO, G-CSF vs GM-CSF, corrected reticulocyte count, CXCR4/CXCL12 niche and plerixafor,
aspirate vs core biopsy, cellularity (100−age), Prussian blue, when *not* to biopsy,
Hgb:Hct ×3 rule, MCHC >36, acute blood loss, dry tap/myelofibrosis, buffy coat.

**Objectives with no questions in the Question Bank** (`_meta.objectives_without_questions`):
**LO 30, 47, 49, 59, 73.**

⚠️ That field tracks the **117-question Question Bank only** — it is *not* updated by the
Jeevs Edition quizzes. Batch 01 does contain items serving LO 49 (next steps in iron
deficiency) and LO 59 (accuracy vs precision), but because those questions live in the
Jeevs quiz rather than the bank, the map still lists them as uncovered.

So there are two separate worklists. Keep them straight:
- **Question Bank gaps** → read `_meta.objectives_without_questions`.
- **Jeevs Edition coverage** → read the `LO_TAGS` dicts in `quiz-toolchain/lo_tags_batch*.py`.

If you want one combined view:

```bash
cd quiz-toolchain
python3 - <<'PY'
import json,glob,importlib.util,re
bank=json.load(open("../heme_summative3_lo_question_map.json"))
covered={int(k) for k,v in bank["objectives"].items() if v["questions"]}
for f in sorted(glob.glob("lo_tags_batch*.py")):
    sp=importlib.util.spec_from_file_location("t",f); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    covered |= {lo for v in m.LO_TAGS.values() for lo in v}
print("uncovered across bank + all Jeevs batches:", sorted(set(range(1,84))-covered))
PY
```

**Suggested next blocks**, with their review-file sections:

| Block | Sections | Native LOs |
|---|---|---|
| Anemia — evaluation & classification | §3 | 19, 42, 53, 55 |
| Iron / B12 / folate / AOCD | §4, §5, §6 | 20, 49 |
| Hemolysis & the globin disorders | §8, §9, §10 | 25, 28 |
| Laboratory foundations (CBC, smear, interference) | §23, §24, §25 | 27, 59 |
| Coagulation & bleeding | §29, §30, §31 | 32, 36, 50 |
| Splenic trauma & post-traumatic edema | §55, §56 | 47, 73, 34 |

---

## 11. File inventory

```
OMK/Heme/summative/
├── OMK_2A_Heme_Summative_3_Objective_Review.html   ← SOURCE OF TRUTH (59 sections, 83 LOs)
├── OMK_2A_Heme_Summative_3_Question_Bank.html      ← separate 117-question bank, also LO-tagged
├── heme_summative3_lo_question_map.json            ← LO ↔ section ↔ question map
├── index.html                                      ← item-writing spec + lab reference table
├── Jeevs Edition - Hematopoiesis and Marrow Quiz.html   ← batch 01 output
├── QUIZ_BUILD_METHOD.md                            ← this file
└── quiz-toolchain/
    ├── build_quiz.py                               ← clones template, injects Q + figures + LO blocks
    ├── questions_batch01_hematopoiesis_marrow.py   ← the 20 questions as Python data
    ├── lo_tags_batch01.py                          ← question № → LO numbers
    └── figs/                                       ← resized JPEGs, keyed fig_*
```

To start batch 02: copy `questions_batch01_*.py` and `lo_tags_batch01.py` to `_batch02_`
names, replace the contents, add any new figures to `figs/`, and run `build_quiz.py`
with the new filenames.
