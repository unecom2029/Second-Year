# How this was built

A dev log for future-me (or a future Claude session) picking this back up.

## What this is

An interactive, offline HTML study version of the "Lower Extremity, Screening and Diagnosis OMM Exam 26-27" rubric (the faculty grading rubric for the OMM skills-test practical). Every screening/diagnosis test row is interactive: hover (desktop) or tap (touch) shows purpose / step-by-step technique / diagnosis-naming logic / reference photos (where a good one exists) for that row.

It's a single self-contained HTML file (`Lower Extremity, Screening and Diagnosis OMM Exam.html`) plus an `assets/` folder (currently empty — see "Why no images" below). No build step, no server, no dependencies — just open the HTML file in a browser (or serve the folder for the most reliable local preview — see "Verifying" below).

This is the **fourth of five** related OMM rubrics being built from the same source series (Axial Spine and Ribs, Lumbar Spine/Pelvis/Sacrum, and Upper Extremity are already done and polished; a treatment-technique rubric is the one remaining future build). Like the other three, this one was built by copying the *current, fully-polished* architecture of the most-recently-finished rubric (Upper Extremity) line-for-line (same CSS, same JS interaction logic, same per-row 4-column grading, memory hooks, text-size control, row-number badges, expand-to-reader-modal button). Nothing architectural was re-invented here; this file only documents what's specific to the lower-extremity content — **including the flex/min-width CSS fix that was diagnosed and applied to all three prior rubrics right after Upper Extremity shipped, which this build has baked in from the start rather than as an afterthought** (see "The flex/min-width CSS fix" section below).

## Row structure

13 rows total, following the task brief's transcription of the source rubric exactly:

1. Communication (plain row, no popover)
2. Consent (plain row, no popover)
3. Washes Hands (plain row; only 2 real grading options, middle two are `N/A-DO NOT SELECT`)
4–10. Seven hoverable rows (hip, knee, fibular head, talocrural/subtalar, navicular/cuboid/cuneiforms, metatarsals/phalanges, most-restricted positional diagnosis)
11. Accuracy of the Specific Lower Extremity Diagnosis (hoverable, eighth hoverable row)
12. CAP summary: "Did the Student have to CAP this Rubric?" (plain row, own 4-option wording)
13. CAP summary: "Was the CAP Completed Successfully?" (plain row, own 4-option wording)

**The one row-label wrinkle, matching the pattern already established in the other three rubrics in this series:** row 11 ("Accuracy of the Specific Lower Extremity Diagnosis") uses `100% Correct` as its first-column label instead of the usual `100% Correct and Fluid` — same as every other short "Accuracy of X" summary-style row throughout this rubric series (e.g. "Accuracy of the Specific Upper Extremity Diagnosis" in the Upper Extremity rubric, "Accuracy of Innominate Diagnosis" and "Accuracy of Sacrum Diagnosis" in the Lumbar/Pelvis/Sacrum rubric). Rows 4–10 keep the standard 4-option wording. Verified directly in the live DOM (see "Verifying" below), not assumed.

No student-name/date header fields were added, matching the source rubric and the rest of this series' precedent.

## The flex/min-width CSS fix (baked in from the start, not retrofitted)

Right after Upper Extremity shipped, a real bug was found and fixed live across all three existing rubrics: `#sidePanel` is a flex child with `flex: 0 0 360px`, and a flex child's default `min-width` is `auto` — meaning a long unbreakable string in its content (e.g. Upper Extremity's row 9 technique list `scaphoid/lunate/capitate/triquetrum/trapezium/trapezoid/hamate`) could force the panel wider than its 360px flex-basis, making the whole layout visibly resize depending on which row was hovered. This build was written *after* that fix existed in the reference file, so all four fix points were copied in directly rather than added later:

1. `#sidePanel{...}` includes `min-width: 0;` alongside `flex: 0 0 360px;` (confirmed present in the CSS source, line-by-line copy from the current Upper Extremity reference).
2. `#sidePanelInner{...}` includes `overflow-wrap: break-word; word-break: break-word;` alongside its existing `overflow-y: auto;`.
3. `#popover{...}` includes the same `overflow-wrap: break-word; word-break: break-word;` alongside its existing `overflow-y: auto;`.
4. `#readerContent{ zoom:1.35; overflow-wrap: break-word; word-break: break-word; }` — all three declarations on the one-line rule.

**Live verification (not just source inspection):** at 1600px viewport width, `getComputedStyle` was read directly for all four properties — `sidePanel.minWidth === "0px"`, `sidePanelInner.overflowWrap === "break-word"` (and `wordBreak`), `popover.overflowWrap === "break-word"` (and `wordBreak`), `readerContent.overflowWrap === "break-word"` (and `wordBreak`) — all confirmed true.

**Then the actual regression test**: at 1600px width (≥1300px side-panel-mode breakpoint), each of the 8 hoverable rows was hovered in sequence via a scripted `mouseenter` dispatch, and `document.getElementById('sidePanel').getBoundingClientRect().width` was read after each one. Every single row measured exactly **360**:

| Row (data-key) | Row name | Measured `#sidePanel` width |
|---|---|---|
| 4 | Hip Screening | 360 |
| 5 | Knee Screening | 360 |
| 6 | Fibular Head Screening | 360 |
| 7 | Talocrural and Subtalar Screening | 360 |
| 8 | Navicular, Cuboid, and Cuneiform Screening | 360 |
| 9 | Metatarsal and Phalange Screening | 360 |
| 10 | Most Restricted Somatic Dysfunction — Positional Diagnosis | 360 |
| 11 | Accuracy of the Specific Lower Extremity Diagnosis | 360 |

Zero exceptions. No row's content contains a long unbreakable slash-joined string the way Upper Extremity's row 9 did, but the fix is architectural (not content-dependent), so it's confirmed regardless — and it protects this file the same way if a future images/content round adds a long unbroken string later.

## How the content got in there

1. **Rubric skeleton (all 13 rows, exact wording, exact per-row column labels)**: transcribed directly from the task brief, which itself was checked against the Week 5 OMM course-notes plain-text extraction (`omm5_text.txt`) — the rubric's own "LO 10 - LE Screening Exam Rubric" section (a region/minimum-screen-items/common-diagnoses summary table) appears there as a close paraphrase of the actual rubric line items.
2. **Rows 4–11 popover content (purpose / how-to-perform / diagnosis-naming logic)**: sourced from `omm5_text.txt`, specifically the "LO 10 - Lower Extremity Screening Exam" section (screening-exam walkthrough, lines ~397–440 of the extracted text) and its worked Q&A on hip extension stabilization, plus the same LO's condensed rubric-summary table (lines ~733–749) for the "common diagnoses you can name" language used in each row's `normal` field, plus supporting clinical color pulled from the arches/gait biomechanics section (LO 2–3, lines ~91–147) for hook material — e.g. the foot-tripod and windlass-mechanism concepts used in rows 8 and 9.
3. **Rows 4–11 reference images**: none. See "Why no images" below.

## Row-by-row content sourcing (rows 4–11, the only rows with popovers)

All eight hoverable rows are **text-only**, sourced from `omm5_text.txt` as follows (line numbers refer to the plain-text extraction in the scratchpad):

- **Row 4 (Hip Screening)** — steps and purpose transcribed directly from line 409–410 ("Hip ROM and strength screen. Flexion, extension, internal/external rotation, abduction/adduction bilaterally. Stabilize pelvis/hip for extension so the patient does not roll into false motion."), plus the worked Q&A at lines 434–439 ("During hip extension testing in side-lying, why stabilize the pelvis? To avoid mistaking pelvic/lumbar rotation for true hip extension. Stabilization keeps the screen anatomically honest.") used directly as the row's hook. The "common diagnoses you can name" language in `normal` comes from the LO 10 summary table's Hip row (line 422–424: "Restricted hip IR/ER, flexion loss, abductor dysfunction, femoroacetabular capsule restriction").
- **Row 5 (Knee Screening)** — transcribed directly from line 411–412 ("Knee screen. Flexion/extension, tibial internal/external rotation, screw-home observation, varus/valgus glide, anterior/posterior tibial glide, patellar motion, and effusion/mechanical signs."). The `normal` field's diagnosis language comes from the summary table's Knee/tibia row (line 425–427: "Externally or internally rotated tibia, patellar glide restriction, valgus/varus strain, knee capsule imbalance.").
- **Row 6 (Fibular Head Screening)** — transcribed directly from line 413–414 ("Fibular head. Contact fibular head and compare anterior-lateral vs posterior-medial glide; relate findings to ankle sprain, fibular nerve symptoms, and IT band/peroneal tension."). Per the task brief's explicit note, the source consistently says "anterior-lateral/posterior-medial" while the rubric's own row text says "anterolateral/posteromedial" — the row label keeps the rubric's own wording, while the hook and steps use the source's hyphenated phrasing interchangeably (same concept). Diagnosis language in `normal` from the summary table's Fibula row (line 428–430).
- **Row 7 (Talocrural and Subtalar Screening)** — this row, along with rows 8 and 9, splits the single source paragraph at line 415–416 ("Ankle and foot. Talocrural dorsiflexion/plantarflexion at the talus, subtalar inversion/eversion through calcaneus, forefoot motion, toes, navicular, cuboid, cuneiforms, and metatarsals.") into three rubric-matching rows. Row 7 takes the talocrural (dorsiflexion/plantarflexion) and subtalar (inversion/eversion) portion specifically.
- **Row 8 (Navicular, Cuboid, and Cuneiform Screening)** — takes the midfoot-bone portion of the same source paragraph (navicular, cuboid, cuneiforms), with supporting arch-architecture color from the LO 3 Arches section (lines 129–137: medial longitudinal arch = calcaneus-talus-navicular-cuneiforms-rays 1–3; lateral longitudinal arch = calcaneus-cuboid-rays 4–5) used in both the hook and the steps to explain *why* the navicular/cuboid/cuneiform split matters mechanically.
- **Row 9 (Metatarsal and Phalange Screening)** — takes the forefoot portion of the same source paragraph (metatarsals, toes/phalanges), with supporting color from the LO 2 gait-phase table's pre-swing row (line 122–125: "toe flexors and the windlass effect help convert the foot from flexible platform to rigid lever") used in the hook to tie forefoot mobility to propulsion, and the transverse-arch/Morton-neuroma connection (LO 3, line 135–137) used in the steps as a note on transverse arch integrity.
- **Row 10 (Most Restricted Somatic Dysfunction — Positional Diagnosis)** — sourced from line 417–418 ("Name, treat, and recheck. State the region, direction of ease/restriction, likely pain generator, and pre/post effect. Rechecking is part of the treatment, not an afterthought.") and, per the task brief's explicit differentiation guidance, framed as the row that grades the *process* of naming a positional diagnosis (not yet the *accuracy* of the specific joint/side/direction named, which is row 11's job) — the same process-vs-accuracy split used for Upper Extremity's rows 11/12.
- **Row 11 (Accuracy of the Specific Lower Extremity Diagnosis)** — sourced from the same "name, treat, and recheck" language plus the LO 10 summary table's full four-region breakdown (hip/knee-tibia/fibula/ankle-foot, lines 419–433), used here to build the accuracy-specific checklist (correct region, correct direction of ease/restriction, correct pain generator, correct articular-vs-soft-tissue barrier call) — mirroring exactly how Upper Extremity's row 12 (barrier-type accuracy) was built from its own rubric-line description.

Every hoverable row's `hook` is an original short mnemonic written to compress the corresponding source-text technique into something sticky (e.g. row 6's "the fibular head's own compass," row 8's arch-architecture framing, row 9's windlass/propulsion framing), consistent with the `hook` field's purpose in the other three rubrics in this series — none of these are quoted from the source text verbatim beyond the short phrases explicitly noted above.

## Why no images (0 of 8 hoverable rows illustrated)

This build is **entirely text-only** — a deliberate, documented decision, not an oversight, and expected per the task brief. The Week 5 OMM lecture deck's 43 embedded class figures were already checked (by figure caption, per the task brief's own grep against the full caption list) and none of them are screening/diagnosis technique photos for the specific rows this rubric grades. They fall into the same two out-of-scope categories already seen twice in this series:

1. **Pathology/condition diagrams and clinical imaging** — e.g. pes cavus/pes planus presentation, plantar fasciitis, hallux valgus/bunion, Morton neuroma, foot drop, meniscal tears, Baker cyst, varus/valgus knee deformity, patellofemoral pain, hip osteoarthritis, labral tear, greater trochanteric pain syndrome, meralgia paresthetica, piriformis syndrome, SI joint dysfunction, Ottawa ankle/knee rule figures. This is *clinical-diagnosis* content (LO 1, 4–9, "what condition is this and how do you work it up"), not *OMM screening technique* content (LO 10, "how do you physically screen the joint"). The rubric only grades the latter.
2. **OMM *treatment* technique photos** — BLT for the tibia (seated and supine), BLT of the patella, talocrural/subtalar BLT bootjack, Still technique for the midfoot, BLT of the femoroacetabular joint, HVLA for externally/internally rotated tibia, counterstrain for lateral and medial hamstrings — all from LO 11 ("OMT Technique Atlas"). These are explicitly out of scope for a *screening/diagnosis* rubric, the same category already excluded from the other three rubrics in this series (e.g. Axial Spine/Ribs' excluded Still Arm Arc/FPR photos, Lumbar/Pelvis/Sacrum's excluded Still-technique and SI Joint BLT photos, and Upper Extremity's excluded Spencer sequence/radial head ME/counterstrain photos).

No substitution was forced. Per this series' established "don't force a bad match" principle (already exercised repeatedly in all three prior rubrics' build notes), all eight hoverable rows ship text-only. The Week 5 notes' LO 10 section is detailed enough — a clear step-by-step walkthrough from observation through hip, knee, fibular head, and ankle/foot, plus a worked Q&A and its own condensed screening-rubric summary table — to carry real teaching content on its own without images.

**This mirrors exactly what happened with the Lumbar/Pelvis/Sacrum rubric (2/10 illustrated before Round 2/3) and, even more directly, the Upper Extremity rubric (0/9 illustrated before the very next message supplied a filling PDF).** For Upper Extremity, the user supplied `UE.pdf` (OPP Vol.1, UNECOM 2025, Upper Extremity chapter) in the message immediately following the initial build, and three of nine hoverable rows (SC joint, AC joint, radial head) were illustrated in that same follow-up round using `pdftoppm -r 300 -png` renders, a PIL content-band auto-cropper, and individual hand-scoped `Edit` calls per row. **The same thing may well happen here**: if the user supplies an OPP Vol. 1 chapter excerpt covering the hip, knee, or ankle-and-foot exam (the textbook series clearly has one, given the Sacrum/Lumbar/Innominates and Upper Extremity chapters already pulled for the other rubrics in this series cross-reference the same book's other regional chapters), this build should get the identical re-sourcing treatment. Flagging this explicitly now so the next conversation turn (or a future Claude session) knows exactly where to start.

## Architecture elements replicated from the reference rubric (confirmed by direct comparison, not assumption)

- Single self-contained HTML + `assets/` folder (created, currently empty), no `index.html` naming.
- `DATA` object keyed by row number 4–11 (the eight hoverable rows only), each with `name`, `purpose`, `hook`, `steps[]`, `normal`, and `images: []` (empty array, matching the reference's explicit-empty-array convention for text-only rows) — `buildContent()` already handles this safely since `d.images && d.images.length` gates the image block.
- Per-row 4-column grading: native `<input type="radio" name="r{n}">` per row, abbreviated `<span class="grade-text">` labels, full original wording preserved as `title=""` on the `<label>`, `.is-na` modifier on N/A cells.
- `table-layout:fixed` with identical `colgroup` widths to the reference (`col.col-grade{width:5.5%}` / `col.col-test{width:78%}`).
- Row numbers as `.row-num-badge` spans, `float:right`, injected as the first child of each description `<td>` — no dedicated row-number column exists anywhere in this file (verified: `td.row-num`/`col-num` selectors return 0 matches; live-DOM `.row-num-badge` count is exactly 13, matching the 13 `<tr data-row>` rows).
- Dual interaction mode: sticky `#sidePanel` at ≥1300px via `showInPanel()`, floating `#popover`/`#overlay` below that via `openPopover()`/`positionPopover()`/`closePopover()`.
- Click-to-enlarge `#lightbox` machinery present and correctly wired (delegated click listener on `#popContent .pop-images img, #sidePanelContent .pop-images img, #readerContent .pop-images img`), even though there are currently zero images to click — ready for a future re-sourcing pass.
- Expand button (`#sideExpandBtn`/`#popExpandBtn`) opening `#readerModal`/`#readerContent` at `zoom:1.35`, tracked via `currentKey`, `#readerModal` at `z-index:1800`. All shared `#popover X, #sidePanelContent X, #readerContent X{...}` CSS rules were copied by hand from the reference's already-finished CSS — no regex was run to add them.
- Text-size control: floating A−/A+ pill, `--font-scale` CSS variable, persisted to `localStorage` under **`omm-lower-extremity-font-scale`** — a new, file-unique key, confirmed different from `omm-axial-ribs-font-scale`, `omm-lumbar-pelvis-sacrum-font-scale`, and `omm-upper-extremity-font-scale`.
- Both historical bugs avoided: `closePopover()` resets `popover.style.display = ''` (not just the `.open` class) — copied verbatim from the reference and re-verified live (see below); the base `#sidePanel{ display:none; }` rule appears before its `@media (min-width:1300px)` override in source order — also copied verbatim and re-verified live.
- **The newly-fixed flex/min-width bug (Step 0.5) avoided from the start** — see the dedicated section above with the full 8-row measured-width table.

## On the "don't bulk-regex across the whole file" warning

The task brief flagged the historical bug from the first rubric's build: a regex meant to extend `#sidePanelContent SELECTOR{...}` CSS rules to also match `#readerContent SELECTOR{...}` was once run across the entire file, including the `<script>` block, silently corrupting JavaScript that looked fine in a screenshot but had zero working interactivity (caught only by `node --check`).

This build was written by hand, section by section, copying the reference file's already-correct (post-fix) CSS and JS verbatim and only substituting the row content — no find/replace of any kind was run across the file, so this specific failure mode has no opening here. The verification discipline (`node --check`, brace-count parity, live interaction testing) was still followed in full regardless.

## Verifying

```
cd "Lower Extremity, Screening and Diagnosis OMM Exam"
python3 -m http.server 8796
```

then load `http://127.0.0.1:8796/Lower%20Extremity%2C%20Screening%20and%20Diagnosis%20OMM%20Exam.html`.

This build was verified this way:

- **`node --check` on the extracted `<script>` block: passed cleanly, zero syntax errors.** Brace-count parity checked first as a cheap sanity pass (151 `{` / 151 `}` in the raw file) before the full syntax check.
- Zero console errors on load (checked live via the browser tool, not just visually), and zero console errors after every subsequent interaction test below.
- All 13 `<tr data-row>` rows present; exactly 8 have a `.hoverable` span (rows 4–11) and all 8 have a matching `DATA[key]` entry (keys 4–11), with zero mismatches in either direction (confirmed via live-DOM `Object.keys(DATA)` vs. `.hoverable[data-key]` comparison).
- `.row-num-badge` count === 13 (live-DOM count, not a raw-file grep); zero `td.row-num`/`col-num` elements anywhere in the document.
- Live-DOM spot-check of rows 3, 11, 12, and 13's `.grade-text` labels confirmed each differs from the standard `100%/88%/75%/<75%` pattern exactly as specified: row 3 shows `100%` (not `100% & Fluid`) with N/A on the middle two columns; row 11 shows `100%` (not `100% & Fluid`) with standard 88%/75%/<75% on the rest; row 12 shows its own CAP-summary wording (`NO CAP`/`N/A`/`N/A`/`YES CAP`); row 13 shows its own wording (`YES Done`/`Partial`/`N/A`/`NO`).
- At 1600px width, `getComputedStyle(sidePanel).display === "block"`; at 900px width, `=== "none"`.
- **The Step 0.5 side-panel-width regression check**: at 1600px width, all 8 hoverable rows were hovered in sequence via scripted `mouseenter` events, and `sidePanel.getBoundingClientRect().width` was read after each — **all 8 measured exactly 360**, with zero exceptions (full per-row table above).
- CSS bug-fix property values confirmed via `getComputedStyle` (not just source-text grep, which can miss reformatted rules): `sidePanel.minWidth === "0px"`; `sidePanelInner.overflowWrap === "break-word"` and `.wordBreak === "break-word"`; `popover.overflowWrap === "break-word"` and `.wordBreak === "break-word"`; `readerContent.overflowWrap === "break-word"` and `.wordBreak === "break-word"`.
- At 900px width (floating-popover mode): simulated a `click` on row 4's `.hoverable` — popover opened (`.open` class present, inline `display:"block"`), closed via the × button (`.open` removed, inline `style.display` reset to `""` — not left at `"block"`), then reopened and closed a second time to confirm no stuck-open state across repeated cycles.
- At 900px width: clicked row 9's `.hoverable` to open the popover, then clicked `#popExpandBtn` — `#readerModal` opened (`zoom:1.35` on `#readerContent`) with the correct row 9 content ("Metatarsal and Phalange Screening"), then closed cleanly via `#readerCloseBtn` (`.open` removed).
- Since there are zero images in this build, image-preload verification (done for the other three rubrics once images existed) does not apply here — the lightbox/image-click delegation code is present and unchanged from the reference but has nothing to click yet.

## If you want to add images in a future round

Follow the same process used for the Lumbar/Pelvis/Sacrum rubric's Round 2/3 and the Upper Extremity rubric's Round 2 (see either rubric's own `BUILD_NOTES.md` for the full worked example):

1. Get a real source (ideally an OPP Vol. 1 textbook chapter PDF covering the hip, knee, or ankle-and-foot exam — the lecture deck was already checked and does not have usable screening-technique photos).
2. `pdftoppm -r 300 -png` to render full-resolution page images (beats `pdfimages`, which has fragmented scans in this same textbook series before).
3. Use the PIL content-band auto-cropper approach (scan for near-white gaps to auto-split stacked photos on one page) rather than manually eyeballing every crop box.
4. Visually review every crop via the Read tool before keeping it.
5. Add `images: [{src:"assets/your_file.jpg", caption:"... (Source: ...)"}]` to the relevant row's `DATA` entry via an individual, hand-scoped `Edit` call — never a bulk find/replace across the file.
6. Re-run the full verification pass (`node --check`, live interaction testing, the Step 0.5 side-panel-width check, image-preload `naturalWidth > 0` checks) before considering the round done.

## Round 2: a partial-match textbook excerpt — big text upgrade, one image, most rows still unillustrated

The user supplied `LE.pdf` — OPP Vol.1, UNECOM 2025, the Lower Extremity chapter — in the very next message, following the exact pattern seen with the other rubrics. Unlike the Sacrum/Lumbar/Innominates/Upper-Extremity PDFs, though, **this excerpt is only 34 pages and stops at book page 119** ("Evaluation for Tibial Rotation"), which is *before* the textbook's own "Special Tests of the Lower Extremity" section (book pp. 122–133 per its table of contents — FABERE, Ober's, Thomas, Trendelenburg, McMurray, Apley's, valgus/varus stress, Lachman's, drawer tests, squeeze test, talar tilt, Thompson test, Tinel's). That's the section that would contain hands-on hip/knee/ankle exam photos analogous to the SC-joint/AC-joint/radial-head photos that filled in Upper Extremity's Round 2 — **it simply isn't part of what was supplied here.** Worth noting for a possible future round: even if that section does turn up later, most of its named tests (FABERE, McMurray, Lachman's, drawer, Ottawa-rules-related tests) are orthopedic pathology special tests, not the OMM structural screening motions this rubric grades — the same category already excluded elsewhere in this series (e.g. the Innominates rubric's excluded Patrick/FABERE photo) — so a future pass would still need to filter carefully rather than assume every photo in that section is a fit.

**What this excerpt DID contain: exceptionally precise textbook protocol text for two rows, and one legitimate reference image.**

- **Row 5 (Knee Screening)** — added the textbook's own **"Evaluation for Tibial Rotation"** protocol verbatim-adjacent (position: seated, knee flexed, physician marks patella midline and tibial tuberosity; action: patient extends the knee while digit position is held; results: tuberosity should align with the patella at 90° flexion and rotate laterally in full extension — external tibial rotation suspected if the tuberosity sits lateral to the patella in BOTH positions, internal tibial rotation suspected if it sits medial/in-line at 90° and fails to move laterally into extension). Also folded in the textbook's precise screw-home-mechanism explanation (why a free tibia externally rotates on full extension) and the **"Evaluation for Posterior Tibia on Femur"** test (same setup as the ligamentous Drawer test — supine, knee bent, foot stabilized, anterior-then-posterior pressure on the proximal tibia; a posterior-tibia-on-femur finding reaches its barrier posteriorly while anterior motion is restricted before reaching that barrier) as additional context for the row's A/P glide step. This is a real content upgrade over the original Week-5-notes-only version — the original said "test tibial IR/ER" as one bullet; the row now has the textbook's actual landmark-based protocol.
- **Row 6 (Fibular Head Screening)** — added the textbook's own **"Evaluation for Fibular Head Dysfunction"** protocol verbatim-adjacent (position: seated or supine, knee bent 90°; action: glide the fibular head posteromedially and anterolaterally, compare bilaterally; results: resists anterolaterally → posterior fibular head, resists posteromedially → anterior fibular head), plus an explicit **nerve-safety note** not present in the original version: avoid direct pressure on the common fibular nerve, which winds around the fibular neck right at this contact point. Also added the clinical cross-check that posterior fibular head dysfunction specifically can mimic common fibular nerve entrapment and often follows a recurrent ankle sprain, with tenderness expected at the fibularis longus/brevis muscles too. This was the single biggest per-row upgrade in this round — the row went from a general "compare anterior-lateral vs posterior-medial glide" instruction to the textbook's exact position/action/results protocol with the correct resisted-direction interpretation rule spelled out.
- **Row 7 (Talocrural and Subtalar Screening)** — added `assets/ankle_foot_motions_reference.jpg`, a clean 4-panel photo (plantarflexion / dorsiflexion / inversion / eversion) from the textbook's Ankle & Foot Motion section (p.113), cropped and reviewed via the Read tool before use. **Honesty note in the caption:** this is a *motion* reference, not a hands-on *technique* photo — no examiner's hands are shown, it's just the four positions the row grades, on a bare foot. Captioned accordingly rather than implied to be an exam-technique demonstration. Also added the textbook's supination/pronation composite-motion definitions (supination = adduction + plantarflexion + inversion; pronation = abduction + dorsiflexion + eversion) to the row's hook as bonus context, since those composite terms come up in the same source material even though the rubric's own row text sticks to the four individual motions.
- **Rows 4 (Hip), 8 (Navicular/Cuboid/Cuneiforms), 9 (Metatarsals/Phalanges), 10 (Positional Diagnosis), 11 (Diagnosis Accuracy) — unchanged, still text-only.** The textbook excerpt's hip content (AROM/PROM motion list, hip ROM degree table) essentially confirms what was already in row 4 from the Week 5 notes rather than adding anything new technique-wise, so it was left as-is. Rows 8–9 (midfoot/forefoot) and 10–11 (diagnosis-naming rows) had no new textbook content in this excerpt beyond general arch biomechanics already reflected in row 8's existing text.

**Net result: 1 of 8 hoverable rows now has an image (row 7) — up from 0 of 8 — but 2 additional rows (5 and 6) got a substantial, textbook-precise content upgrade even though they remain text-only.** This rubric is likely to stay the most text-heavy of the four screening/diagnosis rubrics in this series unless the textbook's own Special Tests section (book pp. 122–133) becomes available and turns out to contain OMM-screening-relevant (not just orthopedic-pathology) technique photos.

**Verification for this round:** `node --check` passed cleanly on the re-extracted script (single hand-scoped `Edit` call touching rows 5, 6, and 7 together, no bulk regex). Served locally; live JS execution confirmed the one new image resolves with `naturalWidth > 0` (zero `onerror`), and `DATA[7].images` contains exactly the one expected file.
