# Week 14 notes — build method and state (handoff)

Written so a fresh session can resume without re-reading the sources. Update as each file lands.

## Request (2026-10-01)
Jeeval: build study notes for several Scully pharmacology lectures, following
`Quiz, anki, notes instruction /OMK_2_notes.md` and the existing Week 14 notes. **No UWorld images.**
Output: `OMK/Cardio/Week 14/notes/` (same folder as ECG II / Peds Cardiology notes).

## The four lectures → four notes files
| # | Output file | Deck (Downloads) | Transcript (Downloads) |
|---|---|---|---|
| 1 | `Antiarrhythmic_Pharmacology_Study_Notes.html` | `CARDIO_Rhythm.pptx` (43 slides, 30 imgs, slides 10–14 hidden physiology) | `Pharmacology - HF an-transcript.txt` — FIRST half (antiarrhythmics, ends at "let's take 5") |
| 2 | `Heart_Failure_Pharmacology_Study_Notes.html` | `CARDIO_Heartfailure_2026_Upload.pptx` (22 slides) | same transcript — SECOND half (HF + 4 cases) |
| 3 | `Ischemic_Heart_Disease_Pharmacology_Study_Notes.html` | `CARDIO_Ischemic Heart Disease_Upload.pptx` (15 slides) | `CARDIO_Angina_2026.m-transcript.txt` (recorded video) |
| 4 | `Dyslipidemia_Pharmacology_Study_Notes.html` | `CARDIO_LipidUpload.pptx` (11 slides) | `CARDIO_Lipids_2026.m-transcript.txt` (recorded video; ends with a revisit of the last HTN case) |

Lecturer for all four: **Kyle R. Scully, PhD** (Pharmacology). The "Upload" decks are student
versions: case slides without answers. The transcripts carry the answers — they are the primary source.

## Sources and tiers
- Primary: transcript + slides. Lecture emphasis → `strong.hot`.
- Board add-ons (tag `<span class="src-tag">Board add-on</span>`): AMBOSS library article text in
  `~/Board Study/build/text/amblib.json` (indices: 71 Antiarrhythmic drugs, 53 Amiodarone, 120 Beta blockers,
  141 CCBs, 150 Cardiac glycosides, 260 Diuretics, 379 Heart failure, 17 Acute HF, 587 Nitrates, 814 Statins,
  768 Second-line lipid-lowering agents, 501 Lipid disorders, 214 CAD, 835 Sympathomimetics, 833 SVT, 509 LQTS).
  Dumped to scratchpad `pharm/amb/*.txt`.
- Figures: lecture slide images + AMBOSS (`~/Board Study/figures/amboss/*.png` and
  `figures/Text/AMBOSS Library Data/assets/asset-N.jpg`) + CV Pathophysiology book. **Never UWorld.**
- Cross-links: Week 13 `Hypertension_Pharmacology_Study_Notes.html` (diuretics/CCB/RAAS in depth),
  `CV_Pharm_Basic_Sciences_Review_Study_Notes.html`, Week 14 `ECG_II_Clinical_Arrhythmias_Study_Notes.html`,
  `Cardiac_Physiology_Review_Study_Notes.html`.

## Build pipeline (scratchpad `.../scratchpad/pharm/`)
Same as the Peds Cardiology build (`scratchpad/peds/build.py`): shell (CSS, theme, study-tools JS,
auth gate) is copied from `ECG_II_Clinical_Arrhythmias_Study_Notes.html`; body files use placeholders
`[[F key|cls]]`, `[[ROW k1 k2:sm]]`, `[[V id|title|channel;;...]]`; figures resized ≤1400 px into
`assets/<lecture>/`, numbered per file; README table appended to `assets/README.md`.

## Conventions
Spell out abbreviations per section (abbr-strip) + glossary; drug cards with MOA / Indications /
AEs / CI-DDI lines; ≥2 exam Qs per section; HY one-pager per file (verify 1 page in headless Chrome
with the auth gate forced open: replace `hasValidNoteAuth()?'unlocked':'locked'` → `'unlocked'`);
drill options balanced in length; Study Hub `index.html` Week 14 gets one entry per file.

## Status
- [x] 1 Antiarrhythmics — built (31 figs, 25 exam Qs, 10 videos, 14 sections). Source files: scratchpad `pharm/aa/`
  (`shell.html` = toc + `<!--HERO-->` hero + `<!--FOOTER-->` footer; `body1-4.html`; `hy.html`). Rebuild: `python3 build.py AA`.
- [x] 2 Heart failure — built (16 figs, 20 exam Qs, 7 videos, 12 sections). Source `pharm/hf/`. Rebuild `python3 build.py HF`.
- [x] 3 Ischemic heart disease — built (14 figs, 13 exam Qs, 6 videos, 10 sections; inline SVG for ranolazine). Source `pharm/ihd/`.
- [x] 4 Dyslipidemia — built (13 figs, 16 exam Qs, 6 videos, 9 sections; includes the HTN-case revisit). Source `pharm/lipid/`.
- [x] README tables appended (assets/README.md) · [x] Study Hub `index.html` Week 14 entries (4) — inline script parses
- [x] Verified 2026-10-01: all images load, tools + drills work, no console errors, no overflow at 390 px;
  headless print: every HY one-pager = 1 page; full notes AA 44 / HF 31 / IHD 22 / LP 24 pages.
  Drill answer-length audit (52 items): key uniquely longest 21%, shortest 15% (chance ≈ 25%).
- Fixed during verification: IHD plan tool suggested a β-blocker for vasospasm + PDE5 case; ranolazine SVG capped at 760 px.
- Not committed (Jeeval commits himself).

## Content decisions already made (don't re-derive)
- Lecture slips flagged in the notes: HF transcript said "beta-intercalated cells" swap K⁺ for H⁺ → it is α-intercalated;
  lipid transcript said DCT reabsorbs "25–30%" of filtered Na⁺ → ~5–10% (TAL ~25%).
- HF case 5 (68-year-old Black woman, slide 22) was NOT discussed in the recording (time ran out) → answer written as a
  worked synthesis, labelled as such; note the lecturer's point that race-based RAAS avoidance was debunked.
- Lipids: oral PCSK9 inhibitor transcribed "elicitide" = enlicitide; "inclysorin" = inclisiran (siRNA).
- Antiarrhythmic hidden slides 10–14 (physiology) are included briefly; intrinsic rates filled in as Board add-on.

## Quizzes (2026-10-01)
V1 + V2 quizzes (18 items each) for Peds Cardiology and all four pharm lectures are built in `notes/Quiz/`.
Sources, build commands and image rules are in `notes/Quiz/_source/README.md`. No UWorld images. Not linked from the
Study Hub (the earlier Week 14 quizzes aren't either).
