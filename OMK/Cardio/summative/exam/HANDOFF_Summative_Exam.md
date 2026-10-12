# HANDOFF — Cardio Summative Review Exam

> For any Claude session picking this up. **Read this whole file before writing or building anything.**
> Started 2026-10-09. Update §6 (status) and §7 (log) every time a batch of questions lands, before starting the next one.

## 1. What Jeeval asked for

- A **summative review exam** for OMK 2A Cardio that covers **Parts A–H plus Section 37** of the review page
  (`../OMK_2A_Cardio_Summative_Objective_Review.html`), with "every freaking possible question" and **no loss of quality**.
- **Images in the stems** — yes. Sources: `~/Board Study/figures/` (amboss/, Robbins/, …) and `../assets/` (lecture + AMBOSS copies),
  plus the Week 13–17 `notes/assets/` folders. **Never UWorld images.**
- **Follow the JSON spec inside the quiz builder's prompt (`buildPrompt()` in `index.html`) except for the question count** — no cap.
- Built from `quizbuilder/Unmodified Index/index.html`, copied untouched to `exam/index.html`.
- **One Part at a time.** Part A first; show Jeeval, wait for "keep going" before the next Part (his standing rule for big builds).

## 2. Files

| Path (from `summative/exam/`) | What |
|---|---|
| `index.html` | Untouched copy of the quiz builder. `build.py` reads it as the template. Never edit it. |
| `_source/images.py` | Image registry: path, crop, neutral credit, white-out masks, numbered labels, upscaling. |
| `_source/build.py` | Turns question modules into `Cardio_Summative_Exam_Part_<X>.html` (preloaded, NBME UI mode). |
| `_source/q_<Part><n>_<topic>.py` | Question modules. Each defines `Q = [dict(...)]`; field list is in `build.py`'s docstring. |
| `_source/vsheet.py` | `python3 vsheet.py out.jpg key1 key2 …` renders processed images (masks applied) to check them. |
| `_source/lens.py` | `python3 lens.py q_A1_cycle` — per-item answer-length rank, flags key uniquely longest/shortest. |
| `Cardio_Summative_Exam_Part_<X>.html` | The deliverables. One file per Part (data-URI images make one giant file impractical). |

Build: `cd _source && python3 build.py A write` (omit `write` to audit only; `all` builds every Part).

## 3. Item-writing rules (from the builder's prompt + Jeeval's standing feedback)

- NBME house style: opening line with age/sex/setting/exact duration; vitals in house format; clipped exam; explicit negatives that
  each kill a listed option; one buried clue + a separate dramatic decoy; cover-the-options test; lead-in from the inventory.
- No teaching or diagnosis labels in the stem ("classic for", naming the disease), no negative lead-ins, no "all/none of the above".
- Homogeneous option family; **4–8 options, varied** (ordered series, matched-set table rows, extended differentials).
  `build.py` sorts options alphabetically (lists whose options all start with a digit keep their written order) and remaps the key.
- Mix shapes: full vignettes (most), compact vignettes, investigator items, computation sets with named-error distractors,
  matched-set tables (a small HTML table in the stem; each option is one row), a chart-format item now and then.
- `wrong` explanations: say why that option is wrong for this patient and, where natural, what would have made it right —
  **not** a forced "Would be correct if…" every time (Jeeval's 2026-10-08 feedback on the NBME bank).
- `exp` may use arrows (the builder's JSON spec asks for them); end with `<b>Educational objective:</b> …`.
- **Spell out abbreviations** in stems, options and explanations (first use per item).
- **Balance answer lengths**: key uniquely longest and uniquely shortest each at or below chance across the file; don't overcorrect.
  Check with `build.py` (totals) and `lens.py` (per item).
- Lecture content leads; board add-ons (AMBOSS/UWorld text, First Aid) are fine for distractor logic and explanations.
  Where the lecture and the boards disagree (see the review page's warning boxes), test the version both agree on, or say which
  source the item follows in the explanation.

## 4. Image rules

- Captions say what the view is plus the source credit, **never the diagnosis**; credits are neutral ("AMBOSS", "Qazi lecture").
- Mask any burned-in label that names the answer (titles such as "Mitral Valve Stenosis", "Tall v-wave", "OS", "Mid-systolic click").
- Letters on figures clash with answer letters → replace with numbers (`labels=` in `images.py`); options then read "Point 1"… / "Loop 1"….
- Check every processed image with `vsheet.py` before using it. Mask coordinates are fractions of the ORIGINAL image.
- `masks` colour `'auto'` = lightest corner pixel inside the box (keeps the background shade).

## 5. Part A blueprint (Sections 1–5; objectives 1–9 and 72)

| Module | Topic | Planned testing points |
|---|---|---|
| `q_A1_cycle` | §1 cycle, Wiggers, PV loops, muscle | valve events on Wiggers (numbered); JVP waves in AF; dP/dt in isovolumetric contraction; tachycardia + mitral stenosis; SV/EF/CO computation; afterload/preload/contractility/compliance on the loop; first 10 s of MI; excitation–contraction coupling (L-type → RyR2); sliding filaments; length–tension; Starling matching RV and LV; MR loop recognition |
| `q_A2_sounds` | §2 heart sounds | S3 vs S4 mechanism and timing; S3 in pregnancy/young; S4 lost in AF; four S2 splits (AMBOSS diagrams); opening-snap interval and severity; ejection click (bicuspid); soft S2/loud P2 |
| `q_A3_murmurs` | §3 lesions | MS/AS/MR/AR tracings and schematics (masked); concentric vs eccentric; LA pressure in AS; AS symptoms, preload dependence, Heyde; bicuspid vs calcific by age; MR primary vs functional; MVP pathology; AR wide pulse pressure, Austin Flint, hyperdynamic signs; acute vs chronic regurgitation |
| `q_A4_maneuvers` | §3 location, maneuvers, innocent, rheumatic | auscultation sites (numbered); radiation; Valsalva/standing/squat/handgrip/leg raise/inspiration; HCM vs AS; TR on inspiration; Valsalva physiology; Still murmur/venous hum; diastolic murmur → echo; rheumatic fever mimicry, Aschoff body, fish-mouth valve |
| `q_A5_exercise` | §4 | HR/SV/BP/VO₂ responses; SV plateau; Fick; Karvonen and ischemic-threshold targets; exercise SBP fall; protective mechanisms; METs and mortality; rehab phases, indications, timing, Medicare; underuse; FITT; diets (PREDIMED, DASH-sodium, trans fat, sodium targets); 150/75 minutes |
| `q_A6_control` | §5 | receptor/G-protein grid; β1 and renin; phenylephrine reflex; NE with M2 block; NE/Epi/Iso graph; PDE3 and cAMP; nodal vs myocyte ions; vagal mechanism (trace figure); refractory periods; conduction velocities; Poiseuille; continuity; series/parallel; MSFP and venous return; Guyton shifts; HF paradox and dilutional hyponatremia; Bainbridge; baroreceptor nerves; renin/ADH directions |

## 6. Status

| Part | Sections | State | Items |
|---|---|---|---|
| A | 1–5 | **Built 2026-10-09 — waiting for Jeeval's review** → `Cardio_Summative_Exam_Part_A.html` (2.6 MB) | 92 (31 with images) |
| B | 6–10 | **Built 2026-10-09 — waiting for Jeeval's review** → `Cardio_Summative_Exam_Part_B.html` (8.8 MB) | 107 (47 with images) |
| C | 11–16 | **Built 2026-10-09 — waiting for Jeeval's review** → `Cardio_Summative_Exam_Part_C.html` (5.4 MB) | 105 (30 with images) |
| D | 17–20 | **Built 2026-10-09 — waiting for Jeeval's review** → `Cardio_Summative_Exam_Part_D.html` (3.0 MB) | 83 (17 with images) |
| E | 21–23 | **Built 2026-10-09 — waiting for Jeeval's review** → `Cardio_Summative_Exam_Part_E.html` (4.1 MB) | 69 (22 with images) |
| F | 24–25 | **Built 2026-10-09 — waiting for Jeeval's review** → `Cardio_Summative_Exam_Part_F.html` (1.5 MB) | 46 (9 with images) |
| G | 26–27 | **Built 2026-10-10 — waiting for Jeeval's review** → `Cardio_Summative_Exam_Part_G.html` (2.2 MB) | 38 (12 with images) |
| H | 28–36 | **Built 2026-10-10 — waiting for Jeeval's review** → `Cardio_Summative_Exam_Part_H.html` (4.4 MB) | 102 (29 with images) |
| §37 | 37 | **Built 2026-10-10 — folded into Part H's file** (`q_H9_women`) | 5 |

## 7. Log

**2026-10-09 — setup**
- Copied `quizbuilder/Unmodified Index/index.html` → `exam/index.html` (byte-identical).
- Wrote `images.py` (masks, numbered labels, 'auto' background colour), `build.py` (multi-module Parts, structural checks,
  UWorld-path assertion, length audit), `vsheet.py`, `lens.py`.
- Checked and masked Part A figures: Wiggers with valve events numbered 1–4 (1 mitral closure, 2 aortic opening, 3 aortic
  closure/dicrotic notch, 4 mitral opening); AMBOSS PV cycle (points 1–4 already numbered: 1 mitral closure, 2 aortic opening,
  3 aortic closure, 4 mitral opening); AMBOSS AS/MR loop legends removed; systolic/diastolic loops relabelled 1 = diastolic
  dysfunction (blue), 2 = normal (green), 3 = systolic dysfunction (yellow); Qazi MS/AS/MR/AR tracings and schematics with
  titles and answer labels masked; phonocardiogram labels ("OS", "Mid-systolic click", "Ejection click") masked (tiny arrow
  tips remain on MVP/AS — harmless); auscultation sites A–G → 1–7 (1 suprasternal, 2 right 2nd intercostal space, 3 left 2nd,
  4 left sternal border, 5 tricuspid area, 6 mitral area (apex), 7 axilla — confirmed from the AMBOSS caption);
  NE/Epi/Iso graph drug names → Drug 1/2/3 (1 norepinephrine, 2 epinephrine, 3 isoproterenol); autonomic pacemaker traces →
  1 gray = rest, 2 green = sympathetic, 3 blue = parasympathetic.
- Review page fix found while planning: §3 said handgrip separates hypertrophic cardiomyopathy from aortic stenosis; it softens
  both. Now says standing/Valsalva (or location). Reinjected.

**2026-10-09 — Part A written and built (92 items, 31 with images)**

| Module | Items | Images | What it covers |
|---|---|---|---|
| `q_A1_cycle` | 15 | 6 | Wiggers numbered valve events (opening snap = point 4), JVP a wave lost in AF, dP/dt in isovolumetric contraction, tachycardia in pregnant mitral stenosis, SV/EF/CO computation, afterload rows, ejection click on the PV loop (point 2), dobutamine and ESPVR, diastolic-dysfunction loop, first 10 s of MI, verapamil and calcium-induced calcium release, sliding filaments (EM), length–tension, Frank–Starling matching in a transplant, MR loop |
| `q_A2_sounds` | 11 | 4 | S4 mechanism, S4 after the P wave, S3 in alcoholic DCM, S3 + flow murmur in pregnancy (reassure), fixed split = ASD, paradoxical split = delayed A2 in AS, wide split → RBBB ECG, physiologic split mechanism, S2–OS interval and severity, soft A2 in severe AS, ejection click → image the aorta |
| `q_A3_murmurs` | 16 | 7 | MS/AS/MR tracings (masked), AR and AS schematics (diastolic runoff; LA pressure from stiff LV), eccentric vs concentric rows, MS → AF → LA thrombus stroke, bicuspid vs calcific by age, nitroglycerin in AS (preload), Heyde, ischemic MR tethering, MVP myxomatous histology (phono), acute MR soft murmur, Austin Flint, Quincke/de Musset, AR loop |
| `q_A4_maneuvers` | 13 | 7 | auscultation sites (MR at 6, HCM at 4), HCM standing/handgrip rows, MVP click later with squatting, TR louder on inspiration → v waves, Valsalva strain rows, MS bell/left lateral, Still murmur, venous hum, diastolic murmur → echo, rheumatic mimicry, Aschoff → MS, fish-mouth valve → group A strep |
| `q_A5_exercise` | 17 | 4 | flat DBP (arteriolar dilation), SV plateau → HR, Fick, Karvonen target, ischemic threshold −10, exercise SBP fall, HDL rise, shear stress → NO, endurance AF, 0.87 per MET compounding, phase II rehab, Medicare HF EF ≤35%, physician endorsement, PREDIMED, DASH-sodium additive, 150/75 minutes, Guyton in exercise |
| `q_A6_control` | 20 | 3 | M2/Gi receptor, β1 renin, phenylephrine reflex via M2, NE + M2 block rows, NE/Epi/Iso graph (drug 3 = isoproterenol), nitrate + sildenafil cGMP, verapamil PR not QRS, vagal trace 3, relative refractory period, AV node slowest, transplant HR 100, Poiseuille 1/16, parallel resistance, capillary velocity, hemorrhage on the vascular curve, HF dilutional hyponatremia, Bainbridge/atrial receptors, carotid sinus CN IX, furosemide ↑ renin, NE reuptake |

- Option counts: 4 ×19, 5 ×61, 6 ×11, 7 ×1. Answer-length audit after rebalancing: key uniquely longest 0, uniquely shortest 1 (chance ≈ 12.5 each).
- Browser check (port 8805, `cardio-summative-static`): 92 questions load, all 31 data-URI images decode, answering Q1 shows the explanation and wrong-answer notes correctly mapped after the app's runtime shuffle.
- Not yet covered in Part A (candidates if Jeeval wants more): ACE = kininase II (cough) is left for Part H; pericardial rub and tumor plop are left for Parts E and D; the c-wave timing disagreement is avoided rather than tested.
- **Next:** wait for Jeeval's review of Part A. Then Part B (§6–§10: ECG, arrhythmias, AF, antiarrhythmics) — ECG images from `../assets` (k-, r-, aa- prefixes) and Week 13/14 `ecglib` (no machine reads; crop headers).

**2026-10-09 — Part B started** (Jeeval: "keep the quality up"; "maybe we should make a new HTML" → yes, `Cardio_Summative_Exam_Part_B.html`)
- ECG image sources added to `images.py` (keys prefixed `B_`): Week 13 lecture ECGs (`E1`, k-*), Week 14 ECG II cases (`E2`, r-*),
  ecglibrary.com GIFs copied into `_source/ecglib/` (composited on its grid by `_ongrid`), and `~/Board Study/figures/Cardio/Cardiovascular pathophys/` (`CP`).
  Machine reads/headers cropped: k-1avb, k-sinus-arrhythmia, k-rvh, k-case-8 (WPW, "ABNORMAL ECG"), r-case-flutter, r-case-wpw-af,
  img_vtavd2 ("SUPRAVENTRICULAR TACHYCARDIA" read), img_wpw (patient name + "WOLFF-PARKINSON-WHITE"), img_trifas2. r-adenosine-flutter:
  printed "SV TACHY RHYTHM" lines masked, handwriting kept. aa-class1-abc relabelled Drug 1 = IA, Drug 2 = IB, Drug 3 = IC.
- Planned B3 (§8 ~24), B4 (§9 ~12), B5 (§10 ~25).

**2026-10-09 — Part B written and built (107 items, 47 with images)**

| Module | Items | Images | What it covers |
|---|---|---|---|
| `q_B1_basics` | 14 | 7 | rate ×6 / ×10 / 1,500 ÷ boxes, sinus criteria (upright P in II), sinus arrhythmia, MAT vs WAP, LAFB (left axis, narrow QRS), RBBB + LPFB, RVH (tall R V1), PR 240 ms, Bazett 500 ms (named errors), artifact, flutter 4:1 → atrial 300, sinus tach in asthma (treat cause, no β-blocker) |
| `q_B2_patterns` | 22 | 17 | RAE (P pulmonale) and LAE mechanism, LVH most specific (aVL > 11), LVH strain vs ischemia, LBBB, RBBB → wide split S2, trifascicular syncope → pacing, delta wave mechanism, congenital LQTS → EADs, dofetilide + ondansetron → torsades, hyperK image and earliest sign, hypoK U waves → torsades, inferior STEMI → RCA, anterior STEMI → PCI, posterior MI mirror, NSTEMI = subendocardial, old inferior Q waves, hyperacute T vs hyperK, pericarditis, early repolarization (Ito), inferior STEMI + CHB → RCA/AV nodal artery |
| `q_B3_arrhythmias` | 28 | 14 | re-entry initiation, digoxin DADs, Wenckebach site (node), Mobitz II → pacemaker, 2:1 block in elderly syncope, CHB, AF + CHB (regularized AF), AVNRT hidden P, adenosine dose/technique, adenosine in transplant, adenosine unmasks flutter, CTI ablation (AF later), carotid massage contraindications, unstable → synchronized cardioversion, negative concordance, capture beat, scar re-entry VT, avoid verapamil in WCT, Brugada algorithm step 2, pre-excited AF → procainamide, orthodromic AVRT circuit table, Ebstein–WPW, torsades → magnesium, Brugada syndrome (Na channel), ARVC fibro-fatty, HCM top athlete SCD, VF → defibrillation, syncope → 12-lead ECG first |
| `q_B4_afib` | 13 | 3 | recognition, fatigue/dyspnea > palpitations, paroxysmal vs persistent, CHA₂DS₂-VASc = 4 (named errors), flutter anticoagulated like AF, holiday heart score 0, thyrotoxic AF → propranolol, rhythm control in HFrEF, pulmonary vein isolation in the young, >48 h/unknown → TEE or 3 weeks anticoagulation, AF in a stiff ventricle (kick + filling time), wearable alerts need confirmation, AF with old LBBB vs pre-excited AF |
| `q_B5_antiarrhythmics` | 30 | 6 | class I subtypes (AP figure, Drug 1 = IA), lidocaine use-dependence, IC contraindicated after MI (CAST), flecainide 1:1 flutter → add nodal blocker, cinchonism, digoxin-raising drugs (procainamide doesn't), procainamide lupus (butterfly image), disopyramide anticholinergic, lidocaine CNS toxicity in cirrhosis, sotalol to avoid in LQTS, labetalol in pregnancy (α1), esmolol, propranolol bronchospasm (β2), masked hypoglycemia, dofetilide (renal, HFrEF OK, in-hospital), ibutilide, sotalol AP rows, amiodarone lung/thyroid/liver monitoring (CXR), corneal deposits (photo), amiodarone–warfarin CYP, IV verapamil + β-blocker → EMD, verapamil raises digoxin (renal), adenosine mechanism (A1/Gi, K⁺, bronchospasm), theophylline blocks adenosine, digoxin mechanism chain, digoxin + furosemide → check K⁺, digitalis ECG, acute digoxin OD hyperK → Fab, atropine first for symptomatic brady, anticholinergic toxidrome → physostigmine |

- Option counts: 4 ×11, 5 ×87, 6 ×8, 7 ×1. Length audit: key uniquely longest 0, uniquely shortest 0 (chance ≈ 13.6 each).
- **Quality rule learned this Part:** do not describe the tracing in the stem of an image item (it reads the ECG for the student). 18 stems trimmed to "His/Her electrocardiogram is shown." Keep only clinical facts and data the image cannot show (old tracings, QRS duration when it must exclude something, lab values).
- Browser check: 107 questions, all 47 images decode; Q42 (complete heart block) screenshot shows the ecglib tracing rendering cleanly on its grid.
- **Next:** wait for Jeeval's review. Then Part C (§11–§16: atherosclerosis, IHD/ACS, biomarkers, MI pathology, MI complications, IHD pharmacology).

**2026-10-09 — Part C written and built (105 items, 30 with images)** (Jeeval: "keep going - im proud")
- Image keys prefixed `C_` in `images.py`. Masks/labels: `C_flow` (Gimbrone panels B/C → 1/2), `C_plaqueAnat` (right-hand labels removed; 1 = fibrous cap, 2 = necrotic core, 3 = media), `C_bio` (CV Pathophysiology biomarker curves; word labels removed with staircase masks along the rotated text; 1 = myoglobin, 2 = CK-MB, 3 = troponin), `C_ach` (A/B → 1/2), `C_vsrEcho` (header with "VSR" + patient name blacked out), Gardner histology panels (corner letters cropped).
- **Dropped** `v-fmd-beads` from the exam: the lecture labels it fibromuscular dysplasia, but the Robbins atlas caption describes a lower-extremity angiogram with polyarteritis-type beading. FMD is tested in text only.
- Registered but unused (spares): `C_hyalineAm`, `C_neutRb`, `C_scarAm`, `C_livedo`, `C_antStemi`.

| Module | Items | Images | What it covers |
|---|---|---|---|
| `q_C1_athero` | 16 | 7 | hyaline (diabetic kidney) vs hyperplastic (malignant HTN) arteriolosclerosis, Mönckeberg + falsely high ABI, in-stent restenosis (medial SMC → intima), laminar vs turbulent flow culture → branch points, fatty streak in a teenager, foam cell origin, PDGF, numbered plaque (cap collagen from medial SMC), atheroma is intimal (clefts), vulnerable plaque features, MMPs/IFN-γ, outward remodeling, abdominal aorta most involved, cholesterol emboli → livedo with pulses, FMD string of beads |
| `q_C2_ihd` | 18 | 2 | test choice (LVH strain → exercise echo; can't exercise → dobutamine echo), crescendo angina → aspirin + ambulance (no stress test, no office troponin), flow-reserve graph, type 2 MI in sepsis, NSTEMI ECG → partial thrombus, NSTE-ACS timing (shock < 2 h; GRACE > 140 < 24 h), STEMI with 3-h transfer → fibrinolysis in 30 min, pinpoint pain, diabetic woman epigastric → ECG, dissection before heparin → CTA, takotsubo, INOCA/microvascular, diabetic 3-vessel → CABG, optimal medical therapy (4 classes), unstable angina with flat hs-troponin, aVR elevation → left main |
| `q_C3_biomarkers` | 14 | 1 | numbered marker curves → CK-MB for re-infarction, early hs-troponin → repeat 1–3 h, marathon, CKD flat troponin, rhabdo (cardiac isoforms), PE (RV strain), myocarditis plateau, ARNI raises BNP (follow NT-proBNP), obesity → echo, age-specific NT-proBNP table, NT-proBNP renal clearance, BNP actions (matched set), COPD low BNP (NPV), constriction keeps BNP low |
| `q_C4_mipath` | 15 | 9 | wavy fibers (first day), neutrophils (1–3 d), macrophages → free-wall rupture day 5, granulation (10–14 d), trichrome scar → chronic IHD (diabetic, silent), contraction bands (Ca²⁺ on reperfusion), coagulative necrosis, transmural gross → complete occlusion/STEMI, circumferential subendocardial in shock, EM irreversibility, stunning, TTC stain, why days 3–7, mottled 3–5-day gross, old scar + fresh reperfused band |
| `q_C5_complications` | 16 | 5 | VSR echo → O₂ step-up, papillary rupture (PDA single supply, soft/absent murmur), hemopericardium → Beck triad/PEA, free-wall rupture risk (first MI, older woman), pseudoaneurysm → emergency surgery, true aneurysm → mural thrombus, RV infarct (inferior STEMI ECG, V4R) → fluids, septal MI → RBBB, early fibrinous pericarditis (image) vs Dressler, Dressler → aspirin + colchicine, LV apical thrombus stroke, VF in first hour, cardiogenic shock → revascularize, stent thrombosis after stopping clopidogrel, shock liver, timing matched set |
| `q_C6_pharm` | 26 | 3 | nitrate mechanism (venodilation), coronary steal (AMBOSS schematic), PDE5 + nitrate, patch tolerance (4 options), Monday headache, ALDH2 East Asian, sublingual = no first pass, beta-blocker first line (7 options), BB + nitrate complement, pindolol ISA, Prinzmetal ECG → amlodipine, BB worsens vasospasm (α), acetylcholine provocation (M3), cocaine → benzodiazepine, IR nifedipine reflex tachycardia, verapamil in HFrEF, nitrates in HOCM, ranolazine for low HR/BP, late Na⁺ → NCX, ranolazine + clarithromycin, ivabradine phosphenes, chewed aspirin / O₂ only if hypoxic, hold BB + NTG in inferior STEMI with brady/hypotension, stop clopidogrel 5 d before CABG, post-MI EF 35% → eplerenone, fibrinolysis absolute contraindication |

- Option counts: 4 ×2, 5 ×92, 6 ×10, 7 ×1. Length audit: key uniquely longest 0, uniquely shortest 0 (chance ≈ 15.6 each).
- Image-stem rule applied: stems no longer describe what the image shows (trimmed "pale yellow-tan full-thickness zone", "outlines preserved", "grey-white area", "tear through the wall").
- Browser check: 105 questions, all 30 images decode; Q44 (NT-proBNP table) renders and its explanation/wrong notes map correctly after the runtime shuffle; Q35 biomarker curves render clean.
- **Next:** wait for Jeeval's review. Then Part D (§17–§20: heart failure, HF pharmacology, cardiomyopathies, cardiac tumors).

**2026-10-09 — Part D written and built (83 items, 17 with images)** (Jeeval: "keep going por favor")
- Image keys prefixed `D_`. Masks/labels: `D_hfrefLoop` / `D_hfpefLoop` (Morganelli loops; "↓ Inotropy", "↓ ESPVR", "↑ EDPVR" removed, red loop labeled "Patient"), `D_neuro` (Golan neurohumoral chart, "Increased ATII" box → X), `D_boxcar` (Gardner c-lvh panel D only), Gardner/Robbins panel letters masked on HCM gross, disarray, myxoma gross/histo. All 17 registered D images are used.

| Module | Items | Images | What it covers |
|---|---|---|---|
| `q_D1_hf` | 25 | 8 | pressure vs volume overload (boxcar nuclei; parallel vs series), chronic AR eccentric, HFrEF loop → only inotropes restore ESPVR, HFpEF loop (EDV↓ SV↓ EF normal), titin N2B in HFpEF, S4 with concentric LVH echo, neurohumoral X = angiotensin II, natriuretic peptide resistance, orthopnea, heart-failure cells (Prussian blue), nutmeg liver zone 3, LHF commonest cause of RHF, AV-fistula high output, wet beriberi, wet-cold → ICU inotropes, warm-wet → IV furosemide (no new BB), cocaine + metoprolol unopposed α1, cardiogenic edema CXR, nephrotic edema, H₂FPEF = 5, NYHA III, ACC/AHA stage B, IV iron, JVP + 5 cm, HFimpEF |
| `q_D2_hfpharm` | 26 | 0 | mortality vs symptom drugs, neprilysin substrates, 36-h ACEi washout, ACEi + MRA hyperkalemia, spironolactone → eplerenone, carvedilol (α1) among the evidence-based 3 (7 options), SGLT2 TGF afferent constriction, Fournier, euglycemic DKA, SGLT2 in HFpEF, loop Ca/Mg loss, hypokalemic alkalosis (α-intercalated), metolazone sequential blockade, ethacrynic acid, H-ISDN add-on (A-HeFT, not replacement), hydralazine lupus, vericiguat, nitroprusside cyanide → hydroxocobalamin, milrinone on carvedilol, norepinephrine reflex brady (matched set), PKA/phospholamban, furosemide down the same Starling curve, ACEi cough → ARNI, RAAS fetal toxicity, rapid four-pillar start, tolvaptan |
| `q_D3_cm` | 22 | 6 | DCM gross (alcohol), doxorubicin vs trastuzumab, TTN, peripartum, hemochromatosis (Prussian blue) → phlebotomy, Chagas RBBB + megaesophagus, HCM gross → AD sarcomere, disarray slide, carrier screening through adolescence, ICD risk markers (syncope), HOCM → metoprolol, mavacamten, amyloid (Congo red) → low voltage, ATTR → tafamidis, ARVC section → desmosomes, Friedreich ataxia, infant of diabetic mother, Löffler, cardiac sarcoid heart block, 2nd cause of athlete SCD = coronary anomalies, EF by cardiomyopathy (matched), DCM EF ≤35% → ICD (not CRT, narrow QRS) |
| `q_D4_tumors` | 10 | 3 | myxoma gross → IL-6, myxoma histo, tumor plop/positional → pedunculated mass at fossa ovalis, stalk + septal cuff excision, Carney complex, rhabdomyoma + tuberous sclerosis CT, "most common" matched set, malignant effusion tamponade → pericardiocentesis, RCC up the IVC, papillary fibroelastoma |

- Option counts: 4 ×4, 5 ×73, 6 ×5, 7 ×1. Length audit: key uniquely longest 0, uniquely shortest 0 (chance ≈ 8.4 each).
- Browser check: 83 questions, all 17 images decode; Q7 (neurohumoral X) renders cleanly.
- **Next:** wait for Jeeval's review. Then Part E (§21–§23: infective endocarditis pathology, IE diagnosis and treatment, myocarditis and pericardial disease).

**2026-10-09 — Part E written and built (69 items, 22 with images)** (Jeeval: "keep going")
- Image keys prefixed `E_`. `E_prosth` cropped to the left (prosthetic ring) panel to drop the textbook caption. **Left out on purpose:** the lecture's `e-osler.jpg` (flat sole petechiae — looks like Janeway lesions, not Osler nodes) and AMBOSS "Osler nodes" (atypical); Osler nodes are tested in text only. `pc-effusion-echo` skipped (its labels give the answer). `E_mitralVeg` registered, unused.

| Module | Items | Images | What it covers |
|---|---|---|---|
| `q_E1_ie` | 23 | 7 | IDU tricuspid TTE → S. aureus (septic pulmonary emboli, no murmur), viridans dextran, NBTE in cancer (image), Libman–Sacks → antiphospholipid, prosthetic ring → S. epidermidis biofilm, biofilm SEM (slow growth, poor penetration), S. gallolyticus → colonoscopy, Enterococcus after TURP (6.5% NaCl), Coxiella phase I IgG > 1:800, Bartonella quintana (lice), culture-negative = prior antibiotics, Candida veg → surgery + line removal, perforated aortic cusps → acute AR, acute vs subacute organisms (matched), MVP now commonest predisposition, dialysis risk, mycotic aneurysm, immune-complex GN, splenic infarct, mitral commonest valve, device → remove whole system, HACEK → ceftriaxone, pathogenesis sequence |
| `q_E2_ie_dxrx` | 22 | 6 | splinters (embolic), Janeway (septic micro-abscess), Roth spots ↔ Osler nodes (immune), petechiae → 3 culture sets first, unstable → vanc + cefepime after cultures, negative TTE → TOE, TOE perforation = major, Duke possible (3 minor), Duke definite (1 major + 3 minor), PET on a >3-month TAVR = major, MSSA → nafcillin, rifampin never alone, viridans → ceftriaxone 4 wk, enterococcal synergy, enterococci resist cephalosporins, vancomycin infusion reaction, nafcillin AIN, ring abscess → heart block → surgery, >10 mm vegetation + embolus → surgery, dental prophylaxis (prosthetic valve only), tricuspid repair first, rheumatoid factor |
| `q_E3_myoperi` | 24 | 9 | lymphocytic myocarditis biopsy → parvovirus B19, CAR (adenovirus), no sport 3–6 months, diphtheria EF-2, Lyme CHB ECG → IV ceftriaxone, Chagas amastigotes → triatomine feces, giant cell myocarditis, checkpoint-inhibitor myocarditis, mRNA vaccine myocarditis, pericarditis ECG → NSAID + colchicine, pericarditis vs STEMI features, phrenic → trapezius, 2 of 4 criteria, myo- vs perimyocarditis, colchicine mechanism, ECG stage 3, TB pericarditis (Langhans) → constriction, fluid types, uremic fibrinous → dialysis, electrical alternans → pulsus paradoxus, interdependence mechanism, water-bottle heart (rate > volume), post-pericardiotomy syndrome, calcified pericardium → pericardiectomy |

- Option counts: 4 ×5, 5 ×63, 6 ×1. Length audit: key uniquely longest 0, uniquely shortest 0 (chance ≈ 9.7 each).
- Browser check: 69 questions, all 22 images decode; Q24 (splinter hemorrhage) renders cleanly.
- **Next:** wait for Jeeval's review. Then Part F (§24–§25: valvular disease, aortic valve replacement / cardiac surgery).

**2026-10-09 — Part F written and built (46 items, 9 with images)** (Jeeval: "keep going")
- Smaller by design: the murmurs, maneuvers, rheumatic mimicry, fish-mouth valve and Aschoff body for these lesions were already tested in Part A (q_A3/q_A4), so Part F tests pathology, causes, management and prostheses.
- Image keys prefixed `F_`. `F_valvePlane` (McGrath valve-plane drawing; valve names → 1 tricuspid, 2 mitral, 3 aortic, 4 pulmonary), `F_ossif` (CV Pathophysiology calcific valve with bone; panel letter masked). Dropped `s-cpb` (labeled bypass diagram).
- One negative lead-in caught and reworded (acute AR: "which would worsen the regurgitation" → balloon pump); esmolol option replaced by nitroprusside to avoid ambiguity.

| Module | Items | Images | What it covers |
|---|---|---|---|
| `q_F1_valves` | 25 | 3 | numbered valve plane (aortomitral continuity), bicuspid → CT aorta, calcific AS bone (no drug slows it), AS angina mechanism, symptomatic AS prognosis, Heyde (angiodysplasia image, vWF multimers), syphilitic aortitis, AR surgical triggers (EF < 50, LVESD > 55), acute AR → balloon pump worsens it, MS in pregnancy → metoprolol, rheumatic MS + AF → warfarin, TEE before balloon commissurotomy, MVP myxomatous spongiosa, repair degenerative vs replace functional MR, rheumatic TS → mitral too, functional TR, carcinoid (lung MAO), Noonan PS → balloon, PR after TOF → PVR, nitroglycerin in AS, secondary rheumatic prophylaxis, acute carditis = MR, Ortner syndrome, McGrath's upstream cascade, tricuspid tissue valve |
| `q_F2_avr` | 21 | 6 | severe AS echo criteria (table), asymptomatic EF 42% → AVR, cath before SAVR, frail → transfemoral TAVR, pure AR Marfan (no anchor), young → SAVR (durability), bileaflet → warfarin + heparin bridge, mitral mechanical INR 3.0, bioprosthesis for planned pregnancy, 72-year-old with bleed → tissue, post-TAVR heart block (His bundle), left main obstruction at deployment, schistocytes → paravalvular leak, tilting-disc thrombosis after stopping warfarin, bioprosthetic degeneration → valve-in-valve, prosthetic ring on CXR + dental → viridans, optimize before bypass, cardioplegia mechanism, bicuspid + aneurysm + LAD → SAVR, early PVE = skin flora, warfarin embryopathy |

- Option counts: 4 ×2, 5 ×44. Length audit: key uniquely longest 0, uniquely shortest 0 (chance ≈ 6.8 each).
- Browser check: 46 questions, all 9 images decode; Q1 (numbered valve plane) renders cleanly.
- **Next:** wait for Jeeval's review. Then Part G (§26–§27: congenital heart disease, coarctation and the newborn).

**2026-10-10 — Part G written and built (38 items, 12 with images)** (Jeeval: "have fun!")
- Image keys prefixed `G_`. Most pediatric-lecture diagrams print the lesion name, so they were skipped; used the Robbins gross specimens (ASD + VSD, PDA, PFO, coarctation), the boot-shaped CXR, circumoral cyanosis, the coarctation angiogram, and AMBOSS images (transposition schematic, truncus with title/labels masked, subaortic VSD specimen, secundum-ASD ECG cropped of its header, digital clubbing). **Skipped:** AMBOSS "Ebstein anomaly.jpg" — it actually depicts transposition with PDA/PFO, not Ebstein.
- Heredoc gotcha (cost two syntax errors this session): inside a Python triple-quoted string in a bash heredoc, `\"` becomes a bare quote. Use ‘curly’ quotes in text added that way.

| Module | Items | Images | What it covers |
|---|---|---|---|
| `q_G1_chd` | 27 | 10 | foramen ovale closure (LA > RA), ductus closure (O₂ up, PGE₂ down), VSD commonest/membranous, symptoms at 4–8 weeks as PVR falls, ASD → atrial arrhythmias, secundum ASD ECG (RAD + iRBBB vs primum LAD), PFO paradoxical embolism → bubble study, preterm PDA → indomethacin, rubella → PDA, Eisenmenger (clubbing), differential cyanosis in reversed PDA, boot heart → RVOT obstruction sets cyanosis, tet spell knee-chest (SVR), BT shunt, DiGeorge → infundibular septum, TGA → PGE₁, hyperoxia test → echo, HLHS shock → PGE₁, truncus (aorticopulmonary septum), tricuspid atresia (LAD), Ebstein (lithium, WPW), Down → AV septal defect, Williams → supravalvular AS, Holt–Oram TBX5, TAPVR needs ASD, small muscular VSD → observe, secundum ASD → device closure |
| `q_G2_coarct_newborn` | 11 | 2 | juxtaductal coarctation case, critical coarctation → PGE₁, rib notching (angiogram), coarctation + Turner + berry aneurysm (gross), radio-femoral delay in a hypertensive adult, failed pulse-oximetry screen → echo, well newborn soft murmur → re-examine, louder murmur at 4 months → ECG/echo, any diastolic murmur is structural, VSD vs bicuspid incidence, critical lesions without a murmur |

- Option counts: all 5. Length audit: key uniquely longest 0, uniquely shortest 0 (chance ≈ 5.6 each).
- Browser check: 38 questions, all 12 images decode; Q16 (transposition schematic) renders cleanly.
- **Next:** wait for Jeeval's review. Then Part H (§28–§36: hypertension, HTN pharmacology, lipids, lipid pharmacology, aneurysm/dissection, connective tissue disease, vasculitis, PAD, mesenteric ischemia) and §37 (women and heart disease).

**2026-10-10 — Part H (+ §37) written and built (107 items, 29 with images)** (Jeeval: "keep going")
- **Bug found and fixed in Part F:** `q_F2_avr`'s severe-AS echo table appended data rows *after* `hdr()` had already closed its `<table>`, so the rows rendered outside the table. Fixed with a post-processing loop at the bottom of the module (also used in `q_H1_htn`, `q_H2_htnpharm`); Part F rebuilt and re-sent 2026-10-10. A scan of every module now confirms each stem has matched `<table>`/`</table>` and no `</table><tr>`. **Rule:** if a module's `hdr()` closes its table, either use its own row helper (as `q_C3_biomarkers` does) or append the post-processing loop.
- Image keys prefixed `H_`. Masks: `H_debakey` (DeBakey/Stanford titles removed, numbered 1–3), `H_abi` (computed indices masked), `H_cAnca`/`H_pAnca` (pattern names blacked out), `H_gcaTemporal` / `H_rubor` (panel letters), `H_blueToe` (date stamp). Dropped the Kawasaki angiogram (its masked "Aneurysm?" label covered the vessels). `H_sma` left unmasked ("Arteries"/"Clot" labels) because the questions ask about source and management, not identification.
- Item-design catch: the first ABI option set had two near-identical correct answers (0.39 and 0.40, same interpretation); replaced with distinct, error-based distractors (2.54 = inverted ratio).

| Module | Items | Images | What it covers |
|---|---|---|---|
| `q_H1_htn` | 16 | 2 | BP category (higher of two), measurement errors, masked vs white-coat (table), vascular subtype in the elderly, primary aldosteronism pattern, beta-blocker false-positive ARR, adrenal venous sampling, licorice (11β-HSD2), Liddle → amiloride, atherosclerotic RAS, Cushing (striae image) → dexamethasone test, pheochromocytoma (MEN 2) → metanephrines, OSA in resistant HTN, spironolactone 4th drug, malignant HTN (retinopathy image) → ≤ 25% MAP in hour 1, Cushing reflex |
| `q_H2_htnpharm` | 15 | 1 | stage 2 → two drugs in one pill, thiazide for osteoporosis/stones, ACEi/ARB for albuminuria, α1 blocker first-dose syncope, switch ACEi before conception, ACEi angioedema (bradykinin), DHP edema mechanism, clonidine rebound, ACEi in bilateral RAS, thiazide metabolic profile (tophi image), MRA hyperkalemia + acidosis (matched), BB + verapamil, thiazide vs loop hyponatremia, no ACEi + ARB, severe preeclampsia → IV labetalol |
| `q_H3_lipids` | 10 | 2 | type I chylomicronemia (lipemic serum), FH (tendon xanthomas), corneal arcus in a 32-year-old, PCSK9 biology, hypothyroidism → TSH first, nephrotic hyperlipidemia, type III (apoE2) → fibrate, apoA-I/LCAT, statin groups regardless of risk, diet (saturated fat > eggs) |
| `q_H4_lipidpharm` | 10 | 0 | statin → SREBP, simvastatin + clarithromycin rhabdo, gemfibrozil vs fenofibrate, fibrate + warfarin, cholestyramine spacing/TG, ezetimibe synergy, PCSK9 mAb step-up, niacin flushing → aspirin, bempedoic acid (gout), rhabdo → stop + CK |
| `q_H5_aorta` | 17 | 8 | AAA gross (smoking), rapid growth → repair, CT outer wall vs angiogram, one-time screening US, post-repair ischemic colitis (IMA), splenic aneurysm before pregnancy, popliteal aneurysm → look for AAA, pseudoaneurysm, cystic medial degeneration, type B CTA → esmolol first, numbered DeBakey → type A surgery, impulse control, dissection presenting as stroke → CTA before tPA, Adamkiewicz paraplegia, Marfan management, vascular EDS (COL3A1, face image), Loeys–Dietz |
| `q_H6_vasculitis` | 14 | 8 | GCA (steroids before biopsy; histology ↔ PMR), Takayasu, PAN (fibrinoid, HBV), Kawasaki → IVIG + aspirin, Buerger → stop smoking, c-ANCA GPA, p-ANCA MPA, EGPA (myocarditis kills), IgA vasculitis (purpura → intussusception), leukocytoclastic = immune complex (cryo/HCV), anti-GBM → plasmapheresis, Behçet HLA-B51, vessel-size matching |
| `q_H7_pad` | 14 | 6 | neurogenic vs vascular claudication, ABI computation (masked) → 0.40 rest-pain range, ABI > 1.4 → TBI, Leriche CTA, dependent rubor = CLTI not cellulitis, blue toe → look upstream, supervised exercise first, cilostazol contraindicated in HF, aspirin + low-dose rivaroxaban, acute limb ischemia → heparin + surgery, reperfusion compartment syndrome (fasciotomy image), CTA with runoff, SFA localization, prognosis (MI/stroke > limb) |
| `q_H8_mesenteric` | 6 | 2 | SMA embolus CTA → embolectomy + anticoagulation, normal labs don't exclude → CTA now, chronic mesenteric ischemia → revascularize, NOMI (pressors, digoxin), dead bowel → resect + second look, watershed splenic flexure |
| `q_H9_women` (§37) | 5 | 0 | pregnancy complications as risk enhancers, MHT timing hypothesis, SCAD with FMD, early menopause, atypical MI presentation in women |

- Option counts: all 5. Length audit: key uniquely longest 0, uniquely shortest 1 (chance ≈ 15).
- Browser check: 107 questions, all 29 images decode; Q3 (office/home table) renders as a proper table.
- **The exam is complete:** Parts A–H + §37 = 647 questions in 8 files.

---

## Full audit — 2026-10-10 (all 647 items, all 8 files rebuilt)

Every module was read item by item for accuracy, cueing and house style, plus scripted checks (scratchpad `audit.py`: lead-ins, grammar, HTML/table balance, option format, absolutes, clang, abbreviations; `lens.py` for lengths). Fixes are in the `q_*.py` sources; all 8 HTML files were rebuilt and browser-checked (647 questions parse, 197 images decode, no rows outside tables).

**Content corrections**
- F2 #7 (bileaflet mechanical aortic valve + polypectomy): key changed from "bridge with heparin" to "hold warfarin briefly, no bridging" (current guideline: bridge only for mechanical mitral, older valves or added risk factors).
- A5 #4: distractor "132/min" had no real derivation; replaced with 96/min (60% of age-predicted max).
- H5 #16: Loeys–Dietz distractor no longer says "gain-of-function TGFBR".
- A2 #1 (S4 "always" pathologic), A2 #11 and F1 #2 (bicuspid "always"/"every" aortopathy → about half): overstatements softened.
- H9 #4: the "postmenopausal = male sex" guideline claim corrected (guideline enhancer is premature menopause < 40; lecture view kept as an aside).
- B5 #20 wrong explanation reworded so it no longer contradicts H4 #4 (fibrate–warfarin displacement).

**Duplicates removed:** F1 #6 (Heyde mechanism, = A3 #10) now asks long-term management (valve replacement); F1 #20 (AS + nitroglycerin, = A3 #9) replaced with apparently asymptomatic severe AS → supervised exercise test.

**Style:** no negative lead-ins left ("least likely", "should be avoided", "withheld", "why … not"); stems no longer describe images (A1 #12, A4 #12, B3 #8, B3 #16, B5 #18–19, E1 #6, G1 #17, H5 #16); "classic/characteristic" lead-ins and lecturer names removed from stems (G1 #9, #23, F1 #25, G2 #10, H3 #7, H5 #9); "A 81" → "An 81" (×4); all temperatures now carry °F; format-mismatched keys made parallel (B2 #6, D2 #19, D2 #26, E2 #7, E3 #7, E3 #15, F1 #25, H2 #14); absolutes trimmed from distractors (E3 #18, F2 #6, G1 #27, H8 #5, H9 #1, #2, #4).

**Abbreviations:** options no longer carry unexplained short forms (ACE, LDL/HDL/VLDL, STEMI, LAD, AV, ENaC, ADH, RAAS, INR, FDG-PET, COX-2, TAVR in options, etc.). A scripted pass (scratchpad `abbr.py`, ~820 edits) expands every remaining abbreviation at its first use in each item's stem/explanation ("full name (ABBR)"), spells IV/AV/LV/RV/US/TB/ICU/GI out in full, and writes eli5 text without short forms. Kept as-is on purpose: ECG, CT, MRI, wave/lead names (QRS, ST, PR, QT, aVR…), gene symbols, apolipoprotein and HLA names, IgA/IgG, PCSK9/P2Y12/cAMP in option text, HACEK, c-ANCA. Mnemonics MaRRoW, WiLLiaM, STOP-BANG and CRASH were unpacked.

**Images:** 22 AMBOSS figures in `Board Study/figures/amboss/` had been converted from .png to .jpg; `images.py` now points at the .jpg files (masks/labels re-checked on a contact sheet).

**Length audit after the audit:** key uniquely longest 0 in every Part; uniquely shortest 1 (Part A) — all far below chance.
