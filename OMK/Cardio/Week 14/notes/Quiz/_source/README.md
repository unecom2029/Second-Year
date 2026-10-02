# Quiz sources — Cardio Week 14

These files generate the quiz HTML files in the folder above. Each quiz file is a copy of `../index.html` (the quiz builder, copied from Week 13) with the questions and images embedded, so the quizzes themselves don't need anything in here.

| Question file | Builds |
|---|---|
| `q_phys_v1.py` | `Cardiac_Physiology_Quiz_V1.html` (18 questions, 6 with images) |
| `q_phys_v2.py` | `Cardiac_Physiology_Quiz_V2.html` (18 questions, 6 with images) |
| `q_arr_v0.py` | `ECG_II_Arrhythmias_Concept_Quiz_V0.html` (15 easier concept questions, 4 ECGs) |
| `q_arr_v1.py` | `ECG_II_Arrhythmias_Quiz_V1.html` (18 questions, 6 ECGs) |
| `q_arr_v2.py` | `ECG_II_Arrhythmias_Image_Quiz_V2.html` (18 questions, every one an ECG, with no findings in the stem) |

- `images.py`: the image list. Each key maps to a source file, an optional crop, a credit, and optional white-out boxes (used to hide the diagnosis labels on the AMBOSS valve PV loops). Sources are `../../assets/physiology/` and `../../assets/ekg-2/`, the UWorld PV-loop figures in `~/Board Study/figures/Uworld images/`, and `ecglib/` (ECGs from ecglibrary.com, drawn onto that site's grid). Machine-read headers are cropped off the ECGs.
- `build.py`: turns a question file into a quiz HTML file. It sorts the answer options alphabetically, remaps the key and wrong-answer explanations to match, and prints an audit of answer lengths.

The question format is the same as Week 13's (see `Week 13/Notes/Quiz/_source/README.md`).

## Rebuild

```bash
cd "_source"
python3 build.py phys arr write
```

Leave off `write` to see only the length audit.

## Built 2026-10-01: V1 + V2 for the five newer Week 14 lectures (18 items each)

| Job | Question files | Builds | Images | Angle |
|---|---|---|---|---|
| `peds` | `q_peds_v1.py`, `q_peds_v2.py` | `Pediatric_Cardiology_Quiz_V1.html`, `Pediatric_Cardiology_Image_Quiz_V2.html` | V1 6, V2 all 18 | V1 murmurs, fetal circulation, syncope, KD, IE, HCM screening · V2 image diagnosis → next step |
| `aa` | `q_aa_v1.py`, `q_aa_v2.py` | `Antiarrhythmic_Pharmacology_Quiz_V1/V2.html` | 3 / 4 | V1 action potentials, rate vs rhythm, class I, class II · V2 class III, IV, adenosine, digoxin, atropine, hockey case |
| `hf` | `q_hf_v1.py`, `q_hf_v2.py` | `Heart_Failure_Pharmacology_Quiz_V1/V2.html` | 2 / 2 | V1 neurohumoral cycle, pillars, Frank–Starling, decompensation · V2 cases: loops, inotropes, nitrates/nitroprusside, regimen |
| `ihd` | `q_ihd_v1.py`, `q_ihd_v2.py` | `Ischemic_Heart_Disease_Pharmacology_Quiz_V1/V2.html` | 2 / 2 | V1 supply/demand, anginas, vasospastic case, nitrates · V2 stable case, β-blockers, CCBs, ranolazine, risk reduction |
| `lp` | `q_lp_v1.py`, `q_lp_v2.py` | `Dyslipidemia_Pharmacology_Quiz_V1/V2.html` | 2 / 3 | V1 secondary causes, statins, ezetimibe, sequestrants · V2 fibrates, fish oil, niacin, PCSK9, last HTN case |

Rebuild: `python3 build.py peds aa hf ihd lp write` (one file: `python3 build.py aa:q_aa_v2 write`; omit `write` to audit).
Length check per item: `python3 lens.py q_aa_v2`. Final audit: key uniquely longest/shortest at or below chance in every file;
no UWorld paths (asserted). The quiz app reshuffles choices at runtime, so letter spread in the build doesn't matter much.

Rules for these: **no UWorld images** (Jeeval, 2026-10-01). Image keys added to `images.py` read lecture figures from
`../../assets/<lecture>/` (repo copies, not the temp deck dumps), plus AMBOSS, Robbins and `ecglib/`. `images.py`
supports coloured white-out boxes `(l,t,r,b,'black')` and an `UPSCALE` dict for small sources. Answer-revealing
labels were masked or cropped (VSD label on the echo, "Tet spell" text, "Initial" on the CXR, the BAV arrow, the
WPW machine read, the PSVT slide title, the Kawasaki caption, the A/B panel letters on the acetylcholine angiogram).
Credits must stay neutral: AMBOSS library-asset credits had the article name ("Amiodarone article") and leaked the
answer, so they now read just "AMBOSS". Not used: the HF Frank–Starling slide (labels give the answers, A–G letters
clash with choices), the AMBOSS complete-heart-block schematic, the arcus photo (ring not visible).
