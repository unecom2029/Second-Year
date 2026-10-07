# Week 15 quizzes — source

| Job | Question files | Builds | Images |
|---|---|---|---|
| `vs` | `q_vs_v1.py`, `q_vs_v2.py` | `Vascular_Disease_Quiz_V1.html`, `Vascular_Disease_Image_Quiz_V2.html` | V1 6, V2 all 18 |
| `wh` | `q_wh_v1.py`, `q_wh_v2.py` | `Cardiovascular_Health_in_Women_Quiz_V1/V2.html` | 2 / 1 |
| `er` | `q_er_v1.py`, `q_er_v2.py` | `Exercise_Rehabilitation_Quiz_V1/V2.html` | 3 / 2 |

Rebuild: `python3 build.py vs wh er write` (one file: `python3 build.py vs:q_vs_v2 write`; omit `write` to audit answer lengths).
Per-item length ranks: `python3 lens.py q_vs_v1`. Contact sheet of images: `python3 vsheet.py out.jpg Key1 Key2 …`.

`build.py`, `lens.py`, `vsheet.py` and the loader in `images.py` are copied from `Week 14/notes/Quiz/_source/`.
Images come from `../../assets/vasc-surg/` (lecture slides) and AMBOSS. **No UWorld images.**
Masked giveaways: "LA Thrombus" label (left atrial CT), "Arteries"/"Clot" labels (SMA CT), "Common Femoral Artery Occlusion"
label (angiogram), stray panel letters on the popliteal angiogram and post-thrombotic photo. Captions name the view, never the diagnosis.
V1 and V2 cover different angles; the app reshuffles choices at runtime.

Women and Exercise Rehab quizzes (Qazi, no recordings) are concept/number-based, so images are used only where a graph is the point
(menarche U-curve, preterm-delivery hazard curve, prevalence chart, stroke-volume curve with its axis label removed, BP response,
Blair fitness bars, PREDIMED, DASH-Sodium). Panel letters masked. A few items are tagged Board add-on in their explanations
(SCAD, Takotsubo, atypical MI symptoms, exercise hypotension, Karvonen formula).

## Rewrite (2026-10-02)
All six Week 15 quizzes were rewritten to Jeeval's NBME/NBOME item-writer spec: house-style stems (exact durations, vitals format,
explicit negatives that kill options, inventory lead-ins), one buried clue + one decoy per item, homogeneous option families with
4–7 options (ordered series, matched-set table rows, extended differentials, communication scripts, one chart-format item per
vascular quiz), and counterfactual wrong-answer explanations ("Would be correct if…"). Images kept (his instruction).
`build.py` now turns "\n" in a stem into <br> so chart and table stems render.
