# How this was built

A dev log for future-me (or a future Claude session) picking this back up.

## What this is

An interactive, offline HTML study version of the "Upper Extremity, Screening and Diagnosis OMM Exam 26-27" rubric (the faculty grading rubric for the OMM skills-test practical). Every screening/diagnosis test row is interactive: hover (desktop) or tap (touch) shows purpose / step-by-step technique / diagnosis-naming logic / reference photos (where a good one exists) for that row.

It's a single self-contained HTML file (`Upper Extremity, Screening and Diagnosis OMM Exam.html`) plus an `assets/` folder (currently empty — see "Why no images" below). No build step, no server, no dependencies — just open the HTML file in a browser (or serve the folder for the most reliable local preview — see "Verifying" below).

This is the **third** of five related OMM rubrics being built from the same source series (Axial Spine and Ribs, and Lumbar Spine/Pelvis/Sacrum, are already done and polished; Lower Extremity and a treatment-technique rubric are still future builds). Like the Lumbar/Pelvis/Sacrum rubric, this one was built by copying the *current, fully-polished* architecture of that most-recently-finished rubric line-for-line (same CSS, same JS interaction logic, same per-row 4-column grading, memory hooks, text-size control, row-number badges, expand-to-reader-modal button). Nothing architectural was re-invented here; this file only documents what's specific to the upper-extremity content.

## Row structure

14 rows total, following the task brief's transcription of the source rubric exactly:

1. Communication (plain row, no popover)
2. Consent (plain row, no popover)
3. Washes Hands (plain row; only 2 real grading options, middle two are `N/A-DO NOT SELECT`)
4–12. Nine hoverable rows (SC joint, AC joint/glenohumeral, elbow, radial head, wrist, radiocarpal/carpal bones, hand/fingers, most-restricted positional diagnosis, accuracy of specific diagnosis) — see below
13. CAP summary: "Did the Student have to CAP this Rubric?" (plain row, own 4-option wording)
14. CAP summary: "Was the CAP completed successfully?" (plain row, own 4-option wording)

**The one row-label wrinkle, matching the pattern already established in the other two rubrics in this series:** row 12 ("Accuracy of the Specific Upper Extremity Diagnosis") uses `100% Correct` as its first-column label instead of the usual `100% Correct and Fluid` — same as every other short "Accuracy of X" summary-style row throughout this rubric series (e.g. "Accuracy of Innominate Diagnosis" and "Accuracy of Sacrum Diagnosis" in the Lumbar/Pelvis/Sacrum rubric). Rows 4–11 keep the standard 4-option wording. Verified directly in the live DOM (see "Verifying" below) rather than assumed.

No student-name/date header fields were added, matching the source rubric and the rest of this series' precedent.

## How the content got in there

1. **Rubric skeleton (all 14 rows, exact wording, exact per-row column labels)**: transcribed directly from the task brief, which itself was checked against the Week 7 OMM course-notes plain-text extraction (`omm7_text.txt`) — the rubric's own LO 8 section ("Upper Extremity Screening Rubric") appears there as a close paraphrase of the actual rubric line items.
2. **Rows 4–12 popover content (purpose / how-to-perform / diagnosis-naming logic)**: sourced from `omm7_text.txt`, specifically the "LO 8 - Upper Extremity Screening Rubric" section (screening-exam walkthrough, lines ~166–210 of the extracted text) and its worked Q&A on radial head screening, plus supporting clinical color pulled from the surrounding LO 9-10A/B/C sections (shoulder, elbow/forearm, wrist/hand conditions) for hook material — e.g. the "anterior radial head → supination restriction / posterior radial head → pronation restriction" pearl from the LO 9-10B elbow/forearm table.
3. **Rows 4–12 reference images**: none. See "Why no images" below.

## Row-by-row content sourcing (rows 4–12, the only rows with popovers)

All nine hoverable rows are **text-only**, sourced from `omm7_text.txt` as follows (line numbers refer to the plain-text extraction in the scratchpad):

- **Row 4 (SC Joint and Shoulder Girdle Screening)** — steps and purpose transcribed directly from lines 180–181 ("SC joint and shoulder girdle. Thumb in jugular notch/fingers over proximal clavicle. Arm forward/back should move clavicular head posterior/anterior; arm up/down should move it inferior/superior. Decide if restriction is articular or soft tissue."). The hook's closing line about cross-checking against thoracic outlet symptoms draws on the SC/clavicle/first-rib/thoracic-inlet anatomy context from LO 9-10A (line 216) and the Thoracic Outlet Syndrome entry (lines 224–227).
- **Row 5 (AC Joint and Glenohumeral Motion)** — transcribed directly from lines 182–183 ("AC joint and glenohumeral motion. Evaluate internal/external rotation and shoulder horizontal adduction/abduction patterns while monitoring AC mechanics and shoulder soft tissues.").
- **Row 6 (Elbow Screening)** — transcribed directly from lines 184–185 ("Elbow. Test flexion/extension, then passive valgus/varus joint play with the wrist stabilized.").
- **Row 7 (Radial Head Screening)** — transcribed from lines 186–187 ("Radial head. Palpate anterior/posterior radial head glide during pronation/supination and decide articular radial head vs pronator/supinator soft-tissue barrier."), plus the worked Q&A at lines 206–210 ("During radial head screening, what motion pair should you compare? Anterior/posterior radial head glide during pronation and supination, while deciding if the barrier is articular or soft tissue.") used as the row's hook framing, and the "Radial head dysfunction: Anterior radial head often tied to supination restriction; posterior radial head tied to pronation restriction" pearl from the LO 9-10B Elbow and Forearm table (line 291–294), used both in the hook and folded into the steps as a cross-check.
- **Row 8 (Wrist Screening)** — transcribed directly from lines 188–189 ("Wrist. Test flexion/extension and radial/ulnar deviation.") — note the rubric's own row text uses "abduction/adduction" as the plain-English equivalent of radial/ulnar deviation, matching the task brief's row wording.
- **Row 9 (Radiocarpal Joint and Carpal Bone Screening)** — transcribed directly from lines 190–191 ("Radiocarpal and carpal bones. Wiggle proximal row then distal row; look for the most restricted scaphoid/lunate/capitate/triquetrum/trapezium/trapezoid/hamate relationship.").
- **Row 10 (Hand and Finger Screening)** — transcribed directly from lines 192–193 ("Hand and fingers. Stabilize carpals, glide metacarpals, then screen MCP/PIP/DIP phalanges, especially if arthritis, trauma, or focal pain is present.").
- **Row 11 (Most Restricted Somatic Dysfunction — Positional Diagnosis)** — sourced from line 194–195 ("Name and treat. State the most restricted UE somatic dysfunction, pick a safe modality, communicate reasoning, use minimum effective force, maintain timing, and recheck.") and, per the task brief's explicit differentiation guidance, the "Most restricted diagnosis" rubric-line description at lines 202–203 ("After screening bilaterally, names one greatest restriction with position/motion language and ties it to treatment choice.") — used as this row's hook verbatim-adjacent, since row 11 is specifically about the *process* of naming a positional diagnosis (not yet the *accuracy* of the specific joint/side/barrier named, which is row 12's job).
- **Row 12 (Accuracy of the Specific Upper Extremity Diagnosis)** — sourced from the "Articular vs soft tissue" rubric-line description at lines 200–201 ("Does not merely say 'restricted'; identifies whether the barrier is likely joint play, capsule/ligament, muscle/fascia, or mixed."), per the task brief's guidance that this row grades accuracy of the *specific* diagnosis (which structure, which barrier type) rather than the diagnostic *process* graded in row 11.

Every hoverable row's `hook` is an original short mnemonic written to compress the corresponding source-text technique into something sticky (e.g. row 4's "two arm motions map to two different planes of clavicle motion," row 9's "two rows, not one pile of eight bones"), consistent with the `hook` field's purpose in the other two rubrics in this series — none of these are quoted from the source text verbatim beyond the short phrases explicitly noted above.

## Why no images (0 of 9 hoverable rows illustrated)

This build is **entirely text-only** — a deliberate, documented decision, not an oversight. Per the task brief, the Week 7 OMM lecture deck's 68 embedded images were already checked (by figure caption, cross-referenced against `omm7_text.txt`'s slide-title list) and none of them are screening/diagnosis technique photos for the specific rows this rubric grades. They fall into two categories, both out of scope for a screening/diagnosis-only rubric:

1. **Pathology/condition diagrams and clinical imaging** — e.g. rotator cuff tear/impingement imaging, AC separation classification (Rockwood I–VI), carpal tunnel syndrome anatomy, gamekeeper's thumb, boxer's fracture, jersey/mallet finger. This is *clinical-diagnosis* content (LO 9-10A/B/C, "what condition is this and how do you work it up"), not *OMM screening technique* content (LO 8, "how do you physically screen the joint"). The rubric only grades the latter.
2. **OMM *treatment* technique photos** — BLT (first rib, clavicle, scapulothoracic, glenohumeral, wrist), Spencer sequence stages, radial head muscle energy (anterior/posterior), forearm/interosseous-membrane MFR, carpal tunnel Still/FPR, counterstrain (pec minor, radial head, medial epicondyle) — all from LO 11A/B ("OMT Atlas I/II"). These are explicitly out of scope for a *screening/diagnosis* rubric, the same category already excluded from the other two rubrics in this series (e.g. the Axial Spine/Ribs rubric's excluded "Rib Still Arm Arc" and FPR/Still setup photos, and the Lumbar/Pelvis/Sacrum rubric's excluded Still-technique and SI Joint BLT photos).

Two additional images (`omm7_img008.webp`, `omm7_img009.webp`) are literally scans of the paper rubric pages themselves (referenced in the source deck as "Rubric page 4/5 - Upper extremity screening rubric page 1/2") — not usable as illustrative content images, just the source document being digitized.

No substitution was forced. Per this series' established "don't force a bad match" principle (already exercised repeatedly in both prior rubrics' build notes), all nine hoverable rows ship text-only. The Week 7 notes' LO 8 section is detailed enough — a clear step-by-step walkthrough of every joint from SC to fingers, plus a worked Q&A and the articular-vs-soft-tissue rubric language — to carry real teaching content on its own without images.

**This mirrors exactly what happened with the Lumbar/Pelvis/Sacrum rubric before Round 2/3.** That rubric shipped its initial build at 2 of 10 hoverable rows illustrated (mostly text-only, for the same "the lecture deck doesn't have technique photos for this content" reason), and only became fully illustrated (10 of 10) after the user supplied three dedicated *OPP Vol. 1* (UNECOM textbook) chapter PDFs — Sacrum, Lumbar Spine, and Innominates — across two follow-up rounds. **The same thing may well happen here**: if the user supplies an OPP Vol. 1 chapter excerpt covering the shoulder girdle/SC-AC joint, elbow/radial head, or wrist/hand/carpal exam (the textbook series clearly has one, since the Sacrum/Lumbar/Innominates chapters already pulled for the other rubric cross-reference the same book's other regional chapters), this build should get the same re-sourcing treatment: `pdftoppm -r 300 -png` page renders, the PIL content-band auto-cropper already used for the prior rounds, each crop reviewed via the Read tool before being kept, and individual hand-scoped `Edit` calls (never a bulk regex) to add `images:[...]` entries row by row. Flagging this explicitly now so the next conversation turn (or a future Claude session) knows exactly where to start.

## Architecture elements replicated from the reference rubric (confirmed by direct comparison, not assumption)

- Single self-contained HTML + `assets/` folder (created, currently empty), no `index.html` naming.
- `DATA` object keyed by row number 4–12 (the nine hoverable rows only), each with `name`, `purpose`, `hook`, `steps[]`, `normal`, and `images: []` (empty array, matching the reference's explicit-empty-array convention for text-only rows) — `buildContent()` already handles this safely since `d.images && d.images.length` gates the image block.
- Per-row 4-column grading: native `<input type="radio" name="r{n}">` per row, abbreviated `<span class="grade-text">` labels, full original wording preserved as `title=""` on the `<label>`, `.is-na` modifier on N/A cells.
- `table-layout:fixed` with identical `colgroup` widths to the reference (`col.col-grade{width:5.5%}` / `col.col-test{width:78%}`).
- Row numbers as `.row-num-badge` spans, `float:right`, injected as the first child of each description `<td>` — no dedicated row-number column exists anywhere in this file (verified: `td.row-num`/`col-num` selectors return 0 matches; live-DOM `.row-num-badge` count is exactly 14, matching the 14 `<tr data-row>` rows).
- Dual interaction mode: sticky `#sidePanel` at ≥1300px via `showInPanel()`, floating `#popover`/`#overlay` below that via `openPopover()`/`positionPopover()`/`closePopover()`.
- Click-to-enlarge `#lightbox` machinery present and correctly wired (delegated click listener on `#popContent .pop-images img, #sidePanelContent .pop-images img, #readerContent .pop-images img`), even though there are currently zero images to click — ready for a future re-sourcing pass.
- Expand button (`#sideExpandBtn`/`#popExpandBtn`) opening `#readerModal`/`#readerContent` at `zoom:1.35`, tracked via `currentKey`, `#readerModal` at `z-index:1800`. All shared `#popover X, #sidePanelContent X{...}` CSS rules were copied already including the matching `#readerContent X` selector (no regex was run to add them — they were already present in the reference file's finished CSS, copied by hand).
- Text-size control: floating A−/A+ pill, `--font-scale` CSS variable, persisted to `localStorage` under **`omm-upper-extremity-font-scale`** — a new, file-unique key, confirmed different from `omm-axial-ribs-font-scale` and `omm-lumbar-pelvis-sacrum-font-scale`.
- Both historical bugs avoided: `closePopover()` resets `popover.style.display = ''` (not just the `.open` class) — copied verbatim from the reference and re-verified live (see below); the base `#sidePanel{ display:none; }` rule appears before its `@media (min-width:1300px)` override in source order — also copied verbatim and re-verified live.

## On the "don't bulk-regex across the whole file" warning

The task brief flagged the historical bug from the first rubric's build: a regex meant to extend `#sidePanelContent SELECTOR{...}` CSS rules to also match `#readerContent SELECTOR{...}` was once run across the entire file, including the `<script>` block, silently corrupting JavaScript that looked fine in a screenshot but had zero working interactivity (caught only by `node --check`).

This build was written by hand, section by section, copying the reference file's already-correct (post-fix) CSS and JS verbatim and only substituting the row content — no find/replace of any kind was run across the file, so this specific failure mode has no opening here. The verification discipline (`node --check`, brace-count parity, live interaction testing) was still followed in full regardless.

## Verifying

```
cd "Upper Extremity, Screening and Diagnosis OMM Exam"
python3 -m http.server 8795
```

then load `http://127.0.0.1:8795/Upper%20Extremity%2C%20Screening%20and%20Diagnosis%20OMM%20Exam.html`.

This build was verified this way:

- **`node --check` on the extracted `<script>` block: passed cleanly, zero syntax errors.** Brace-count parity checked first as a cheap sanity pass (152 `{` / 152 `}` in the raw file) before the full syntax check.
- Zero console errors on load (checked live via the browser tool, not just visually).
- All 14 `<tr data-row>` rows present; exactly 9 have a `.hoverable` span (rows 4–12) and all 9 have a matching `DATA[key]` entry (keys 4–12), with zero mismatches in either direction.
- `.row-num-badge` count === 14 (confirmed live-DOM, not just a text grep — the raw-file grep count of 15 includes the CSS class-selector definition itself, so the DOM count is the one that matters); zero `td.row-num`/`col-num` elements anywhere in the document.
- Live-DOM spot-check of rows 1, 3, 4, 12, 13, and 14's `.grade-text` labels confirmed each differs from the standard `100%/88%/75%/<75%` pattern exactly as specified: row 3 and row 12 show `100%` (not `100% & Fluid`); rows 13/14 show their own CAP-summary wording (`NO CAP`/`N/A`/`N/A`/`YES CAP` and `YES Done`/`Partial`/`N/A`/`NO`).
- At 1600px width, `getComputedStyle(sidePanel).display === "block"`; at 900px width, `=== "none"`.
- At 900px width (floating-popover mode): simulated a `click` on row 4's `.hoverable` — popover opened (`.open` class present, inline `display:"block"`), closed via the × button (`.open` removed, inline `style.display` reset to `""` — not left at `"block"`), then reopened and closed a second time to confirm no stuck-open state across repeated cycles.
- At 900px width: clicked row 9's `.hoverable` to open the popover, then clicked `#popExpandBtn` — `#readerModal` opened (`zoom:1.35` on `#readerContent`) with the correct row 9 content ("Radiocarpal Joint and Carpal Bone Screening"), then closed cleanly via `#readerCloseBtn` (`.open` removed).
- At 1600px width: hovered row 11's `.hoverable` (`mouseenter`) — confirmed the side panel's placeholder hid, `#sidePanelInner` gained `.has-content`, then clicked `#sideExpandBtn` — `#readerModal` opened with the correct row 11 content ("Most Restricted Somatic Dysfunction — Positional Diagnosis"), including its Memory Hook block (`.pop-hook` present), at `zoom:1.35`.
- Since there are zero images in this build, image-preload verification (done for the other two rubrics) does not apply here — the lightbox/image-click delegation code is present and unchanged from the reference but has nothing to click yet.

## If you want to add images in a future round

Follow the same process used for the Lumbar/Pelvis/Sacrum rubric's Round 2/3 (see that rubric's own `BUILD_NOTES.md` for the full worked example):

1. Get a real source (ideally an OPP Vol. 1 textbook chapter PDF covering shoulder/SC-AC, elbow/radial head, or wrist/hand/carpal exam technique — the lecture deck was already checked and does not have usable screening-technique photos).
2. `pdftoppm -r 300 -png` to render full-resolution page images (beats `pdfimages`, which has fragmented scans in this same textbook series before).
3. Use the PIL content-band auto-cropper approach (scan for near-white gaps to auto-split stacked photos on one page) rather than manually eyeballing every crop box.
4. Visually review every crop via the Read tool before keeping it.
5. Add `images: [{src:"assets/your_file.jpg", caption:"... (Source: ...)"}]` to the relevant row's `DATA` entry via an individual, hand-scoped `Edit` call — never a bulk find/replace across the file.
6. Re-run the full verification pass (`node --check`, live interaction testing, image-preload `naturalWidth > 0` checks) before considering the round done.
