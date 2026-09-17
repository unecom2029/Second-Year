# How the "Jeevs Edition" quizzes are built

Handoff document. Written so a fresh Claude session (or a human) can produce the next
batch without re-deriving anything. Everything here was used to build batch 01 (Hematopoiesis & Marrow, 20 questions),
batch 02 (Anemia I · Impaired Production, 30 questions) and batch 03 (Anemia II ·
Hemolysis, 20 questions — the first batch APPENDED to the live quiz rather than built as
its own file; see §8).

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

### A third library, added for batch 03

```
/Users/jeeval/Documents/Board Study/figures/pathoma-heme/
```

86 page-extracted images plus a `manifest.tsv` giving page, object number and pixel size —
**no captions**, so each file has to be viewed before it can be described. Unused so far;
AMBOSS and UWorld covered batch 03.

### Figures added for batch 07 — the course's OWN lecture slides

A fourth image source, and the best one yet: the review file's own slide images already live in

```
OMK/Heme/summative/assets/
```

named by topic and content (`anticoag-09-slide-on-warfarin-onset-listing-that-warfarin-is.jpg`,
`coag1-10-mixing-study-interpretation-flowchart-distinguis.jpg`, …). These are the lecturer's
actual slides, so an explanation figure can show Jeevs the exact slide the fact came from.
Batch 07 used twelve of them, keyed `fig_slide_*`:

| Key | Slide | Used in |
|---|---|---|
| `fig_slide_anticoag_classes` | anticoag-01, the four families | Q8, Q11, Q12, Q13, Q14, Q22 |
| `fig_slide_hit` | anticoag-05, HIT four-step diagram | Q2 |
| `fig_slide_hit_mgmt` | anticoag-06, HIT management | Q3 |
| `fig_slide_vitk` | anticoag-08, the vitamin K cycle | Q5, Q7 |
| `fig_slide_warf_onset` | anticoag-09, clotting factor half-lives | Q4 |
| `fig_slide_cyp2c9` | anticoag-11, CYP2C9/VKORC1 | Q6 |
| `fig_slide_xaban_reversal` | anticoag-14, DOAC reversal | Q9, Q10 |
| `fig_slide_fibrinolysis` | anticoag-15, the fibrinolysis diagram | Q23, Q24, Q25 |
| `fig_slide_platelet` | anticoag-16, platelet activation targets | Q16, Q20 |
| `fig_slide_kp_antiplatelet` | anticoag-19, antiplatelet summary | Q17, Q18, Q19, Q21 |

Plus `fig_warfarin_necrosis` (AMBOSS, clean clinical photograph — used as a **stem** image) and
`fig_heparin_mech_uw` (UWorld heparin/LMWH mechanism, Q1 and Q15).

**Use the half-life numbers from the slide, not from memory.** The lecture gives factor II 60 h,
VII 4–6 h, IX 24 h, X 48–72 h, protein C 8 h, protein S 30 h — batch 07 quotes those, so the
explanation matches what the lecturer said.

### Figures added for batch 05

| Key | Source | Used in |
|---|---|---|
| `fig_tx_reactions` | AMBOSS `Transfusion reactions.png` | Q1, Q3, Q4, Q6, Q11, Q14, Q15, Q17, Q18 — explanation |
| `fig_tx_timeline` | AMBOSS `Transfusion reaction timeline.png` | Q2, Q5, Q7, Q12, Q16, Q19, Q20 — explanation |
| `fig_abo` | AMBOSS `ABO blood group system.png` | Q8, Q13 — explanation |
| `fig_o_neg_compat` | AMBOSS `Blood type O- RBC transfusion compatibility.png` | Q9 — explanation |
| `fig_rh_pregnancy` | AMBOSS `Rhesus (Rh) incompatibility in pregnancy.png` | Q10 — explanation |
| `fig_trali_cxr`, `fig_hdfn_uw` | AMBOSS / UWorld | resized, unused — the TRALI film carries red and green overlays |

Transfusion is the first block with **no stem images** — nothing in it is a morphology
question. The two AMBOSS summary figures (the reaction grid and the timeline) carry most of
the explanations, and they are worth reusing heavily because the whole section is one
differential.

### Figures added for batch 04

| Key | Source | Used in |
|---|---|---|
| `fig_pigment_stones` | UWorld GI `035_pathogenesis_of_pigment_stones.jpg` | Q1 — explanation |
| `fig_bilirubin` | AMBOSS `Bilirubin metabolism.png` | Q2, Q3 — explanation |
| `fig_hair_on_end` | AMBOSS `Hair-on-end appearance of the skull.png` | Q8 — **stem** (clean lateral skull radiograph, no annotation) |
| `fig_thal_minor_uw` | UWorld `75_beta_thalassemia_minor_target_cells.png` | Q9 — explanation |
| `fig_sickle_mutation` | UWorld `28_sickle_cell_missense_mutation.jpg` | Q12 — explanation |
| `fig_sickle_inheritance` | UWorld `25_autosomal_recessive_sickle_cell_inheritance.jpg` | resized, unused in the final build |

Everything else in batch 04 reuses batch 03 keys. The skull film is the first non-smear
stem image in the series; it works because the finding can be described in words
("the space between the inner and outer tables is widened, with fine perpendicular
striations") without naming the diagnosis.

### Figures used in batch 03

| Key | Source | Used in |
|---|---|---|
| `fig_schistocytes` | AMBOSS `Schistocytes.png` | Q1 — stem |
| `fig_howell_jolly` | AMBOSS `Howell-Jolly bodies in asplenia.png` | Q1, Q18 — explanation (**has red arrows — explanation only**) |
| `fig_aiha` | UWorld `35_cold_and_warm_autoimmune_hemolytic_anemia.jpg` | Q2, Q7 — explanation |
| `fig_spherocytes` | AMBOSS `Spherocytosis.png` (already in `figs/`) | Q4 — stem; Q5 — explanation |
| `fig_spherocytes_uw` | UWorld `73_hemolytic_anemia_spherocytes_and_reticulocytes.jpg` | Q4 — explanation |
| `fig_bite_cells` | AMBOSS `Bite cells in … (G6PD) deficiency.png` | Q8 — stem (clean, but pale/low contrast) |
| `fig_bite_uw` | UWorld `01_g6pd_deficiency_bite_cells.jpg` | Q8, Q11 — explanation |
| `fig_g6pd_pathway` | UWorld `02_g6pd_nadph_glutathione_pathway.jpg` | Q9 — explanation |
| `fig_heinz` | AMBOSS `Heinz bodies.png` | Q10 — explanation (granular retics in field; too ambiguous for a stem) |
| `fig_globin_chains` | UWorld `82_hemoglobin_chain_composition_and_variants.jpg` | Q12, Q13 — explanation |
| `fig_beta_thal_uw` | UWorld `24_beta_thalassemia_microcytic_target_cells.png` | Q14 — explanation |
| `fig_target_cells` | AMBOSS `Target cells (codocytes).png` | Q15 — stem |
| `fig_electrophoresis` | UWorld `12_hemoglobinopathy_electrophoresis_patterns.jpg` | Q17 — explanation |
| `fig_sickle_smear` | AMBOSS `Erythrocyte morphologies in sickle-cell disease.png` | Q19 — stem |
| `fig_sickle_target` | AMBOSS `Sickle cell disease with drepanocytes and target cells.png` | Q19, Q20 — explanation |

Reused from earlier batches: `fig_retics` (Q3), `fig_parvo_pronormoblast` (Q6),
`fig_ida_progression` (Q15), `fig_hepcidin` (Q16).

Checked and rejected for stems: `fig_howell_jolly` (red arrows burned in) and `fig_heinz`
(the supravitally stained field also contains granular reticulocytes, so "small round
inclusions" cannot be described unambiguously). Both were moved to explanations. AMBOSS
captions describing coloured overlays again turned out to describe annotated versions that
are **not** what is saved in this library — the saved `Spherocytosis.png`, `Schistocytes.png`,
`Target cells (codocytes).png` and both sickle files are clean. Confirm by viewing, never
by reading the caption.

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

### From batch 03 on: APPEND, do not build a new file

Jeevs asked for one quiz, not a file per topic. New batches are appended to

```
OMK/Heme/summative/Jeevs edition _ summative review.html
```

with `append_quiz.py`, which edits that file in place:

```bash
cd "OMK/Heme/summative/quiz-toolchain"
python3 append_quiz.py \
    questions_batch03_anemia2_hemolysis.py \
    lo_tags_batch03.py
```

It applies the same LO tagging and lab-block conversion as `build_quiz.py`, merges the
new questions onto the end of `PRELOADED_QUESTIONS_JSON` and the new figures into
`QUIZ_FIGURES`, and leaves every existing patch (LO blocks, the three normalizers, the
CSS) untouched — so the target must already be a built Jeevs Edition file; the script
asserts all four features and refuses otherwise. It writes a timestamped `.bak` first and
aborts if a question looks already appended (duplicate opening 120 characters), so
re-running it is safe. A third argument overrides the target filename.

`build_quiz.py` is still the tool for creating a *new* quiz from the template:

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
| 03 | Anemia II · Hemolysis | §8, §9, §10 | 7, 25, 28 | 20 | appended to `Jeevs edition _ summative review.html` |
| 04 | Anemia II · Hemolysis, part 2 | §8, §9, §10 | 7, 25, 28 | 15 | appended to `Jeevs edition _ summative review.html` |
| 05 | Transfusion Medicine | §12, §13, §14 | 31, 61, 74 | 20 | appended to `Jeevs edition _ summative review.html` |
| 06 | Transfusion Medicine, part 2 | §12, §13, §14 | 31, 61, 74 | 10 | appended to `Jeevs edition _ summative review.html` |
| 07 | Hemostasis Pharmacology | §15, §16 | 8, 12, 26, 48, 62, 69, 71 | 25 | appended to `Jeevs edition _ summative review.html` |
| 08 | Hemostasis Pharmacology, part 2 | §15, §16 | 8, 48, 62, 69, 71 | 8 | appended to `Jeevs edition _ summative review.html` |
| 09 | Anemia Pharmacology | §17 | 9, 70, 72 | 15 | appended to `Jeevs edition _ summative review.html` |
| 10 | Anemia Pharmacology, part 2 | §17 | 7, 9, 20, 70, 72 | 5 | appended to `Jeevs edition _ summative review.html` |
| 11 | Infection | §18, §19, §20, §21, §22 | 1, 5, 13, 14, 22, 23, 24, 75, 77 | 20 | appended to `Jeevs edition _ summative review.html` |
| 12 | Infection, part 2 | §18, §19, §20, §21, §22 | 1, 5, 13, 14, 22, 23, 24, 77 | 18 | appended to `Jeevs edition _ summative review.html` |
| 13 | Laboratory Foundations | §23, §24, §25 | 5, 19, 20, 27, 28, 33, 59 | 20 | appended to `Jeevs edition _ summative review.html` |
| 14 | Benign White Cell Disorders | §26, §27, §28 | 1, 4, 31, 66, 76 | 20 | appended to `Jeevs edition _ summative review.html` |
| 15 | Coagulation I · Bleeding | §29, §30, §31 | 32, 36, 50, 68, 79 | 25 | appended to `Jeevs edition _ summative review.html` |
| 16 | Coagulation I · Bleeding, part 2 | §29, §30, §31 | 32, 36, 50, 79 | 10 | appended to `Jeevs edition _ summative review.html` |
| 17 | Coagulation II · Clotting | §32, §33, §34 | 33, 43, 44, 45, 46, 48, 52 | 20 | appended to `Jeevs edition _ summative review.html` |
| 18 | Coag II top-up + Lymph Node Pathology | §32–§35 | 33, 43, 44, 45, 46, 52, 63, 66 | 16 | appended to `Jeevs edition _ summative review.html` |
| 19 | Hematologic Malignancy, part 1 (myeloid) | §36, §37, §38, §39 | 6, 37, 38, 39, 52, 54, 58, 66, 80, 82 | 20 | appended to `Jeevs edition _ summative review.html` |

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

**Batch 03 topics:** prosthetic-valve intravascular hemolysis and the dipstick-positive,
erythrocyte-negative urine; which markers actually localize destruction (urine hemosiderin);
the corrected reticulocyte count as arithmetic; hereditary spherocytosis with a negative
Coombs and a high MCHC; osmotic fragility as a surface-area-to-volume test; parvovirus B19
aplastic crisis (low reticulocytes); spherocytes with a POSITIVE antiglobulin test → warm
autoimmune hemolysis; G6PD after a sulfonamide (bite cells); the NADPH/glutathione step;
the falsely normal enzyme assay during a crisis; why a class III variant self-limits;
counting alpha genes (hemoglobin H); hemoglobin Barts oxygen affinity; the globin switch and
onset at 6 months; thalassemia trait vs iron deficiency as an iron-studies grid;
transfusional iron overload → chelation, never phlebotomy; electrophoresis trait vs disease;
fever in a child with sickle cell disease; sequestration vs aplastic vs vaso-occlusive
crisis by reticulocyte count; hydroxyurea and hemoglobin F.

**Batch 04 topics:** pigment gallstones from the chronic bilirubin load; filtered free heme →
acute tubular necrosis; acholuric jaundice (unconjugated bilirubin is albumin-bound, so not
filtered); vaccinating before splenectomy; pyruvate kinase deficiency (ATP, and the 2,3-BPG
shift that explains exercise tolerance); infection as the commonest G6PD trigger; autosomal
dominant recurrence risk and the independence of each pregnancy; marrow expansion and the
skull radiograph; raised hemoglobin A2 in beta-thalassemia trait; cis vs trans alpha
deletions and the hydrops risk; acute chest syndrome; why fluids and oxygen work; transcranial
Doppler → chronic transfusion for stroke prevention; autosplenectomy and Howell-Jolly bodies;
nitric oxide scavenging → pulmonary hypertension and leg ulcers.

**Batch 05 topics:** the restrictive threshold and TRICC (written in chart/tabular format);
the platelet threshold before a lumbar puncture; why platelet transfusion fails in immune
thrombocytopenia; cryoprecipitate for fibrinogen in obstetric DIC; four-factor prothrombin
complex concentrate plus vitamin K for warfarin reversal; factor VIII concentrate rather
than plasma; citrate chelation and hypocalcemia in massive transfusion; why ABO antibodies
exist without exposure; emergency release and RhD rationing; anti-D alloimmunization → HDFN;
the positive antibody screen → antigen-negative units; delayed hemolytic reaction (anti-Jka);
the plasma compatibility inversion; acute hemolytic reaction and wrong-blood-in-tube; TRALI;
TACO as a matched-set contrast; febrile nonhemolytic → leukoreduction; anaphylaxis and IgA
deficiency; the septic platelet unit; TA-GVHD → irradiation.

**Batch 06 topics (the 10 gaps batch 05 left):** the 30% factor-activity threshold and the
"treating the number" plasma error; product storage conditions as a matched set (the platelet
exception); albumin for volume without a hemostatic requirement; type and screen versus type
and cross; the front-type/back-type ABO discrepancy → recollect the sample; hemolytic disease
of the fetus and newborn (IgG crosses, IgM does not); alloimmunization in sickle cell disease
→ extended antigen matching; the reaction algorithm's first step (stop, then clerical check);
the mild allergic reaction, the one that may be resumed; and the transfusion-refusal
conversation.

**Batch 07 topics:** chain length and target (why fondaparinux leaves the aPTT normal); HIT
recognition and management; why warfarin alone is hazardous in HIT; factor half-lives and the
bridge; warfarin-induced skin necrosis; CYP2C9 inhibition raising the INR; the vitamin K diet
conversation; warfarin teratogenicity; idarucizumab for dabigatran; 4F-PCC for a -xaban (andexanet
withdrawn); unfractionated heparin in renal failure; rivaroxaban with food; apixaban in kidney
disease; the mechanical-valve exception; antithrombin deficiency causing heparin resistance;
aspirin's irreversible COX-1 inhibition; clopidogrel/CYP2C19/omeprazole; prasugrel after TIA;
ticagrelor dyspnea; glycoprotein IIb/IIIa thrombocytopenia at 6 hours; cilostazol in heart
failure; white clot versus red clot; plasminogen → plasmin; reversing thrombolysis with
cryoprecipitate and tranexamic acid; the thrombolysis contraindication list.

**Batch 08 topics (the 8 gaps batch 07 left):** enzyme induction lowering the INR; the DOAC
boxed warning on neuraxial anesthesia; alcohol's two directions (acute inhibition, chronic
induction); the aspirin dose paradox; vorapaxar and the PAR-1 thrombin door; tenecteplase as a
single bolus; heparin's non-bleeding harms (hyperkalemia, osteoporosis); and edoxaban's
backwards renal rule.

**Batch 09 — Anemia Pharmacology (§17), 15 items:** acid and Fe²⁺ with the proton pump inhibitor;
when to abandon the oral route; premedicating an iron infusion (steroid yes, Benadryl no); ferric
carboxymaltose and FGF23-driven hypophosphatemia; acute pediatric iron poisoning → deferoxamine;
the three chelators and their boxed warnings; how long to continue iron after the hemoglobin
normalizes; hypokalemia and hyperuricemia when a stalled marrow restarts on B12; folinic acid
bypassing DHFR; the ESA mechanism and the reticulocyte-first response; the boxed warnings (11 g/dL
ceiling, 1 g/dL per 2 weeks rate rule); functional iron deficiency as apparent ESA resistance;
vadadustat and HIF stabilization; luspatercept versus an ESA in thalassemia; and complement
inhibitors requiring meningococcal vaccination.

Batch 09 uses the `anemiadrug-*` lecture slides from `assets/` the same way batch 07 used the
`anticoag-*` ones — nine of them, keyed `fig_slide_*`.

**Batch 10 topics (the 5 gaps batch 09 left):** hydroxyurea and fetal hemoglobin induction (the
gamma chain cannot enter the sickle polymer; HbF ≥ 20% as the threshold); the enteric-coated
formulation that releases its iron past the duodenum ("E-C and S-R are D-O-A"); the ESA cancer
boxed warning's third clause — never when the anticipated outcome is curative; ferumoxytol as an
iron oxide interfering with magnetic resonance imaging for ~3 months; and proximal versus terminal
complement inhibition in PNH (C3d-positive, IgG-negative direct antiglobulin test with a normal
LDH — "C3 catches more than C5").

Batch 10 adds one figure, `fig_slide_sickle_complications`, from `assets/hemolysis-19-*`.

**Batch 11 — Infection (§18–§22), 20 items:** sepsis — the bidirectional temperature and
leukocyte criteria with three qSOFA points and the time-dependent bundle; procalcitonin as the
only cause-specific row on the laboratory panel; viral sepsis triggered by DAMPs rather than
PAMPs; the source-to-organism map (abdominal → *Bacteroides fragilis*). HIV microbiology — p24
and the *gag* gene behind 4th-generation testing; the NNRTI allosteric pocket and its single-
mutation collapse; CXCR4 tropism making maraviroc useless. HIV clinical — the nonreactive screen
inside the window → HIV-1 NAT; PJP with the steroid thresholds (PaO₂ < 70 or A–a ≥ 35) and the
cholesterol-not-ergosterol reason the antifungals fail; paradoxical IRIS read off the improving
virology; CMV retinitis in the CD4 < 50 tier. Vector-borne — bubonic plague in the western US
(bipolar rods, gentamicin); the blocked proventriculus; bacillary angiomatosis versus Kaposi
sarcoma (biopsy, and why serology fails in the immunosuppressed); babesiosis with doxycycline as
the trap; chloroquine and heme polymerase. VHF — dengue and the never-NSAIDs rule; hantavirus
HFRS with its 3–9 week incubation and immunopathologic AKI; Lassa and bilateral sensorineural
hearing loss; Crimean–Congo from a *Hyalomma* tick with ~30% mortality.

Batch 11 adds 19 figures — the `sepsis-*`, `hivmicro-*`, `hivcase-*`, `bli2-*` and `vhf-*`
lecture assets. Two are stem images (the PJP chest CT, the bacillary angiomatosis lesions); the
rest are explanation slides. Note for future batches: `assets/bli2-yersinia-pestis-bipolar-*`
and `ss-infx-yersinia-bipolar` are stock images with a visible Alamy watermark — do not embed
them; the bubo photograph was used instead.

**Batch 12 topics (the 18 gaps batch 11 left):** NEWS2's six parameters against MEWS's five
(oxygen saturation is the one added); the septic shock definition as a strict subset —
fluid-refractory hypotension PLUS a cellular/metabolic abnormality; post-sepsis syndrome and how
much of it is neuropsychiatric. HIV — *gag*/*pol* cleaved by VIRAL protease while *env* is cleaved
by HOST protease (why PIs spare the spikes); integration as the irreversible step behind the latent
reservoir; cobicistat as an enhancer with no antiviral activity; JC virus and PML. HIV clinical —
the live vaccine rule and the recombinant zoster exception; U = U and the PARTNER trial; the
needlestick 72-hour window (start PEP before the source result); booster + over-the-counter nasal
steroid → iatrogenic Cushing with a LOW cortisol and ACTH. Vector — Ervebo/Zaire against a
Bundibugyo outbreak; cat scratch disease, where the inoculum is flea feces and the claw is only the
needle; secondary plague pneumonia and why it transmits by aerosol anyway; RTS,S and the sporozoite
bottleneck. VHF — Dengvaxia's prior-infection prerequisite; the M segment as the only antibody-
accessible target; New World HCPS versus Old World HFRS, settled by a normal creatinine.

Batch 12 adds 14 figures. Two stem images (the cat scratch cervical node, the plague pneumonia
chest radiograph); the rest explanation slides.

**Batch 13 — Laboratory Foundations (§23–§25), 20 items:** §23 — which three values are measured
and which are arithmetic; thalassemia versus iron deficiency separated by the erythrocyte count;
the reticulocyte count as the normocytic branch point; systematic bias versus random bias (the
15% platelet trap); side scatter and the eosinophil; the immature platelet fraction as the
reticulocyte count for platelets; the averaging trap after transfusion, caught by a wide RDW.
§24 — the feather edge that manufactures spherocytes; echinocyte versus acanthocyte (kidney vs
liver, or a bad slide); target cells with normal iron → electrophoresis; schistocytes settled by
the coagulation screen; *P. vivax* hypnozoites; the toddler's milk as a three-way cause; the
deliberately partial transfusion in a compensated chronic anemia. §25 — cold agglutinins and the
impossible MCHC; pseudothrombocytopenia recognised by the absence of bleeding; microcytes counted
as platelets; nucleated red cells inflating the white count; lipemia inflating the hemoglobin; the
uninverted tube producing an artefactual pancytopenia.

Batch 13 adds 13 figures from the `cbc-*` and `wbc-*` lecture assets. Three stem images (target
cells, schistocytes, the iron-deficiency smear) reuse figures already in the file. Note that
`cbc-20`, `cbc-21` and `wbc-07` carry burned-in labels naming the finding, so they are explanation
figures only.

**§23–§25 are covered end to end** (20 items). Batch 13 was authored under the option-length rule
below and shipped at 15% uniquely-longest before append.

**Batch 14 — Benign White Cell Disorders (§26–§28), 20 items:** §26 — computing the ANC when the
percentage looks normal; febrile neutropenia below 200/µL, where fever may be the only sign because
pus is dead neutrophils; the Duffy-null phenotype and the harm of one reference range; drugs as the
adult cause of ineffective production; why a bacteriostatic agent fails in a host who cannot finish
the job; a septic neonate whose count is suppressed rather than raised. §27 — the leukemoid
reaction with Döhle bodies, toxic granulation and vacuolization; the inverted blast pyramid with
Auer rods; the reactive lymphocytosis read off the cytoplasmic 'skirt' and the variety of
appearances; the leukoerythroblastic picture; persistent basophilia → BCR-ABL; pertussis as the
bacterium that raises lymphocytes. §28 — chronic granulomatous disease with a NORMAL neutrophil
count (the qualitative/quantitative split); the catalase logic; Bruton's 6-month maternal-antibody
window and absent tonsils; SCID where only early transplant changes the outcome; DiGeorge as one
neural crest failure with five consequences; irradiated components (leukoreduction is the trap);
live vaccines plus cocooning the household; and ADA deficiency, where transplant corrects the blood
compartment and not the neurons.

Batch 14 adds 18 figures from the `wbc-*` lecture assets, all explanation figures — `wbc-04`,
`wbc-05` and `wbc-07` carry burned-in labels naming the finding, so none is used in a stem.

**§26–§28 are covered end to end** (20 items). Two authoring notes from this batch: LO 66's FIRST
anchor is `s31b-node-architecture` (§35), so reactive-versus-malignant items must be tagged
`(66, "s24-reactive")` or they file themselves under the wrong section — this was caught after
append and corrected in place. And a lab row reading "Serum IgA undetectable (N=…)" fails
`_native()`, which splits at the first numeric token; write `<7 mg/dL` instead.

**Batch 15 — Coagulation I · Bleeding (§29–§31), 25 items:** §29 — factor 12 (long aPTT, no
bleeding) in a man with an uneventful tonsillectomy; the short-draw citrate tube and the 9:1 rule;
the incubated mixing study for a slow factor 8 antibody; a normal screen in von Willebrand disease,
because the platelets were spun out before the test began; factor 13 and delayed bleeding with
three normal screens; the isolated long PT of vitamin K deficiency (factor 7's short half-life);
what a D-dimer actually proves; heparin contamination from a line draw, proved by a normal
peripheral redraw. §30 — hemarthrosis and the expected pattern; factor assays as the only way to
separate hemophilia A from B; severity by factor level against the 50% rule; the inhibitor and the
bypassing agent; emicizumab's falsely SHORT aPTT in a trauma patient; the activity-to-antigen ratio
(type 2); desmopressin as endothelial release, not synthesis; type 2B where desmopressin is wrong;
Bernard-Soulier read off the ristocetin column plus big platelets; Glanzmann versus aspirin; the
grey zone with blood group O; and reading an X-linked pedigree. §31 — DIC with the fibrinogen TREND
as the finding; factor 5 separating vitamin K deficiency from liver disease; why a cirrhotic INR
does not justify plasma before a paracentesis; hemorrhagic disease of the newborn after a home
birth; and Heyde syndrome.

Batch 15 adds 17 figures from the `coag1-*` lecture assets, all explanation figures.

**§29–§31 are covered end to end** (25 items). Authored under the option-length rule and rebalanced
before append: 8 of 25 keyed answers started as the single longest option and 0 finished that way,
mostly by lengthening short distractors rather than trimming the answer.

**Batch 16 — the 10 Coag I gaps:** the vessel wall (hereditary hemorrhagic telangiectasia);
protein C/S inactivating factors Va and VIIIa; factor VIII separating liver disease from DIC;
thrombin's feed-forward loop; dysfibrinogenemia (bleeds AND clots); dense granule storage pool
disease with albinism; type 2N von Willebrand disease masquerading as mild hemophilia A; the
thrombin time and heparin rebound after bypass; Kasabach-Merritt phenomenon; and viscoelastic
testing in massive hemorrhage.

**Batch 17 — Coagulation II · Clotting (§32–§34), 20 items:** §32 — TTP treated on suspicion with
plasma exchange (and platelets withheld); the ADAMTS13/ultra-large multimer mechanism; Shiga toxin
HUS; atypical HUS and eculizumab; why the aHUS genotype decides transplant outcome; and a
six-row matched-set grid separating the TMAs from DIC on PT/aPTT/fibrinogen/D-dimer. §33 — factor
V Leiden as activated protein C resistance; prothrombin G20210A as a 3' UTR regulatory mutation;
antithrombin deficiency causing heparin resistance in nephrotic syndrome; neonatal purpura
fulminans; the lupus anticoagulant paradox and the excess-phospholipid confirmation; antibody
without syndrome (do not anticoagulate); and the biological false-positive RPR. §34 — the 4T score
with argatroban; why LMWH is closed off after HIT; rapid-onset HIT inside the 100-day window;
anti-Xa rather than aPTT for LMWH; duration set by the circumstances, not the genotype, with an
uninterpretable on-heparin antithrombin level; who is worth testing at all; and warfarin-induced
skin necrosis.

Batch 17 adds 15 figures from `coag2-*`, plus the existing schistocyte smear as a stem image. It
also varies option counts deliberately — one 4-option item, one 6-option matched-set grid, the rest
five — and the validator was generalised from A–E to A–H to allow it. A run of four consecutive
identical keys appeared after append and was broken by rephrasing one correct option
("Factors Va and VIIIa" → "Activated factors V and VIII"), which changes the alphabetization and
not the medicine.

**Batch 18 — Coag II top-up (8) + Lymph Node Pathology (8):** Virchow's triad; the postpartum peak;
the reversible oral-contraceptive-plus-smoking combination; essential thrombocythemia versus
reactive thrombocytosis; hyperhomocysteinemia poisoning protein C; pneumococcal HUS (neuraminidase
and the T antigen); drug/transplant-associated TMA; and a low 4T score as a reason NOT to test.
Then §35 — the node floor plan; why BCL2 is negative in a reactive germinal center; mononucleosis
versus Hodgkin decided by retained CD20/OCT2 rather than by CD30; Kikuchi-Fujimoto; Rosai-Dorfman
and emperipolesis; hyaline vascular Castleman and its dendritic-cell sarcoma risk; formalin as a
one-way door; and hemophagocytosis as one criterion of eight.

**Batch 19 — Hematologic Malignancy part 1 (§36–§39), 20 items:** the core construct (differentiation
stage sets tempo); blasts as non-functional cells in a white count of 87,000; tumor lysis (three
highs and one low); APL treated on suspicion; the grade paradox (aggressive = curable); ATRA as
differentiation therapy; flow cytometry assigning lineage; fitness rather than age deciding
induction; therapy-related AML; the 20% blast line; the MDS paradox and what actually kills in it;
CML versus a leukemoid reaction (LAP low, basophilia, BCR-ABL); reading the phase criteria (24%
basophils, 14% blasts); T315I → ponatinib; polycythemia vera; ruxolitinib helping symptoms and
survival but not counts; the two-factor ET risk score; the polycythemia split on erythropoietin
direction; and why the MPNs clot rather than fail.

Authoring note from batch 19: six of twenty items needed re-alphabetisation after drafting, all
from the same two causes — a leading "A "/"An " sorting before a longer word, and options
beginning with the same first word. Check those two patterns first when the validator flags order.

### File size and the 30 MB delivery limit

At 301 questions and 151 figures the file reached 32.4 MB, and 95% of that was embedded base64
images. That crosses the 30 MB ceiling for sending a file to phone/web viewers, so the desktop app
received it and Remote Control did not.

Fix applied in place: every embedded figure was decoded, re-encoded at `-Z 900` / quality 80, and
kept only if the result was SMALLER than the original (so nothing is ever degraded upward).
Embedded bytes fell 30.9 MB → 20.0 MB and the file 32.4 MB → 20.5 MB, with no question touched.
Figures now render at 900px wide, which is still above the display width in the quiz.

For future batches: source figures in `figs/` are still created at 1100px, so the shrink step can
be re-run on the live file whenever it approaches the limit again. Roughly 30 more figures is the
headroom before it needs repeating.

### Option-length audit (run after batch 12)

A test-wise student can score above chance by picking the longest option, so the length of the
correct answer must not stand out. The first audit of all 206 items found a real leak:

| Metric | Before | After | Chance |
|---|---|---|---|
| Correct option is the single longest | 35.4% | 8.3% | 20% |
| Correct option is the single shortest | 18.4% | 15.0% | 20% |
| Mean length rank of the correct option (1 = longest) | 2.37 | 2.90 | 3.00 |
| Mean excess length over the distractors | +6.9 chars | +0.8 chars | 0 |

Fifty-nine questions were rebalanced, preferring to LENGTHEN the short distractors with true,
specific clauses (which also makes them more plausible) and trimming the correct option only
where wording was redundant. No medicine was changed. The rebalance script re-alphabetises each
edited question and remaps both `correct` and the `wrongExplanations` keys, so nothing silently
drifts — see `scratchpad/rebalance.py` for the pattern.

**Rule for future batches:** before appending, check that the keyed option is not the longest.
The quickest fix is to give two distractors an extra true qualifier rather than to cut the answer.

**Known drift:** these 59 edits were applied to the live quiz file only. The batch modules in
`quiz-toolchain/` still hold the original wording. That is harmless — `append_quiz.py` only ever
appends new questions — but the modules are no longer a byte-exact record of what is in the file.

**§18–§22 are covered end to end** (38 items across batches 11 and 12). §20's only listed objective
is LO 77, so the HIV-clinical items carry `(77, "s19-hiv-clinical")` in the anchor form.

**§15–§16 are covered end to end** (33 items across batches 07 and 08). **§17 is covered end to
end** (20 items across batches 09 and 10).

**§12–§14 are covered end to end** (30 items across batches 05 and 06), weighted per a
third-year's advice toward products/indications and the reaction differential. Batch 06's
final item is the first COMMUNICATION/ETHICS question in the series — the house style calls
for one wherever the content touches patient interaction, and batches 01–05 had none.

**§8–§10 are now covered end to end** across batches 03 and 04 (35 items). Not given their
own item, and named in explanations instead: the hemoglobin H inclusion stain, exchange
transfusion arithmetic, and the gene therapies (Casgevy, Lyfgenia).

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
├── Jeevs edition _ summative review.html                    ← THE LIVE QUIZ — batches 01+02+03, append here
├── Jeevs Edition - Hematopoiesis and Marrow Quiz.html        ← batch 01, standalone
├── Jeevs Edition - Anemia I Impaired Production Quiz.html    ← batch 02, standalone
├── QUIZ_BUILD_METHOD.md                            ← this file
└── quiz-toolchain/
    ├── build_quiz.py                               ← clones template, injects Q + figures + LO blocks
    ├── append_quiz.py                              ← appends a batch to an existing quiz, in place
    ├── questions_batch01_hematopoiesis_marrow.py
    ├── lo_tags_batch01.py
    ├── questions_batch02_anemia1_impaired_production.py
    ├── lo_tags_batch02.py
    ├── questions_batch03_anemia2_hemolysis.py
    ├── lo_tags_batch03.py
    └── figs/                                       ← resized JPEGs, keyed fig_*
```

To start the next batch: copy the latest `questions_batchNN_*.py` and `lo_tags_batchNN.py`
to the next number, replace the contents, add any new figures to `figs/`, and run
`append_quiz.py` with the new filenames (§8) — appending to the live quiz, not building a
new file.

---

## Batch 20 — Hematologic Malignancy, part 2 (lymphoid)

**Sections §40, §41, §42 · native LOs 3, 21, 30, 40, 41, 56, 57, 67 · 26 questions · 16 new figures.**

**§40 (12):** acute lymphoblastic leukemia leaves the marrow, so the meninges are a sanctuary site →
intrathecal chemotherapy for every patient; the favorable/unfavorable prognostic lists in childhood
leukemia (age 2–5 is favorable, which is also the peak incidence group); BCR::ABL1 in adult
precursor-B disease → add a tyrosine kinase inhibitor; the naming convention (leukemia = marrow,
lymphoma = mass) read off a thymic T-lymphoblastic mass; double hit lymphoma at ~30% survival beating
the worst possible International Prognostic Index score of 50%; a lymphocyte count of 68,000 that is
**not** a treatment indication; a falling hemoglobin in CLL that is autoimmune hemolysis, not marrow
infiltration → direct antiglobulin test; alcohol-induced nodal pain → **excisional** biopsy, because
the Reed–Sternberg cell is 1–2% of the tissue; IgM hyperviscosity → emergent plasmapheresis; gastric
MALT cured by eradication; nodal marginal zone cured by treating hepatitis C; CD5+/CD23− → mantle
cell and cyclin D1.

**§41 (11):** nodular sclerosis vs mixed cellularity settled by **fibrosis alone**; why PAX5 beats
CD20 (a graded result with a built-in internal control); NLPHL retaining its B-cell program → the
rituximab target; contiguous vs noncontiguous spread, with abdominal disease over a clean neck and
chest as the non-Hodgkin signature; Burkitt (MYC, BCL2 negative, Ki-67 > 95%) against follicular
(BCL2 positive, t(14;18)) — grow-fast vs die-slow; BCL2 inside a follicle as the one stain that
separates lymphoma from hyperplasia; hairy cell leukemia found by **monocytopenia plus a dry tap**;
mycosis fungoides → Sézary, confirmed by the same clone in blood and skin; dermatopathic
lymphadenopathy as the staging trap; ALCL vs classic Hodgkin settled by ALK (and sheets vs scattered
cells); ATLL flower cells, HTLV-1 geography and hypercalcemia.

**§42 (3):** the two numbers 10 and 3 separating MGUS from smoldering myeloma, and the front-loaded
smoldering risk curve that drives 4-monthly rather than 6-monthly surveillance; free light chains
causing cast nephropathy behind a modest electrophoresis spike and a bland urinalysis; myeloma vs
Waldenström — bone and kidney vs viscosity and nerve.

### The option helper — adopted in batch 20, use it from now on

Hand-alphabetising options caused ~30 defects across batches 11–19 and six in batch 19 alone. Batch 20
supplies options as a **dict `{option text: wrong-answer explanation}`** and lets the helper sort:

```python
def q(stem, opts, correct, explanation, eli5, image=None, ...):
    bodies = sorted(opts, key=str.lower)        # same key the validator uses
    ci = bodies.index(correct)
    d = {"choices": [f"{chr(65+i)}. {b}" for i, b in enumerate(bodies)],
         "correct": ci,
         "wrongExplanations": {str(i): opts[b] for i, b in enumerate(bodies) if i != ci}}
```

The correct answer is named by its **text**, not its index, so nothing has to be renumbered. Batch 20
passed the alphabetical, wrongExplanations-key and letter-prefix checks on the first run — the first
batch in the series to do so. It also removes the need for the `rebalance.py` re-sort step; only the
option-length audit remains manual (batch 20 shipped at 1 of 26 uniquely longest before a one-word
fix, then 0).

### Figures

Sixteen `lpd-*` lecture assets, keyed `fig_lpd_*`. Stem images: the nodular sclerosis low-power
(collagen bands), the gastric lymphoepithelial lesion, the starry sky, back-to-back follicles, the
hairy cell, Pautrier microabscesses, ALCL hallmark cells, ATLL flower cells, and the CLL smudge-cell
smear. Explanation figures: the Reed–Sternberg cell, the PAX5 comparison, popcorn cells, the neoplasm
origin map, the Hodgkin-vs-non-Hodgkin table, the follicular-vs-reactive comparison, and the mycosis
fungoides plaques.

Only two carry any burned-in marking, and neither names a finding: arrows on the smudge-cell and
hallmark-cell images (described in the caption as "arrows"), and a `©WebPathology` watermark on the
Pautrier image. `lpd-sezary-syndrome-blood-labeled`, both WHO classification tables and both summary
tables are **labelled** and were not used.

These were resized at `-Z 780 -s formatOptions 62` because the file was already at 24 MB. After the
append the file hit 28.3 MB, so the whole figure library was re-encoded in place at
`-Z 850 -s formatOptions 68`, keeping each result only if smaller: **embedded 26.6 → 20.0 MB, file
28.3 → 21.8 MB.** Run that sweep whenever the file passes ~26 MB; it is lossless in practice at this
viewing size and buys back two batches of headroom.

### State after batch 20

**363 questions · 185 figures · 21.8 MB · 70 of 83 objectives covered, 13 remaining.**
8.5% uniquely-longest options, longest answer-key run 3.

| Batch | Block | Review sections | Native LOs | Qs | File |
|---|---|---|---|---|---|
| 20 | Hematologic Malignancy, part 2 (lymphoid) | §40, §41, §42 | 3, 21, 30, 40, 41, 56, 57, 67 | 26 | appended to `Jeevs edition _ summative review.html` |

The 13 uncovered objectives, grouped as they would be written:

- **Chemotherapy pharmacology (§43, §45, §46)** — LO 64 (principles that enhance a regimen), LO 11
  and LO 16 (targeted therapy and immunotherapy: mechanisms, toxicities), LO 15 (hormonal therapy
  toxicities). Four objectives, three sections — the largest remaining block.
- **Spleen and splenic trauma (§55, §11, §52)** — LO 73 (mechanisms of splenic injury, anatomy,
  rupture/abscess/infarct/pseudoaneurysm) and LO 47 (management of traumatic splenic injury).
- **Lymphatics (§48, §56, §57)** — LO 34 (post-traumatic edema) and LO 60 (anatomic pathways of
  lymphatic dissemination in metastatic carcinoma).
- **Anemia stragglers** — LO 42 and LO 55 (§3, the MCV-based differential and the management plan)
  and LO 35 (§7, porphyria and lead poisoning). These three are the only *content* gaps left outside
  the untouched blocks; §3 is well covered by questions tagged to neighbouring objectives, so LO 42
  and LO 55 are largely a tagging gap rather than a knowledge gap.
- **Deep vein thrombosis diagnosis (§49)** — LO 10. Adjacent to the covered §34 VTE management
  material.
- **Prescription writing (§54)** — LO 78.

---

## Batch 21 — Antineoplastic pharmacology, lymphatics & thrombosis

**Sections §43, §45, §46, §48, §56, §57, §49 · native LOs 10, 11, 15, 16, 34, 60, 64 · 25 questions ·
13 new figures.** The first batch to span three blocks, because the remaining objectives were
scattered rather than clustered.

**§43 traditional chemotherapy (7):** why combination regimens require differing mechanisms AND
differing toxicities — the second half being a dosing argument, since overlapping toxicity forces
dose reduction (R-CHOP as the worked example); the log-kill hypothesis and the 10⁹-cell / 1-gram
detection threshold that justifies adjuvant therapy after a "complete" resection; MDR1 and
P-glycoprotein producing cross-resistance to structurally unrelated drugs; the G0 problem —
methotrexate (cell cycle-specific) versus cyclophosphamide (nonspecific); mesna and acrolein, taught
as one of three rescue agents; **intrathecal vincristine is uniformly fatal**, and the minibag that
makes the error physically impossible; oxaliplatin's cold-induced pharyngolaryngeal dysesthesia,
explicitly not an allergy.

**§45 targeted therapy and immunotherapy (8):** size decides format — no monoclonal antibody can hit
an intracellular target, which is why every signal transduction inhibitor is a small molecule;
trastuzumab and HER2 on cardiomyocytes as the cleanest case of toxicity following the target's normal
tissue distribution; reading an antibody-drug conjugate's payload out of its generic name
(-emtansine/-vedotin → neuropathy; -deruxtecan/-govitecan → myelosuppression); the EGFR acneiform
rash as on-target toxicity rather than allergy, separated from an infusion reaction by timing;
cytokine release syndrome at 9 hours → tocilizumab; **ICANS on day 6 → dexamethasone and a
non-sedating anticonvulsant, NOT tocilizumab**; checkpoint colitis → corticosteroids, with loperamide
as the named trap; daratumumab, CD38 on red cells, and the panreactive antibody screen that can mask
a real alloantibody.

**§46 hormonal therapy (3):** why an aromatase inhibitor fails in a premenopausal woman; SERM versus
aromatase inhibitor read off the bone finding (agonist in bone and endometrium versus estrogen
removed everywhere); leuprolide tumour flare causing cord compression, and the mandated concurrent
anti-androgen.

**§48 / §56 lymphedema and post-traumatic edema (3):** the Stemmer sign and the discriminating triad
(unilateral → not heart failure; negative ultrasound → not a clot; square toes → lymphedema) after a
groin operation; filariasis as the worldwide cause, which is the same picture decided by a history
question about geography; acute compartment syndrome at 6 hours, where the palpable pulses are the
trap because it is a capillary-perfusion problem.

**§57 lymphatic spread (2):** Virchow's node and the thoracic duct's left-sided termination (with the
right lymphatic duct as the contrast); the sentinel node, whose point is avoiding the dissection that
is itself the commonest cause of lymphedema in the developed world.

**§49 DVT/PE diagnosis (2):** duplex ultrasound first in a swollen limb 9 days post-arthroplasty,
with the tempo clue — swelling that had improved and then worsened again; and **the V/Q scan, not CT
angiography, as the screening test for chronic thromboembolic pulmonary hypertension.**

### Notes

- The option helper (batch 20) again produced zero alphabetical and zero wrongExplanations-key
  errors on the first run. The only manual step was the option-length audit: 5 of 25 keyed answers
  were uniquely longest (20%, exactly chance), fixed to **0 of 25** by lengthening distractors with
  true qualifiers — "cross-links" → "interstrand cross-links", "red cell" → "red blood cell".
- **LO 34's first-listed anchor is `s53-traumatic-edema` (§56), not the lymphedema section.** The two
  lymphedema items therefore need `(34, "s43-lymphedema")`; only the compartment syndrome item takes
  a bare `34`. Same trap as LO 66 in batch 14.
- LO 31's anchors are `s11-products` and `s12-immuno` — there is no `s13-compatibility`. The
  daratumumab item's cross-block tag uses `(31, "s12-immuno")`.
- Figures: 13 `chemo-*` and `lymph-*` lecture assets at `-Z 850 -s formatOptions 68`, ~976 KB total.
  All are explanation figures except the established-lymphedema photograph, which is clean and
  unlabelled and is used as a stem image. The Chemo Man mnemonic slide (`chemo-10`) is worth reusing
  heavily — it is the organ-toxicity map the combination-therapy rule depends on.

### State after batch 21

**388 questions · 198 figures · 23.2 MB · 77 of 83 objectives covered, 6 remaining.**
8.0% uniquely-longest options, longest answer-key run 3.

| Batch | Block | Review sections | Native LOs | Qs | File |
|---|---|---|---|---|---|
| 21 | Antineoplastic pharmacology, lymphatics & thrombosis | §43, §45, §46, §48, §49, §56, §57 | 10, 11, 15, 16, 34, 60, 64 | 25 | appended to `Jeevs edition _ summative review.html` |

Remaining objectives, and what each would need:

- **LO 73 (§55, §11, §52) and LO 47 (§55)** — the spleen: mechanisms of splenic injury, key anatomy
  and physiology, rupture/abscess/infarct/pseudoaneurysm, and the medical, surgical and
  interventional management of traumatic splenic injury. The largest remaining block; ~8 questions.
- **LO 35 (§7)** — porphyria and lead poisoning. A genuine content gap; ~4 questions.
- **LO 78 (§54)** — writing a complete prescription. ~2–3 questions.
- **LO 42 and LO 55 (§3)** — the MCV-based differential of anemia and the management plan. Largely a
  TAGGING gap: §3's content is heavily covered by questions tagged to LOs 18, 19, 20, 25, 28 and 49.
  Either write 2–3 explicitly §3-anchored items, or retag existing ones.

---

## Batch 22 — Chemotherapy toxicity, lymphatic structure, and the batch-21 gaps

**Sections §44, §47, §43, §45, §46, §56, §57 · native LOs 11, 15, 16, 17, 34, 60, 63, 64 ·
20 questions · 6 new figures.** Written after a per-section density audit showed that batch 21's
three blocks had two sections with **zero** questions despite each carrying an objective.

**§44 chemotherapy toxicity — LO 17, previously 0 questions (8):** bleomycin pulmonary fibrosis,
identified by *normal blood counts* (it sits in the mildest myelosuppression tier, and the lung lacks
bleomycin hydrolase); the vinca split — vinCRIStine → CRIS-py nerves, vinBLAStine → BLASts;
cumulative lifetime anthracycline dose across a whole life, not per regimen; irinotecan's two
diarrheas — early cholinergic → **atropine**, late → loperamide; the antiemetic suffixes (-pitant =
neurokinin-1, -setron = 5-HT3), with a regimen deliberately containing one of each; cytarabine's
eye-and-cerebellum pairing and the *prophylactic* steroid drops; procarbazine as a monoamine oxidase
inhibitor and the tyramine crisis; plerixafor as a CXCR4 antagonist for stem cell mobilization, which
loops back to the CXCR4/CXCL12 niche from batch 01.

**§47 lymphatic structure — LO 63, previously 0 questions (4):** the **left internal jugular line →
chylothorax**, including why the first film is normal (chyle accumulates over hours and rises with
feeding); why lymphatic obstruction swells more than venous obstruction (lymph is protein-rich, and
the protein has no alternative exit); ileocecal resection in an infant → loss of the major site of
IgA production → bacterial translocation, contrasted with *inherited* selective IgA deficiency;
thymic positive selection, cortex → medulla, non-responders apoptose.

**Top-ups (4):** topoisomerase I vs II (the enzyme number is the strand number); why checkpoint
inhibitors are engineered as **IgG4** — you must not lyse the T cell you are activating — with the
-omab/-ximab/-zumab/-umab nomenclature; lenalidomide → venous thromboembolism requiring prophylaxis;
abiraterone → CYP17 blockade → mineralocorticoid excess → why prednisone is co-prescribed.

**§56/§57 (4):** hypoalbuminemia after large-volume resuscitation as the one mechanism producing
*generalized* rather than local edema; inflammatory capillary leak as the **expected** swelling, with
the negatives in the stem excluding the two emergencies; testis → para-aortic (not inguinal) versus
scrotal skin → superficial inguinal; the dentate line watershed.

### Notes

- Option helper: again zero alphabetical and zero key errors on the first run. Manual fixes were the
  option-length audit (4 of 20 uniquely longest → **0**) and a **run of four identical answer keys**
  at Q1–Q4, broken by rewording one correct option ("Her cumulative lifetime anthracycline exposure"
  → "The cumulative lifetime anthracycline dose she has already received") so it sorted to a
  different letter. Check the key run as well as the length distribution before appending.
- **LO 63's first-listed anchor is `s31b-node-architecture` (§35), not §47.** All four lymphatics
  items need `(63, "s42-lymphatics")`. Third instance of this trap, after LO 66 (batch 14) and
  LO 34 (batch 21) — *always* check `anchors[0]` against the section you are writing.
- LO 76 is anchored to §26 (`s23-wbc-normal`), not to mucosal immunity; the IgA item carries LO 63
  alone rather than a misleading second tag.

### State after batch 22

**408 questions · 204 figures · 24.0 MB · 77 of 83 objectives · 7.6% uniquely-longest · key run 3.**

Every section that carries an objective now has questions behind it, except the six listed below.
Section density for the batch-21/22 blocks: §43 → 8, §44 → 8, §45 → 10, §46 → 4, §47 → 4, §48 → 2,
§49 → 2, §56 → 3, §57 → 4.

| Batch | Block | Review sections | Native LOs | Qs | File |
|---|---|---|---|---|---|
| 22 | Chemo toxicity, lymphatic structure, batch-21 gaps | §43–§47, §56, §57 | 11, 15, 16, 17, 34, 60, 63, 64 | 20 | appended to `Jeevs edition _ summative review.html` |

Still uncovered — unchanged by this batch, which was a density fix rather than a coverage fix:

- **LO 73, LO 47** — the spleen (§55, §11, §52). ~8 questions. The largest remaining block.
- **LO 35** — porphyria and lead poisoning (§7). 35k of source, zero questions. ~4.
- **LO 78** — writing a complete prescription (§54). ~3.
- **LO 42, LO 55** — the MCV differential (§3). A tagging gap, not a knowledge gap.

---

## Batch 23 — Pediatrics, spleen & prescribing · Trauma, edema & metastasis · Geriatrics

**Sections §51, §52, §11, §55, §54, §56, §57, §53, §58 · native LOs 34, 47, 51, 60, 65, 67, 73, 77,
78 · 25 questions (10 / 10 / 5) · 8 new figures.** Nine sections, seven of which had **zero**
questions before this batch.

**Group 1 — pediatrics, spleen & prescribing (10).** §51: the pancytopenic child split by
*how the child looks* (well + acellular marrow = aplastic; sick + splenomegaly + packed marrow =
leukemia, with a LOW white count as the trap); Fanconi vs TAR decided entirely by the thumbs;
Wiskott-Aldrich found by **small** platelets when every other thrombocytopenia gives large ones;
the childhood-ALL prognostic grid (hyperdiploid and t(12;21) favorable, hypodiploid and t(9;22)
adverse). §52/§11: congestive hypersplenism from portal hypertension, where the normal marrow and
normal morphology prove peripheral removal and splenectomy is **not** indicated; splenic vein
thrombosis after pancreatitis → isolated gastric fundal varices → splenectomy curative; OPSI
prevention with the 2-weeks-before / before-discharge timing split; Howell-Jolly bodies as proof of
autosplenectomy, making fever an emergency. §54: the missing "Disp:" line, and the patient-safety
writing conventions as a five-option grid.

**Group 2 — trauma, edema & metastasis (10).** §55: unstable + positive FAST → laparotomy, never the
scanner; stable + contrast blush → embolization (with the CT as a stem image); **delayed rupture on
day 5–6**, which is why NOM is inpatient observation; spontaneous rupture in mononucleosis;
post-splenectomy thrombocytosis > 1 million → aspirin; pancreatic tail injury found by a raised
*drain* amylase with a normal serum amylase. §56: hematoma — immediate, focal, fluctuant, with
expanding size as the alarm (completes all six mechanisms across batches 21–23). §57: the
subcapsular sinus as the first compartment examined; why carcinoma prefers lymphatics (no basement
membrane, overlapping junctions) against carcinoma-by-lymph / sarcoma-by-blood; the medial breast
quadrant draining to internal mammary nodes a sentinel axillary biopsy never samples.

**Group 3 — geriatrics (5).** Marrow cellularity = (100 − age), read as *normal* at 25% in an
82-year-old; **anemia is never "just age"** — WHO thresholds regardless of age, a >10% fall from the
patient's own baseline, and iron deficiency as a gastrointestinal lesion until proven otherwise;
inflammaging in a virologically suppressed patient with a normal CD4; ADL vs IADL, where
**instrumental activities fail first** and the case chain runs cognitive impairment → medication
mismanagement → anticoagulant overdose → hematoma; and the three "there are no safe medications
for…" slides, where dementia behaviours are the only one with **no drug concession at all**.

### Notes

- Option helper: zero alphabetical and zero key errors again. Manual work was the length audit
  (3 of 25 uniquely longest → 0) and nothing else — no key run above 2.
- Renumbering trap: a question inserted mid-file shifts every subsequent tag. Insert the question
  **and** re-key `LO_TAGS` in the same edit, then re-run the validator before appending.
- Figures: 8 from `lymph-*` and `ss-*`. The ALL blood smear (`ss-heme-all-lymphoblasts`) and the
  splenic injury CT (`lymph-40`) are clean enough for stems — the CT carries an arrow and arrowhead
  but no text, so the caption names them as arrows without naming the finding.

### State after batch 23

**433 questions · 211 figures · 24.9 MB · 80 of 83 objectives · 7.2% uniquely-longest · key run 3.**

| Batch | Block | Review sections | Native LOs | Qs | File |
|---|---|---|---|---|---|
| 23 | Peds/spleen/prescribing · trauma/edema/metastasis · geriatrics | §11, §51–§58 | 34, 47, 51, 60, 65, 67, 73, 77, 78 | 25 | appended to `Jeevs edition _ summative review.html` |

**Three objectives remain**, and only one is a real content gap:

- **LO 35 (§7, `s6b-porphyria`)** — porphyria and lead poisoning. 35k of source, **zero** questions.
  The last untouched topic in the file. ~4 questions.
- **LO 42 and LO 55 (§3, `s3-anemia-eval`)** — the MCV-based differential and the management plan.
  A *tagging* gap: §3's content is covered by questions tagged to LOs 18, 19, 20, 25, 28 and 49.
  Either write 2–3 explicitly §3-anchored items, or retag existing ones.

---

## Batch 24 — Porphyria, lead, and the anemia differential — the file is complete

**Sections §7, §3 · native LOs 35, 42, 55 · 8 questions · 4 new figures.** The last coverage gap.

**§7 porphyria and lead (5):** the acute intermittent porphyria vignette — a young woman on a new
oral contraceptive with pain out of all proportion to a soft abdomen and normal imaging, autonomic
instability, hyponatremia and urine that darkens on standing → **spot urine porphobilinogen and
δ-aminolevulinic acid, collected during the attack**; lead poisoning found by the one-enzyme
discriminator (**ALA up + PBG up = porphyria; ALA up + PBG NORMAL = lead**, because lead blocks ALA
dehydratase one step earlier); porphyria cutanea tarda with its hepatitis C / alcohol / dialysis
associations and the **hemochromatosis gene in two-thirds**; the ALAS1 negative-feedback loop, which
explains every precipitant and both treatments (glucose suppresses PGC-1α, hemin restores end-product
inhibition); and the lecture's own thesis — the obstacle is not the test, it is that the diagnosis
never enters the differential, with 26% initially misdiagnosed.

**§3 the anemia differential (3):** extrinsic vs intrinsic destruction, with hypersplenism as the
clean example of a normal cell destroyed by its environment; the **mean corpuscular volume as an
average** — a post-bypass patient whose combined iron and B12 deficiency reads as normocytic, exposed
by a distribution width of 21.4%; and the algorithm run end to end in renal anemia (normocytic → low
reticulocytes → creatinine names it → confirm iron stores → erythropoiesis-stimulating agent below
10 g/dL).

### Note on figures

`porph-porphyria-cutanea-tarda-hands` has **the diagnosis printed across the image** — explanation
figure only, never a stem. The rule from batch 03 held up right to the last batch: confirm by
viewing, never by reading the caption.

---

## Final state — 21 September 2026 exam

**441 questions · 215 figures · 25.4 MB · 83 of 83 objectives covered.**
7.0% uniquely-longest keyed answers (chance is 20%), longest answer-key run 3.
Whole-file browser check: all 441 questions carry an LO chip, every lab block renders as a native
`lab-row` table, and every stem and explanation figure resolves.

Three review sections still have no questions filed to them as a *primary* anchor, and all three are
deliberate:

- **§50 `s45-itp`** — its objective (LO 36) is covered by the Coagulation I · Bleeding items, which
  are anchored to §29–§31.
- **§59 `s50-atlas`** and **§60 `s51-charts`** — reference material carrying no objectives.

Five objectives are carried by a single question each (18, 54, 59, 81, 82). If there is ever another
pass, that is where to add depth rather than breadth.

### Batch history

| Batch | Block | Qs |
|---|---|---|
| 01–02 | Hematopoiesis & Marrow · Anemia I | 50 |
| 03–04 | Anemia II · Hemolysis | 35 |
| 05–06 | Transfusion Medicine | 30 |
| 07–08 | Hemostasis Pharmacology | 33 |
| 09–10 | Anemia Pharmacology | 20 |
| 11–12 | Infection | 38 |
| 13 | Laboratory Foundations | 20 |
| 14 | Benign White Cell Disorders | 20 |
| 15–16 | Coagulation I · Bleeding | 35 |
| 17–18 | Coagulation II · Clotting + Lymph Node Pathology | 36 |
| 19–20 | Hematologic Malignancy (myeloid, then lymphoid) | 46 |
| 21–22 | Antineoplastic pharmacology, lymphatics, thrombosis | 45 |
| 23 | Peds/spleen/prescribing · trauma/edema/metastasis · geriatrics | 25 |
| 24 | Porphyria, lead, and the anemia differential | 8 |

### What made the difference, in order

1. **Writing from the review file's numbered sections**, not the raw lecture notes — and checking
   each block's native objectives before writing a single item (§2).
2. **The heme data-consistency rules** (§3) — Hct ≈ 3 × Hgb, MCV matching morphology, reticulocytes
   as the production/destruction switch, the hemolysis panel moving as a unit, iron studies as one
   coherent row.
3. **The option helper** (batch 20 onward) — supplying options as `{text: wrong-explanation}` and
   letting the code alphabetise and re-key. It ended roughly thirty hand-sorting defects across
   batches 11–19, and every batch since has passed those checks on the first run.
4. **The option-length audit** (after batch 12) — the keyed answer must never be the single longest
   option. File-wide this went from 35.4% uniquely longest to 7.0%.
5. **Checking `anchors[0]`** before tagging. Three objectives (66, 34, 63) list a section other than
   the one you are writing, and a bare tag sends the chip to the wrong place.
6. **Viewing every figure before using it in a stem.** Captions lie; burned-in labels do not.

---

## Final answer-length audit (post-batch-24, whole file)

Re-run properly rather than trusting the single per-batch metric. The earlier check only counted
"keyed answer is uniquely longest", which misses two things: over-correction toward SHORT answers,
and the fact that a reader cannot see a 1–3 character difference, so "one character shorter than the
longest" still looks longest.

### Metrics used

1. **Uniquely longest / uniquely shortest** — the classic tell, and its mirror.
2. **Normalized length rank** of the keyed answer, 0 = shortest option, 1 = longest. Ties get the
   average rank. 0.500 is perfectly neutral.
3. **"Looks longest within ±N characters"**, compared against an empirical chance rate computed by
   picking a random option in each question 300 times. This is the honest version, because it treats
   a near-tie as a tie.

### Result before the fix

| Metric | Value | Chance |
|---|---|---|
| Uniquely longest | 31 (7.0%) | 20.0% |
| Uniquely shortest | 84 (19.0%) | 20.0% |
| Normalized rank (mean) | 0.470 | 0.500 |
| Keyed vs mean distractor length | −0.6 chars (98.2%) | — |
| Looks longest ±0 | 12.9% | 26.1% |
| Looks longest ±2 | 23.8% | 33.8% |

No tell in either direction — below chance at every tolerance, and the shortest-answer rate was
exactly chance, so the earlier rebalancing had not over-corrected.

**What the audit did find:** the rank histogram had a lump at "second longest" (34.7% vs 20%
expected), which is the fingerprint of the fix method — lengthening one distractor by just enough to
clear the keyed answer. Cosmetic rather than real. Isolating the cases that a reader could actually
see gave **8 questions (1.8%) where the keyed answer was uniquely longest by 5 or more characters**:
Q14, Q17, Q22, Q212, Q272, Q275, Q289, Q292.

### The fix

Each was rebalanced by lengthening a distractor with a true qualifier, or shortening a verbose keyed
answer — never by trimming content out of the answer. Examples:

- Q212 "Recovering marrow production, with a rise expected shortly" → "…before the count rises",
  and a distractor lengthened to tie it.
- Q272 "Immune thrombocytopenia" → "Chronic immune thrombocytopenic purpura" (the keyed answer,
  *hereditary hemorrhagic telangiectasia*, is a fixed disease name and could not be shortened).
- Q275 "Calcium is a required cofactor at every step of the cascade" → "…at nearly every step of the
  coagulation cascade".

Edits were applied with a patcher that re-alphabetizes, recomputes `correct`, and re-keys
`wrongExplanations` **by option text rather than by index** — the only safe way to edit an option in
an alphabetized set.

### Result after the fix

| Metric | Value | Chance |
|---|---|---|
| Uniquely longest | **23 (5.2%)** | 20.0% |
| Uniquely shortest | 85 (19.3%) | 20.0% |
| Normalized rank (mean) | 0.463 | 0.500 |
| Looks longest ±0 | **11.3%** | 23.1% |
| Looks longest ±2 | **22.7%** | 32.7% |
| Uniquely longest by 5+ chars | **0** | — |

Integrity re-verified: letter prefixes, alphabetical order, `wrongExplanations` keys and duplicate
options all clean across 441 questions, and the whole file re-checked in the browser (all 441 carry
an LO chip, all lab blocks render, all 215 figures resolve).

**Standing note on the alphabetical check:** it flags five questions — Q10, Q53, Q62, Q80, Q87 —
which are ordered NUMERIC series (`0.8%, 1.6%, 4.0%, 8.0%, 16.0%`; `10,000 … 100,000/mm3`). Numeric
order is correct there and must not be "fixed". These are the documented false positives.

### For any future batch

Run all three metrics, not just "uniquely longest". The threshold that matters is **uniquely longest
by 5+ characters**, which should be zero — a near-tie is invisible to a reader and is not a defect,
so chasing it produces the cosmetic second-longest lump rather than a genuinely neutral set.

---

## What the built-in randomizer does and does not invalidate

The app reshuffles answer choices at run time. Verified against the template source and empirically:

- `randomizeQuestionChoices()` Fisher-Yates shuffles the options, carrying each option's
  `wrongExplanation` with it as a bound property, then rebuilds `correct` from the new position.
- `stripChoiceLabel()` removes the baked-in `A. ` / `B. ` prefix and `choiceLetter(index)` re-letters
  by DISPLAY position.

**Empirical check: 441 questions × 5 shuffles = 2,205 trials — the keyed answer was never lost and
no wrong-answer explanation was ever attached to the wrong option.**

### Therefore these were wasted effort — do not repeat them

- **Answer-key letter distribution and runs.** The student never sees the source letters. The run of
  four identical keys broken in batch 17 (rephrasing "Factor Va and VIIIa" → "Activated factors V
  and VIII") and again in batch 22 (rewording the anthracycline option) achieved nothing. The
  earlier guidance in §8 — "fix only if one letter is correct for more than half the batch, or 4+
  consecutive items share a key" — should simply be ignored.
- **Alphabetical order as a student-facing property.** Keep alphabetizing, because it makes the
  build deterministic and matches NBME house style in the source, but it is invisible in play and is
  not worth a single minute of rebalancing.

### These remain fully valid

- **The whole answer-length audit.** Shuffling changes position, not length. "The longest option is
  the answer" is a positional-INDEPENDENT tell, so every figure in the audit above stands exactly as
  measured.
- **No answer-letter references in prose** — this matters MORE because of the shuffle, not less.
  A file-wide sweep for letter references, positional phrases and "all of the above" returned
  15 flags, **all false positives**: blood group antigens ("A and B antigens"), hemophilia A or B,
  hemoglobin F or A, and the D and E regions of the fibrin monomer. Zero genuine references.
- Everything about content, data consistency, LO tagging and figures.

### One real casualty — ordered numeric series get scrambled

The shuffle is unconditional, so the four questions whose options form an ordered numeric or ordinal
series are displayed out of order. Observed live:

| Question | Source order | Example displayed order |
|---|---|---|
| Q10 | 0.8 / 1.6 / 4.0 / 8.0 / 16.0% | 0.8 / **8.0** / **4.0** / **1.6** / 16.0% |
| Q53 | 0.9 / 2.8 / 3.2 / 6.0 / 12.9% | 2.8 / 6.0 / 12.9 / **0.9** / 3.2% |
| Q62 | One / Two / Three / Four of four | **Four** / **One** / **Three** / **Two** of four |
| Q87 | 10,000 … 100,000/mm3 | 10,000 / **25,000** / **50,000** / **20,000** / 100,000/mm3 |

(Q80, the 0 / 1-in-8 / 1-in-4 / 1-in-2 / 3-in-4 probability item, behaves the same way.)

This is a readability regression, not a correctness one — the answer and its explanation still track
correctly. NBME convention keeps numeric options in numeric order so the reader can scan them. There
is **no data-level fix**: the shuffle has no exemption. Correcting it would mean a ~5-line patch to
`randomizeQuestionChoices()` to skip shuffling when every option parses as a number. That is a
change to the quiz engine rather than to the question bank, so it has been left alone and flagged
here instead.

### Patch applied — ordered numeric series are no longer shuffled

Two helpers were added immediately above `randomizeQuestionChoices()`, and one line inside it
changed. This is the ONLY engine change made to the file.

```js
function parseChoiceNumber(text){        // "0.8%" → 0.8 · "10,000/mm3" → 10000
  var t=stripChoiceLabel(text).trim();   // "1 in 8" → 0.125 · "Three of four" → 3
  var frac=t.match(/^(\d+)\s+in\s+([\d,]+)/i);
  if(frac)return parseFloat(frac[1])/parseFloat(frac[2].replace(/,/g,''));
  var words={zero:0,one:1,two:2,three:3,four:4,five:5,six:6,seven:7,eight:8,nine:9,ten:10};
  var w=t.split(/[\s,]+/)[0].toLowerCase();
  if(Object.prototype.hasOwnProperty.call(words,w))return words[w];
  var m=t.match(/^[<>~≤≥]?\s*([\d,]+(?:\.\d+)?)/);
  if(m)return parseFloat(m[1].replace(/,/g,''));
  return null;
}
function isOrderedNumericSeries(items){  // every option numeric AND strictly ascending
  if(!items||items.length<3)return false;
  var vals=[],i;
  for(i=0;i<items.length;i++){
    var v=parseChoiceNumber(items[i].text);
    if(v===null||isNaN(v))return false;
    vals.push(v);
  }
  for(i=1;i<vals.length;i++){if(!(vals[i]>vals[i-1]))return false;}
  return true;
}
```

and inside `randomizeQuestionChoices()`:

```js
var orderedSeries=isOrderedNumericSeries(realChoices);
var shuffledChoices=(orderedSeries?realChoices.slice():shuffle(realChoices)).concat(blankChoices);
```

**Why it is safe.** `shuffle()` was called from exactly one place, so this is a single chokepoint.
The guard requires ALL options to parse as numbers AND to be strictly ascending, so a set that is
merely number-ish is still shuffled — it cannot accidentally freeze a normal question into
alphabetical order. Minimum three options. Applied on a copy and tested there before touching the
live file, which was backed up first.

**Verified on the live patched file:**

| Check | Result |
|---|---|
| Q10, Q53, Q62, Q80, Q87 hold source order | 50 shuffles each — all ordered |
| Every other question still shuffles | all 436 move |
| Keyed answer follows its option | 2,205 trials, 0 failures |
| Wrong-answer explanations follow their option | 2,205 trials, 0 failures |
| Full session build | 441 questions, all LO chips intact |
| Console | only the pre-existing `assets/copy-generated-question-sets.png` 404 |

The detector was dry-run across all 441 questions before patching and matched exactly the five
intended items — no false positives.

---

## Hardest Exam — a separate final 100-question quiz (5 batches of 20)

**File:** `Hardest exam/Jeevs Edition - Hardest Exam.html` (built with `build_quiz.py`, then the LO
link is patched to `../OMK_2A_Heme_Summative_3_Objective_Review.html` because the file sits one folder
down). Style spec: the UWorld prompt in `Hardest exam/index.html` — with **stem images allowed** (Jeevs
overrode the text-only rule), pathology-weighted, "due to" openers, two-step asks, and every explanation
ending in an `Educational objective:` line. The `q()` helper in the batch modules asserts that line.

New figures are keyed `fig_hx_*` in `quiz-toolchain/figs/`, resized at `-Z 1000 -s formatOptions 75`.
The **Robbins atlas** (`/Users/jeeval/Board Study/figures/Robbins/`, `.png` + `.txt` caption) is the main
new pathology source. Its captions were wrong twice in batch H1 — `Red Blood Cell Disorders - a862…`
is captioned Howell-Jolly body but shows basophilic stippling (used as `fig_hx_stipple_wright`), and
`…3ee064…` is captioned target cells but is not convincingly so (dropped). View every image.

| Batch | Sections | Module | Status |
|---|---|---|---|
| H1 | §1–§14 (hematopoiesis → transfusion) | `questions_hardest01.py` / `lo_tags_hardest01.py` | built, 20 Qs |
| H2 | §15–§28 (pharmacology, infection, lab, benign WBC) | `questions_hardest02.py` / `lo_tags_hardest02.py` | appended, 20 Qs (file now 40 Qs, 58 figures, 11.8 MB) |
| H3 | §29–§35, §49, §50 (coagulation, thrombophilia, VTE, ITP, node) | `questions_hardest03.py` / `lo_tags_hardest03.py` | appended, 20 Qs (file now 60 Qs, 79 figures, 16.5 MB) |
| H4 | §36–§42, §51 (malignancy, peds leukemia) | `questions_hardest04.py` / `lo_tags_hardest04.py` | appended, 20 Qs (file now 80 Qs, 97 figures, 20.2 MB) |
| H5 | §43–§46, §48, §55–§57, §23, §54 (chemo pharmacology, lymphatics, spleen trauma, lab, prescribing) | `questions_hardest05.py` / `lo_tags_hardest05.py` | appended — all 83 objectives covered at 100 Qs |
| H6 | High-yield depth, driven by the review file's own Master High-Yield Checklist | `questions_hardest06.py` / `lo_tags_hardest06.py` | appended — 120 Qs, 119 figures, 23.3 MB |

After H2, 44 of 83 objectives are covered. Batch H2 added Robbins figures `fig_hx_cerebral_malaria`, `fig_hx_pml_histo`, `fig_hx_kaposi_histo` and `fig_hx_ich_gross`; a Robbins smear captioned *P. falciparum* (`Red Blood Cell Disorders - 9ce795…`) was rejected because the field shows enlarged infected cells more consistent with a non-falciparum species.

After H3, 57 of 83 objectives are covered. Still uncovered: 3, 6, 11, 15, 16, 17, 21, 30, 34, 37, 38, 39, 40, 41, 47, 54, 56, 57, 58, 59, 60, 64, 67, 78, 80, 82 — i.e. the malignancy block (H4) plus chemotherapy pharmacology, spleen trauma, lymphatics, prescribing and accuracy/precision (H5).

After H4, 73 of 83 objectives are covered. The last 10 for batch H5: 11, 15, 16, 17 (antineoplastic pharmacology), 34 and 60 (lymphatics), 47 (splenic trauma management), 59 (accuracy vs precision), 64 (chemotherapy principles) and 78 (prescription writing). Note the file is at 20.2 MB — run the figure re-encode sweep (`-Z 850 -s formatOptions 68`, keep only if smaller) if H5 pushes it past ~26 MB.

### Hardest Exam — final state

**100 questions · 110 figures · 21.7 MB · 83 of 83 objectives covered.** 39 questions carry a stem
image. Keyed answer is uniquely longest in 10.0% (chance is 20%), none by 5+ characters; all option
sets alphabetical; every explanation ends in an `Educational objective:` line; every question carries
an LO chip. Browser-verified at 100 questions: no console errors, all figures resolve, all lab blocks
render as native `lab-row` tables.

One engine change beyond the standard `build_quiz.py` patches: figure `<img>` tags now carry
`loading="lazy" decoding="async"`, added by string-patching the single `<img src="'+src+'"` builder in
the built file. It does not shrink the file (the images are inlined base64) but it stops the browser
decoding 110 figures at load. If the file ever needs to be smaller — the 30 MB delivery ceiling — re-run
the in-place re-encode sweep described above.

New figure keys added across H1–H5 are prefixed `fig_hx_*`. Sources: Robbins atlas
(`/Users/jeeval/Board Study/figures/Robbins/`, .png + .txt caption sidecar), AMBOSS, and the review
file's own `assets/` slides. Two Robbins captions were wrong and were caught only by viewing the
image — see the H2 note. Confirm every stem image by eye; the caption is not evidence.

### Batch H6 — how the high-yield top-up was chosen

Rather than picking topics by feel, H6 was built directly from the review file's own **Master
High-Yield Checklist** (section id `checklist`, 66 numbered cards). Each of the first 100 questions
was mapped onto the card it tests, and the 20 cards with no question were written up: 06 (folate
alone masks B12), 07 (thalassemia trait vs iron deficiency), 12 (TRICC), 13 (platelet thresholds
10/20/25), 14 (the 30% rule), 15 (TACO side of the TACO/TRALI pair), 16 (irradiation and TA-GVHD),
17 (white vs red clot), 22 (the two CD4 numbers), 24 (one mutation kills the NNRTI class), 27
(pseudothrombocytopenia), 28 (burr vs spur), 32 (maternal antibody and the timing of
immunodeficiency), 41 (anti-Xa, not aPTT, for LMWH), 47 (CD23 splits the CD5+ B cells), 48
(MGUS vs smoldering), 51 (left internal jugular line → chylothorax), 53 (which DOACs need a
lead-in), 56 (acetaminophen never NSAIDs in VHF) and 61 (fasting provokes porphyria, glucose
treats it).

That mapping is the reusable part: if the file is ever extended again, re-run it and write the
cards that come back uncovered.

**State after H6: 120 questions · 119 figures · 23.3 MB · 83/83 objectives.** Uniquely-longest keyed
answer 10.0% (chance 20%), none by 5+ characters. Title updated to "Final 120".
