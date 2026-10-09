# Quiz sources — Cardio Week 13

These files generate the quiz HTML files in the folder above. Each quiz file is a copy of `../index.html` (the quiz builder) with the questions and images embedded, so the quizzes themselves don't need anything in here.

## Files

| Question file | Builds |
|---|---|
| `q_cardiac.py` / `q1_cardiac.py` | Cardiac Pathology V2 / V1 |
| `q_endo.py` / `q1_endo.py` | Endocarditis, Myocarditis & Pericarditis V2 / V1 |
| `q_ecg_v0.py` / `q_ecg_v1.py` / `q_ecg_v2.py` | ECG Basics V0 / V1 / V2 |
| `q_htn_v1.py` / `q_htn_v2.py` | Hypertension Pharmacology V1 / V2 |
| `q_bsr_v1.py` / `q_bsr_v2.py` | CV Pharm Basic Sciences Review V1 / V2 |
| `q_vasc_v1.py` / `q_vasc_v2.py` | Vascular Pathology V1 (6 images) / Image Quiz V2 (all 18) |

- `images.py`: the image list. Each key maps to a source file, an optional crop, and a credit. Sources are the notes' `assets/`, `~/Board Study/figures/` (Robbins, AMBOSS, UWorld), and `ecglib/` (ECGs downloaded from ecglibrary.com, drawn onto that site's grid).
- `build.py`: turns a question file into a quiz HTML file. It sorts the answer options alphabetically, remaps the key and wrong-answer explanations to match, and prints an audit of answer lengths.

## Question format

```python
dict(img='Lchb',                 # key in images.py, or None for a text-only question
     cap='12-lead ECG',          # figure caption (never name the diagnosis)
     stem="... {FIG}Lead-in?",   # {FIG} marks where the image goes
     choices=[...], key=0,       # key = index of the correct choice
     exp="...",                  # explanation (HTML allowed)
     wrong={1:"...", 2:"..."},   # one explanation per wrong choice, by index
     eli5="...")
```

## Rebuild

```bash
cd "_source"
python3 build.py v1 v2 ecg ecg0 pharm vasc write
```

Leave off `write` to see only the length audit. Job names: `v2` (Cardiac + Endo V2), `v1` (Cardiac + Endo V1), `ecg` (ECG V1 + V2), `ecg0` (ECG V0), `pharm` (all four pharm quizzes), `vasc` (Vascular Pathology V1 + V2).

## Vascular Pathology (2026-10-08)
V1 and V2, 18 items each, written to the NBME/NBOME spec in `../index.html`. Images are keys `V*` in `images.py`: lecture slides in `../../assets/vascular/`,
Robbins atlas (`Blood Vessels - *`) and AMBOSS. `images.py` now supports white-out boxes and upscaling (same loader as Weeks 14–15), and `build.py`
turns "\n" in a stem into a line break for the table and chart-format items. **Masked or cropped giveaways:** panel letters on the hyaline arteriolosclerosis,
Takayasu, plaque-rupture and angiosarcoma slides; the "P-ANCA" label on the immunofluorescence image; the lecture caption under the hyaline panel.
Captions name the view, never the diagnosis. `lens.py` (from Week 15) prints per-item length ranks. Hub links are restricted to jmehta@une.edu.
