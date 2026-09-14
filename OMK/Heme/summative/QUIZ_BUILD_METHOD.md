# How the "Jeevs Edition" quizzes are built

Handoff document. Written so a fresh Claude session (or a human) can produce the next
batch without re-deriving anything. Everything here was used to build batch 01 (Hematopoiesis & Marrow, 20 questions) and
batch 02 (Anemia I · Impaired Production, 30 questions).

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
  "_meta": { "total_objectives": 83, "objectives_without_questions": [30, 47, 49, 59, 73] },
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

Lab values render as a bordered `TEST | RESULT | REFERENCE RANGE` table with zebra
striping and a footnote. **This table is drawn by the quiz template itself** (its
`formatStemText()` function), not by anything the builder injects:

```
┌──────────────────────────────────────────────────────────────────────────┐
│ TEST                          RESULT            REFERENCE RANGE          │
├──────────────────────────────────────────────────────────────────────────┤
│ Hemoglobin                    8.6 g/dL          13.5–17.5 g/dL           │
│ Hematocrit                    26%               41%–53%                  │
│ Mean corpuscular volume       92 µm3            80–100 µm3               │
├──────────────────────────────────────────────────────────────────────────┤
│ Typical educational ranges are shown. Actual reference intervals vary by  │
│ laboratory, age, sex, and clinical context.                              │
└──────────────────────────────────────────────────────────────────────────┘
```

**Write lab blocks in plain stacked form** in the question file, with real `\n`:

```
Laboratory studies show:
Hemoglobin 8.6 g/dL (N=13.5–17.5 g/dL)
Hematocrit 26% (N=41%–53%)
Reticulocyte count 0.3% (N=0.5%–1.5%)
```

`build_quiz.py` finds every block starting `Laboratory studies…:` (up to the next blank
line) and rewrites each line into the template's native row syntax — **two-space indent,
test name, two or more spaces, value**:

```
Laboratory studies show:
  Hemoglobin  8.6 g/dL (N=13.5–17.5 g/dL)
  Hematocrit  26% (N=41%–53%)
  Reticulocyte count  0.3% (N=0.5%–1.5%)
```

The name/value split is **the first token beginning with a digit, `<` or `>`**, so
`Serum vitamin B12 480 pg/mL`, `Hemoglobin A1c 7.1%` and `Haptoglobin <10 mg/dL` all
parse correctly. The build **raises** on a line it cannot parse, on a line with no
`(N=…)`, and on a block with fewer than 2 rows (the template ignores 1-row panels).

**Why the explicit `(N=…)` matters.** The template's `getLabResultAndReference()` uses an
explicit `(N=…)` if present; otherwise it falls back to its own built-in
`TYPICAL_LAB_RANGES` table, whose numbers differ from `index.html` (e.g. hemoglobin
"M: 14–17" vs "13.5–17.5"). Always write `(N=…)` so every range matches the app's Lab
Values panel.

Lines written this way also work if the stem is pasted into any other quiz built on the
same template.

### Line breaks

The template now renders stem newlines natively (`white-space:pre-wrap`, `<br>` joins),
so no stem CSS patch is needed. The builder **does** add `white-space:pre-line` to
explanation text (`.exb .exs .ext`) — without it, multi-paragraph explanations and `•`
bullet lists collapse into one block.

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

### Figures used in batch 02

| Key | Source | Used in |
|---|---|---|
| `fig_ida_progression` | UWorld `78_progression_of_iron_deficiency_labs.png` | Q1 — explanation |
| `fig_ida_smear` | AMBOSS `Iron deficiency anemia.png` | Q2 — stem |
| `fig_hepcidin` | UWorld `93_hepcidin_and_iron_regulation.jpg` | Q6 — explanation |
| `fig_hyperseg_uw` | UWorld `72_megaloblastic_anemia_hypersegmented_neutrophil.png` | Q7 — stem |
| `fig_megaloblastic_marrow` | AMBOSS `Megaloblastic anemia.png` | Q10 — stem |
| `fig_b12_absorption` | AMBOSS `Vitamin B12 absorption.png` | Q13 — explanation |
| `fig_hyperseg` | AMBOSS `Hypersegmented neutrophils.png` | Q14 — stem |
| `fig_ida_smear_uw` | UWorld `42_iron_deficiency_microcytic_hypochromic_smear.jpg` | Q16 — explanation (labelled, so **not** usable in a stem) |
| `fig_celiac_duodenum` | UWorld GI `059_normal_duodenum_celiac_disease.jpg` | Q19 — explanation |
| `fig_mtx_pathway` | UWorld `86_methotrexate_and_5_fluorouracil_folate_pathway.png` | Q24 — explanation |
| `fig_spherocytes` | AMBOSS `Spherocytosis.png` | Q25 — stem |
| `fig_parvo_pronormoblast` | UWorld `64_parvovirus_b19_giant_pronormoblast.jpg` | Q25 — explanation (the near-miss) |
| `fig_intestinal_absorption` | AMBOSS `Intestinal resorption.png` | Q26 — explanation |
| `fig_b12_def_uw` | UWorld GI `043_vitamin_b12_deficiency.jpg` | Q30 — explanation |

Q1 and Q18 share `fig_ida_progression`; Q13 and Q20 share `fig_b12_absorption` — reusing a
diagram across questions is fine. Also look beyond the Hematology folder: the UWorld
**Gastrointestinal & Nutrition** folder has the B12, folate and celiac diagrams.

Rejected: AMBOSS `Gastritis.png` — it shows *H. pylori* gastritis, not the autoimmune
gastritis of pernicious anemia. Read the caption's actual diagnosis, not just the title.

**UWorld files have no `.txt` sidecar.** The filename describes the content; view the
image before writing a caption. UWorld diagrams carry a "©USMLEWorld" mark and labelled
structures, so use them as **explanation** images only, never in a stem.

**Stem image captions must describe findings, not name the diagnosis** — "a neutrophil
with a six-lobed nucleus," not "a hypersegmented neutrophil of B12 deficiency."

To find candidates quickly:

```bash
cd "/Users/jeeval/Documents/Board Study/figures"
ls amboss | grep -iE '\.png$' | grep -iE 'iron|b12|folate|megalob|neutrophil'
ls "Uworld images/COMLEX 1 (Step1 + OMT1) - Hematology & Oncology" | grep -iE 'iron|b12|megalob|hepcidin'
```

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

~5.9 MB (most of it is that quiz's own embedded figures, which get replaced). It was
chosen over the summative Question Bank template because **it supports images natively**,
and it now also renders lab panels natively (§4).

> ⚠️ **The template is live, not pinned.** It was upgraded on 14 Sep 2026 (native lab
> panels, `formatStemText`, pre-wrap stems), which broke the original builder's patches
> mid-way through batch 02. `build_quiz.py` now asserts the features it relies on and
> fails with a `template drift` message naming the patch target if the template changes
> again. If that happens, inspect the new template rather than forcing the old patch.

### Question JSON schema

```jsonc
{
  "stem": "…vignette, with a plain stacked lab block, ending in the lead-in",
  "choices": ["A. …", "B. …", "C. …", "D. …", "E. …"],   // 4–6, alphabetical, letter-prefixed
  "correct": 2,                                           // 0-based index AFTER alphabetising
  "explanation": "Why the key is right. Arrows (→) for mechanism. \n\n and • bullets OK.",
  "wrongExplanations": { "0": "…", "1": "…", "3": "…", "4": "…" },  // keyed by ACTUAL choice index
  "eli5": "Plain language, max 3 sentences.",
  "image": "fig_aplastic",                    // optional — figure in the stem
  "imageCaption": "…",
  "explanationImage": "fig_retics",           // optional — figure in the explanation
  "explanationImageCaption": "…",
  "los": [                                    // added by build_quiz.py — do not hand-write
    { "n": 29, "t": "objective text", "a": "s2-marrow", "s": "§2" }
  ]
}
```

**Never reference an option letter in any explanation text.** The app reshuffles choices
at run time and relabels `wrongExplanations` automatically, but a letter written inside
prose ("unlike C…") will point at the wrong option.

### Template internals worth knowing

- Questions live in `var PRELOADED_QUESTIONS_JSON = "…"` — a JSON string inside a JS
  string literal (double-encoded).
- Figures live in `var QUIZ_FIGURES = { key: "data:image/jpeg;base64,…" }`.
- Quiz name: `PRELOADED_QUIZ_NAME = "…"` plus the `<title>` tag.
- **Three separate normalizer functions** strip unknown fields off question objects
  (the base one, the shuffle path, and the import path). Any new field — e.g. `los` —
  must be added to all three or it vanishes at runtime. `build_quiz.py` patches all three.
  This is the single most common way a new field appears to work in testing and then
  disappears once choices shuffle.
- `buildFigureHTML(index)` takes an **index**; `buildExplanationFigureHTML(q)` takes the
  **question object**. Easy to get wrong when testing.
- Stems are HTML-escaped by `formatStemText`, so a stem cannot contain markup — which is
  also why `<10 mg/dL` is safe to write.

---

## 7. LO tagging in the answers

Every answer opens with a **"🎯 Learning Objective(s) tested"** block: a coral `LO n`
chip that hyperlinks into the review file at the owning section, the full objective
text, and the `§` number.

`build_quiz.py` injects `loBlockHTML(q)` at the top of `buildExplanationHTML()` and adds
the `.exs.exlo` / `.lo-chip` / `.lo-row` CSS. Tags come from `lo_tags_batchNN.py`, keyed by
question number. Each entry is either an LO number or an `(LO, "section-anchor")` pair:

```python
S4, S5, S6 = "s4-iron", "s5-b12-folate", "s6-aocd"
LO_TAGS = {
 1:  [(49, S4), (20, S4)],   # adult male IDA → GI source
 7:  [(20, S5), (53, S5)],   # MMA separates B12 from folate
 12: [18],                   # bare number → objective's first listed section
}
```

**Use the pair form whenever an objective spans several sections.** LO 20 (nutritional
anemias) is listed under both §4 and §5; a bare `20` would always link to §4, sending a
B12 question's chip to the iron section. The builder asserts every anchor exists in the
review file, and reads the `§` number from that section's own label.

**Rule: the first LO in each list must be native to the block being written.** A second,
cross-block LO may follow where the vignette genuinely serves both.

---

## 8. Build and validate

```bash
cd "OMK/Heme/summative/quiz-toolchain"
python3 build_quiz.py \
    questions_batch02_anemia1_impaired_production.py \
    lo_tags_batch02.py \
    "Jeevs Edition — Anemia I · Impaired Production" \
    "Jeevs Edition - Anemia I Impaired Production Quiz.html"
```

Figures default to `quiz-toolchain/figs/`; override with `FIGDIR=…`. Paths to the
template, review file and LO map are resolved relative to the script, so it runs from
any working directory. **Rebuild earlier batches whenever `build_quiz.py` changes**, so
every quiz carries the same features.

Then run the validation sweep — every check here caught a real bug at least once:

```bash
python3 - <<'PY'
import re,json
QUIZ="../Jeevs Edition - Anemia I Impaired Production Quiz.html"   # <- change per batch
native={18,19,20,49}                                               # <- change per block
s=open(QUIZ,encoding="utf-8").read()
qs=json.loads(json.loads('"'+re.search(r'var PRELOADED_QUESTIONS_JSON="(.*?)";\n',s,re.S).group(1)+'"'))
figs=json.loads(re.search(r'var QUIZ_FIGURES=(\{.*?\});\n',s,re.S).group(1))
ids=set(re.findall(r'\sid="([^"]+)"',open("../OMK_2A_Heme_Summative_3_Objective_Review.html",encoding="utf-8").read()))
errs=[];keys=[]
for i,q in enumerate(qs,1):
    ch,c=q["choices"],q["correct"]; keys.append(chr(65+c))
    if [x[:2] for x in ch]!=[chr(65+j)+"." for j in range(len(ch))]: errs.append(f"Q{i} letter prefixes")
    if [x[3:] for x in ch]!=sorted([x[3:] for x in ch],key=str.lower): errs.append(f"Q{i} not alphabetical")
    if {str(j) for j in range(len(ch))}-{str(c)}!=set(q["wrongExplanations"]): errs.append(f"Q{i} wrongExpl keys")
    if not q.get("los") or q["los"][0]["n"] not in native: errs.append(f"Q{i} first LO not native")
    if len({l["n"] for l in q.get("los",[])})!=len(q.get("los",[])): errs.append(f"Q{i} duplicate LO")
    for l in q.get("los",[]):
        if l["a"] not in ids: errs.append(f"Q{i} dead anchor {l['a']}")
    for k in ("image","explanationImage"):
        if q.get(k) and q[k] not in figs: errs.append(f"Q{i} missing figure {q[k]}")
    rows=re.findall(r'\n  (\S.*?)  (\S.*)',q["stem"])
    if "Laboratory studies" in q["stem"] and len(rows)<2: errs.append(f"Q{i} lab block not converted")
    for nm,val in rows:
        if "(N=" not in val: errs.append(f"Q{i} lab row without range: {nm}")
    hb=re.search(r'\n  Hemoglobin  ([\d.]+)',q["stem"]); hc=re.search(r'\n  Hematocrit  ([\d.]+)',q["stem"])
    if hb and hc and not 2.85<=float(hc.group(1))/float(hb.group(1))<=3.15:
        print(f"  Q{i}: Hct/Hgb {float(hc.group(1))/float(hb.group(1)):.2f} — deliberate? (MCHC items differ)")
print("keys:","".join(keys),{k:keys.count(k) for k in sorted(set(keys))})
print("ERRORS:",errs or "none")
PY
```

Two expected false positives: the alphabetical check flags **ordered numeric series**
(`16.0%` sorts before `4.0%` as text — numeric order is correct), and the Hct/Hgb warning
fires on **MCHC items**, where the ratio being off is the testing point.

Key-letter rule: fix only if one letter is correct for more than half the batch, or 4+
consecutive items share a key. The app reshuffles at run time anyway.

### Browser check

Serve the folder and drive it — the file has a client-side login gate that blanks the
body, so injecting this style is needed to inspect it:

```js
const st=document.createElement('style');
st.textContent='html[data-note-auth="locked"] body>*:not(#noteAuthGate){display:revert!important}#noteAuthGate{display:none!important}';
document.head.appendChild(st);
```

Then verify: no JS errors, `questions.length` is right, every
`buildExplanationHTML(q,{r:'c',i:q.correct})` contains `lo-chip`, every figure resolves
via `buildFigureHTML(i)` / `buildExplanationFigureHTML(q)`, and every question with labs
renders rows — `getStemHTML(i)` should contain `class="lab-row"`.

The same override also un-hides the app's "Laboratory Values" modal, which will cover the
page in screenshots. Hide it with:

```js
[...document.body.children].find(e=>/Laboratory Values/.test(e.innerText||''))?.style.setProperty('display','none','important');
```

If `python3 -m http.server` starts answering `400` with 0 bytes, the server has gone
stale — the file is fine. Kill it and start a fresh one on a new port.

---

## 9. Mistakes made — do not repeat

### Batch 01

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

### Batch 02

6. **The template changed underneath the builder.** The shared quiz template gained a
   native lab-panel renderer the same day; three of the builder's string patches no longer
   matched and the build aborted. Rather than force the old `[[LABS]]` injection over the
   new renderer, the builder was rewritten to emit the template's own row syntax (§4). It
   now asserts the template features it needs and names the exact patch that drifted.

7. **Multi-section objectives linked to the wrong section.** A bare `20` sent B12
   questions' LO chips to the iron section. Fixed with `(LO, anchor)` tag pairs (§7).

8. **Explanations lost their paragraph breaks** in both batches until
   `white-space:pre-line` was added to explanation text. Visible only in the browser —
   the JSON looked fine.

9. **Check stem images for overlays before using them.** AMBOSS captions describe
   coloured overlays and arrows; the saved PNGs in this library turned out to be the clean
   versions, but that has to be confirmed by viewing each file, not assumed. UWorld's
   `42_iron_deficiency…smear.jpg` is the counter-example: it has the diagnosis printed as
   a title plus arrows, so it was moved from a stem to an explanation.

10. **A question listed the same LO twice** (LO 20 tagged once for §4 and once for §5).
    An LO appears once per question — pick the section the question actually tests. The
    validation sweep now checks for duplicates.

---

## 10. Progress tracker

| Batch | Block | Review sections | Native LOs | Qs | File |
|---|---|---|---|---|---|
| 01 | Hematopoiesis & Marrow | §1, §2 | 2, 29, 65, 81, 83 | 20 | `Jeevs Edition - Hematopoiesis and Marrow Quiz.html` |
| 02 | Anemia I · Impaired Production | §4, §5, §6 | 18, 19, 20, 49 | 30 | `Jeevs Edition - Anemia I Impaired Production Quiz.html` |

**Batch 01 topics:** fetal→adult hematopoietic sites, red marrow retreat and biopsy site,
self-renewal vs pluripotency, HSC quiescence, CMP/CLP branch point, EPO source, HIF oxygen
sensing, TPO, G-CSF vs GM-CSF, corrected reticulocyte count, CXCR4/CXCL12 niche and
plerixafor, aspirate vs core biopsy, cellularity (100−age), Prussian blue, when *not* to
biopsy, Hgb:Hct ×3 rule, MCHC >36, acute blood loss, dry tap/myelofibrosis, buffy coat.

**Batch 02 topics (Q1–Q15):** adult-male iron deficiency → bidirectional endoscopy
(negative FOBT decoy), why iron-deficient cells are small, duodenal absorption and gastric
bypass, ferritin as an acute phase reactant, AOCD iron-study row (matched-set item),
hepcidin/ferroportin direction trap, methylmalonic acid vs homocysteine, folate masking
B12 → subacute combined degeneration, pernicious anemia → gastric carcinoma surveillance,
ineffective erythropoiesis, metformin, preconception folic acid, terminal ileum/cubilin,
the hypersegmented neutrophil, AOCD management.

**Batch 02 topics (Q16–Q30):** pica + menorrhagia → continue iron after hemoglobin
normalizes, black stools on oral iron and the reticulocyte response, depleted stores as
the first stage (frequent blood donor, iron compartments), refractory iron deficiency →
celiac serology, proton pump inhibitors → B12 not released from food protein, fish
tapeworm, the Schilling test, anti-intrinsic factor (specific) vs anti-parietal cell
(sensitive), methotrexate → leucovorin, chronic hemolysis → folate deficiency vs parvovirus
aplastic crisis, bariatric dual deficiency with a normal MCV, high-dose oral B12 by passive
diffusion, AOCD erythropoietin inappropriately low, transferrin as a negative acute phase
reactant, breastfed infant of a vegan mother.

§4–§6 is now covered end to end. The only review-file content not given its own item is
the AOCD hemophagocytosis mechanism and the epidemiology line ("most common anemia in
hospitalized patients") — both are named in explanations instead.

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
    covered |= {(t[0] if isinstance(t,(tuple,list)) else t) for v in m.LO_TAGS.values() for t in v}
print("uncovered across bank + all Jeevs batches:", sorted(set(range(1,84))-covered))
PY
```

**Suggested next blocks**, with their review-file sections:

| Block | Sections | Native LOs |
|---|---|---|
| Anemia — evaluation & classification | §3 | 19, 42, 53, 55 |
| Porphyrias & lead | §7 | 35 |
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
├── Jeevs Edition - Hematopoiesis and Marrow Quiz.html        ← batch 01
├── Jeevs Edition - Anemia I Impaired Production Quiz.html    ← batch 02
├── QUIZ_BUILD_METHOD.md                            ← this file
└── quiz-toolchain/
    ├── build_quiz.py                               ← clones template, injects Q + figures + LO blocks
    ├── questions_batch01_hematopoiesis_marrow.py
    ├── lo_tags_batch01.py
    ├── questions_batch02_anemia1_impaired_production.py
    ├── lo_tags_batch02.py
    └── figs/                                       ← resized JPEGs, keyed fig_*
```

To start the next batch: copy the latest `questions_batchNN_*.py` and `lo_tags_batchNN.py`
to the next number, replace the contents, add any new figures to `figs/`, and run
`build_quiz.py` with the new filenames (§8).
