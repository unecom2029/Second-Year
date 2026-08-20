# How this was built

A dev log for future-me (or a future Claude session) picking this back up. Written after the fact from the actual build history, so it should be accurate.

## What this is

An interactive, offline HTML study version of the "Axial Spine and Ribs, Screening and Diagnosis OMM Exam 26-27" rubric (the faculty grading rubric for the OMM skills-test practical). Every screening/diagnosis test row is interactive: hover (desktop) or tap (touch) shows purpose / step-by-step technique / diagnosis-naming logic / reference photos for that row.

It's a single self-contained HTML file (`Axial Spine and Ribs, Screening and Diagnosis OMM Exam.html`) plus an `assets/` folder of images. No build step, no server, no dependencies — just open the HTML file in a browser (or serve the folder for the most reliable local preview — see "Verifying" below).

This is the first of five related OMM rubrics being built from the same source PDF (the other four — Lumbar Spine/Pelvis/Sacrum, Upper Extremity, Lower Extremity, and a treatment-technique rubric — are separate future builds). It was made by copying the architecture of the OCS rubric tools almost line-for-line (same CSS, same JS interaction logic, same two historical bugs already fixed and carried forward — see "Bugs to avoid" below), with one deliberate structural change: **per-row 4-column grading instead of a single global */P/0 legend** (see next section).

## The big structural difference from the OCS reference rubrics

The OCS rubrics (Musculoskeletal-Shoulder, Cranial Nerve/CV, etc.) all used one uniform 3-column `*`/`P`/`0` legend for every gradable row, printed once at the top of the table. **This rubric is different**: the source PDF prints **4 grading columns per row, and the column text itself varies row to row** — most rows read `100% Correct and Fluid | 88% Correct | 75% Correct | Less than 75% Correct — Must CAP Line`, but:

- The **Washes Hands** row only has 2 real options — `100% Correct` and `Less than 75% Correct...` — with the middle two columns printed as `N/A-DO NOT SELECT`.
- The two **CAP summary rows** at the bottom (rows 10–11) each have their own completely different 4-option wording (`NO, DOES NOT need to CAP` / ... / `YES, DOES need to CAP`; and `YES, CAP was completed successfully` / `Partially Completed...` / `N/A- SELECT IF STUDENT DID NOT HAVE TO CAP` / `NO, CAP was NOT completed successfully`).

Collapsing this to one shared legend (the OCS pattern) would have silently discarded real information — a grader reading only a generic `*/P/0` legend has no way to know that a given row's 3rd option is literally "N/A-DO NOT SELECT" rather than "75% correct". So instead of a `.grade-box` class of plain checkboxes with one legend block, each row got:

- **Its own 4 `<td class="grade-cell">` cells**, each containing a native `<input type="radio">` (grouped by a per-row `name="r{n}"` so the browser enforces single-select for free — no custom JS needed the way the OCS checkbox rows needed a manual "uncheck siblings" listener) plus a `<span class="grade-text">` holding that row's **exact column wording** in small caption text under the radio.
- A `.is-na` modifier class on any cell whose text is literally `N/A-DO NOT SELECT` (or the CAP-row equivalent `N/A- SELECT IF STUDENT DID NOT HAVE TO CAP`), which gives it a light grey background and italic label — so an N/A cell is visually distinguishable from a real scoring option at a glance, without hiding or removing it (the source rubric does print it as a literal column, so it stays clickable/selectable like the others; it's just visually deprioritized).
- The enlarged-tap-target behavior from the OCS build (tapping anywhere in the cell toggles the radio, good for iPad) was kept, adapted to `.grade-cell` / `input.grade-box` instead of `.col-check` / checkbox.
- A `.grading-note` block at the top of the page (replacing the OCS `.grading-key` block) explains this per-row-label structure in plain English up front, since it's a real behavioral difference from what a "grading key" table implies.

This was the main new engineering risk in the build (per the task brief) and it works cleanly: verified by pulling the rendered page text and confirming row 1 and row 3 print different column wording, and that rows 10–11 each print their own distinct 4-option sets (see "Verifying" below for how this was checked).

No student-name/date header fields were added — the source PDF for this rubric doesn't have them (unlike the OCS rubrics), so none were invented.

## How the content got in there

1. **Rubric skeleton (all 11 rows, exact wording, exact per-row column labels)**: transcribed directly from the OMM Week 1 course-notes source file, which — usefully — contains a plain-text extraction of the actual rubric PDF (the "Axial Spine and Ribs, Screening and Diagnosis OMM Exam 26-27" table appears verbatim partway through that notes file, alongside the other four related OMM rubrics). This let the row text and column labels be checked directly against the source rubric text rather than only against the task's paraphrase of it.
2. **Rows 4–9 popover content (purpose / how-to-perform / diagnosis-naming logic)**: sourced primarily from the Week 1 OMM notes' "Perform Axial Spine, Ribs, Pelvis, and Sacrum Screening Exams" section and its "LO2 · Axial Spine & Rib Screening Detail" table — OA/AA/lower-cervical contact and coupling rules, the rib-by-rib (Rib 1 / Ribs 2-4 / Ribs 5-10 / Ribs 11-12 / mechanical ribs) contact-and-diagnosis-logic table, and the Fryette Type I/Type II naming rules ("LO3 · Fryette Type I vs Type II" and the worked examples in "LO3 · Type I/II Comparison & Worked Examples"). This file has zero embedded images but is the most detailed technique text available.
3. **Rows 4–9 reference images**: sourced from the Week 2 OMM lecture-slide file (FPR/Still/ribs/radiculopathy deck), which has real course-slide photos and diagrams with descriptive alt text. Each image was viewed directly (not just alt-text-matched) before use to confirm it actually shows what its alt text claims — see the per-row list below.

Every image caption ends with a short `(Source: ...)` note for traceability, matching the OCS-rubric convention.

## Row-by-row image sourcing (rows 4–9, the only rows with popovers)

- **Row 4 (Head/Cervical Spine Screening)** — `cervical_screen_seated.jpg` ("Cervical Screen" slide): seated cervical segmental translation screen. Direct, clean match.
- **Row 5 (Head/Cervical Spine Segmental Diagnosis)** — two images:
  - `atlantoaxial_no_joint.jpg` (slide titled "Atlantoaxial Motion", originally alt-tagged "OA and AA Anatomy" in the source deck — the alt text is a bit of a misnomer since the slide is really about AA motion specifically, not gross anatomy, but its content — the "OA is the yes joint / AA is the no joint" framing, ~50% of cervical rotation at AA, minimal AA flexion/extension/sidebending — is exactly the fact base needed to justify why AA is diagnosed by rotation alone. Captioned to describe what the slide actually shows rather than trusting the alt text.
  - `lower_cervical_uncovertebral_joints.jpg` ("Lower Cervical Mechanics" slide, actual slide title "Lower Cervical Unit Motion (C2-C7)"): anatomical diagram of the uncovertebral (Luschka) joint, which is exactly why lower-cervical sidebending/rotation coupling isn't "true" Fryette mechanics per the Week 1 notes. Strong match.
- **Row 6 (Thoracic Spine Screening + thoracic outlet)** — `thoracic_lumbar_screen_seated.jpg` ("Thoracic/Lumbar Screen" slide): seated segmental screen with shoulder compression + monitoring hand. Good match for the vertebral half of the row; see "Known gap" below for the thoracic-outlet half.
- **Row 7 (Thoracic Spine Segmental Diagnosis + thoracic outlet)** — `managing_seated_torso.jpg` (slide titled "Managing the Patient's Torso", alt-tagged "Seated Torso Management" in the deck): shows how to localize/compress through the seated patient's torso (axilla weight-drop, arm-across-chest for F/E, weight-drop + translation for sidebending) — this is the general hands-on skill underlying the 3-position diagnostic test, which is why it was placed on the diagnosis row rather than the screening row.
- **Row 8 (Rib Cage Screening)** — `rib_angle_screen_seated.jpg` ("Rib Screen" slide): same seated setup as the thoracic screen with the monitoring hand moved to the rib angles. Direct match.
- **Row 9 (Rib Cage Diagnosis)** — `anterior_vs_posterior_rib_model.jpg` ("Anterior vs Posterior Rib" slide): a physical rib model photographed to show the anterior-subluxation vs. posterior-subluxation positional difference described in the Week 2 notes' mechanical-rib table. Direct, unambiguous match — this is a rib bone model, not a patient photo, so there's no consent/identifiability concern.

Two Week 2 images that also touch ribs — "Rib Still Arm Arc" (appears twice in the deck) and the FPR/Still setup photos ("FPR Neutral/Idling", "Cervical FPR Setup", "Still Technique Setup") — were deliberately **not** used here even though they're in the same source file: they're treatment-technique photos (how to *treat* a rib/cervical dysfunction with Still or FPR), not screening/diagnosis photos, and this rubric is screening/diagnosis only. They belong to the future OMM Treatment rubric build instead.

All 7 images used here were originally `.webp` in the extracted asset set and were converted to `.jpg` with macOS `sips` to match the OCS-rubric asset convention (`sips -s format jpeg <in>.webp --out <out>.jpg`); `cwebp`/`ffmpeg`/`imagemagick` were not available in this environment, but `sips` handled the conversion natively without quality loss worth worrying about for this use case.

## Known gap: thoracic outlet has no dedicated image

Rows 6 and 7 explicitly grade "the thoracic outlet" alongside the thoracic spine (`Effectively segmentally screens the entire thoracic spine (T1-T12) AND the thoracic outlet...`). The Week 1 notes cover this region under the name **thoracic inlet** (same anatomical space — the costoclavicular junction bounded by rib 1, the clavicle, and the manubrium — "outlet" and "inlet" are used interchangeably across sources for this junction depending on whether you're emphasizing the neurovascular exit from the neck or the entrance to the thorax), giving a naming rule (`Inlet SrRl` — sidebending and rotation tested and named independently, not assumed coupled) but no photo. Neither Week 1 nor Week 2 source material had a clean, unambiguous photo specifically illustrating thoracic-outlet/inlet screening or diagnosis technique (as opposed to the general vertebral thoracic screen, which is well illustrated). Rather than force a mismatched image onto that half of rows 6–7, the thoracic-outlet naming/testing rule is covered in text only within those rows' popovers, and this gap is called out explicitly in-page (in row 6's "Normal vs. Abnormal / Accuracy" callout) so a student using this tool isn't misled into thinking the photo shown covers the outlet too. If a good thoracic-outlet-specific photo turns up later (from a future course-notes file, e.g. the Upper Extremity OMM rubric's source material may have thoracic-outlet-syndrome content worth checking), add it to rows 6–7 following the "If you want to add/fix a row" steps below.

## How the interactivity works

Same architecture as the OCS rubric tools — everything lives in one `<script>` block at the bottom of the HTML:

- **`DATA`** — an object keyed 4–9 (only the rows with popover content; rows 1–3, 10, 11 are plain rows with no `.hoverable` span and no DATA entry, same treatment as the OCS rubrics' plain professionalism rows), each with `name`, `purpose`, `steps[]`, `normal`, and optionally `images[]` (`{src, caption}`).
- **`buildContent(key)`** — turns one `DATA` entry into the HTML shown in a popover/panel (purpose, steps list, normal/accuracy callout, image thumbnails). Identical to the OCS version, just with the "Normal vs. Abnormal" label renamed to "Normal vs. Abnormal / Accuracy" since these rows are graded on diagnostic accuracy rather than a normal-vs-abnormal exam finding.
- Two display modes, picked automatically by viewport width:
  - **≥1300px (side-panel mode)**: a sticky panel docked to the right of the rubric (`#sidePanel`) shows content directly — hovering a row just swaps `#sidePanelContent`'s innerHTML in place. No positioning, nothing opens or closes.
  - **<1300px (floating-card mode, used on tablets/phones and narrow windows)**: a floating popover (`#popover`) positioned near the hovered/tapped row via `positionPopover()`, with a semi-transparent `#overlay` to catch outside clicks.
- **Click-to-enlarge**: any image in either mode opens in a full-screen `#lightbox` overlay (dark backdrop, tap/click outside or the × to close).
- Touch detection is `matchMedia('(hover: none)')` — real touch devices get tap-only behavior; anything with a mouse gets hover behavior in whichever display mode applies.
- **Grading inputs differ from the OCS build**: native `<input type="radio">` grouped by a per-row `name` instead of `<input type="checkbox">` with a manual "uncheck siblings" JS listener. Radios give single-select-per-row behavior for free from the browser, so that whole chunk of OCS JS (`document.querySelectorAll('input.grade-box').forEach(cb=>{...})`) was simplified away; only the enlarged-tap-target click handler (`td.grade-cell` click → `checked = true` → dispatch `change`) was kept, since radios need an explicit click on a coordinate inside the `<input>` itself by default.

### Bugs to avoid (carried forward from the OCS builds — do not reintroduce)

1. **`closePopover()` must reset `popover.style.display = ''`.** `positionPopover()` sets an inline `display:block` on the popover to measure its size before positioning it. If `closePopover()` only removes the `.open` class and doesn't also clear that inline style, the popover never actually hides again after the first time it opens — it looks like "the × button doesn't work." Verified fixed in this build: `closePopover()` does `popover.style.display = '';` right after removing `.open`, and this was specifically re-tested via JS (open → close via × button → reopen → close again) to confirm no stuck-open state across repeated cycles.
2. **CSS source order for `#sidePanel`.** The base `#sidePanel{ display:none; }` rule and the `@media (min-width:1300px){ #sidePanel{ display:block; } }` override have equal specificity (both plain `#sidePanel`), so the base rule **must come before** the media-query block in the stylesheet, or the base rule wins regardless of viewport width and the panel never shows. Verified in this build by checking `getComputedStyle(sidePanel).display` at both a 900px-wide viewport (returned `"none"`) and a 1600px-wide viewport (returned `"block"`).

## If you want to add/fix a row

1. Find the row's entry in the `DATA` object (search for its row number, e.g. `7: {`). Only rows 4–9 have entries; rows 1–3/10/11 are intentionally plain.
2. Edit `purpose` / `steps` / `normal` as plain strings (double-quoted; escape any literal double quotes).
3. To add a photo: drop the image file in `assets/` (descriptive lowercase-with-underscores filename), then add `images: [{src:"assets/your_file.jpg", caption:"... (Source: wherever)"}]` to that row's object.
4. If you need to change a row's *grading labels* (not its popover content), edit the four `<td class="grade-cell">` blocks directly in the HTML table for that `<tr data-row="N">` — each cell's visible text lives in its `<span class="grade-text">`, and whether a cell should render as N/A-shaded is controlled by adding/removing the `is-na` class on that `<td>`.
5. Serve the folder locally and load it over `http://` to check (see below) rather than trusting `file://`.

### Verifying (file:// can be unreliable)

```
cd "Axial Spine and Ribs, Screening and Diagnosis OMM Exam"
python3 -m http.server 8793
```

then load `http://127.0.0.1:8793/Axial%20Spine%20and%20Ribs%2C%20Screening%20and%20Diagnosis%20OMM%20Exam.html` (URL-encode the spaces/comma, or just navigate a browser UI to the folder listing and click the file).

This build was verified this way, mostly via direct JS execution against the live page (more reliable than trusting screenshots, per the lesson recorded in the OCS rubrics' own build notes):

- Zero console errors on load.
- All 11 `<tr data-row>` rows present; exactly 6 have a `.hoverable` span (rows 4–9) and all 6 have a matching `DATA[key]` entry; the 5 plain rows (1, 2, 3, 10, 11) have none.
- Pulled the rendered page text and confirmed row 1 and row 3 print genuinely different 4-option label sets, and that rows 10 and 11 each print their own distinct label sets — the core new-architecture risk for this build.
- At 1600px width, `getComputedStyle(sidePanel).display === "block"`; at 900px width, `=== "none"`.
- Simulated a `mouseenter` on row 4's `.hoverable` and confirmed the side panel's placeholder hid, its content updated to the Head/Cervical Spine Screening entry, and it rendered exactly 1 `<img>`.
- At 900px width: clicked row 9's `.hoverable` to open the floating popover (`display:block`, `.open` class present), clicked the × close button (`.open` removed, `display:none`, and — critically — the popover's *inline* `style.display` was confirmed reset to `""`, not left at `"block"`), then reopened and closed it a second time to confirm no stuck-open state.
- Clicked an image inside the open popover and confirmed the lightbox opened with the correct `src`, then confirmed the × button closed it.
- Preloaded all 7 image `src` values referenced across the `DATA` object as `new Image()` objects and confirmed every one resolved `onload` with `naturalWidth > 0` (900–1100px wide each) rather than `onerror`.
- Tested the enlarged tap-target behavior: clicking a `td.grade-cell` (not directly on the `<input>`) correctly checks that cell's radio and — because same-row radios share a `name`, verified natively by the browser — unchecks any previously-selected option in that row.

## Rows to double-check for accuracy

- **Row 5's "OA and AA Anatomy" image** — the source deck's alt text calls it "OA and AA Anatomy" but the slide itself is titled "Atlantoaxial Motion" and its content is entirely about the AA joint's rotation-dominant behavior (the "no joint" framing), not a combined OA+AA anatomy diagram. The caption used in this build describes the slide's actual content rather than repeating the (slightly misleading) alt text — worth a second look if a cleaner combined OA/AA anatomy diagram turns up later.
- **Rows 6–7's thoracic-outlet coverage** — text-only for the outlet-specific half of each row; see "Known gap" above.
