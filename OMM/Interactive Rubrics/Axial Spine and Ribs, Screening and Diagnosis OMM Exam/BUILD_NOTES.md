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

## Round 2: user-requested refinements (post-launch polish pass)

After the initial build shipped, the user asked for four follow-up changes in two rounds. These became the template for every later rubric in the series, so they're documented in detail here.

### 1. Shrink the 4 grading columns

The first version's grading columns were too wide — `table.rubric` wasn't using `table-layout:fixed`, so the browser sized columns by content instead of respecting the `colgroup` widths, and the long labels (`Less than 75% Correct — Must CAP Line`) forced every grading column to stretch. Fix, in two passes:
1. Add `table-layout:fixed` to `table.rubric`, and rebalance `colgroup` widths (grading columns went from ~25% each down to ~8.5%, then down again to ~5.5% in the second pass).
2. **Abbreviate the on-screen label text** (`"100% Correct and Fluid"` → `"100%<br>& Fluid"`, `"N/A-DO NOT SELECT"` → `"N/A"`, etc.) while preserving the full original wording as a `title` attribute on the `<label>` — so the abbreviation is a pure display optimization, not a loss of information (hovering/long-pressing the cell still shows the full text). This was done with a single Python regex pass over the whole file (`<label><input .../><span class="grade-text">FULL</span></label>` → `<label title="FULL"><input .../><span class="grade-text">SHORT</span></label>`) rather than 44 manual edits.

Net effect: grading columns now take ~22% of the table combined (down from ~100% in the original broken version), description column got the reclaimed space.

### 2. Add memory hooks / plain-language explanations

Each of the 6 `DATA` entries (rows 4–9) got a new `hook` field — a short, sticky, plain-English explanation distinct from the clinical `steps`/`normal` text (e.g. "OA nods 'yes' ... AA shakes 'no'", "Pump handle up top, bucket handle down low"). Rendered via `buildContent()` as a `🧠 Memory Hook` labeled callout (`.pop-hook`, gold-tinted box) positioned right after `Purpose` and before `How to Perform` — the idea being: give the reader the sticky mental model *before* the detailed steps, not buried after them. This is purely additive; the original `purpose`/`steps`/`normal` fields were not shortened or replaced to make room for it.

### 3. Add a text-size control

A floating A−/A+ pill, fixed bottom-right (`.floating-stack`), scales `document.documentElement`'s font-size via a `--font-scale` CSS custom property (`html{ font-size: calc(16px * var(--font-scale)); }`). Since virtually every font-size in the stylesheet is in `rem`, this one variable scales the whole page — table, grading labels, and popover/side-panel content — together. Persisted per-file in `localStorage` under a unique key (`omm-axial-ribs-font-scale`) so it doesn't collide with the other rubrics' scale settings if they're open in the same browser. Range clamped to 0.85×–1.6×.

### 4. Re-sourced rows 5 and 9 from the actual OPP textbook, plus a row-number layout fix and an "expand to full-size popup" button

The user supplied two more PDF excerpts directly from *Osteopathic Practices and Principles Vol. 1* (Cervical Spine and Ribs chapters) and asked for the content/images to be pulled from them. **Important gotcha hit during this step: the two PDF files' names were swapped relative to their content** — `rubs.pdf` (8 pages) was actually the *Ribs* chapter, and `OPP_UNECOM_Yr1_2025.pdf` (6 pages) was actually the *Cervical Spine* chapter. Always verify with `pdftotext -f N -l N file.pdf -` on a page or two before trusting a filename.

- Extracted real page renders with `pdftoppm -r 300 -png` (not `pdfimages`, which fragmented these particular scans into unusable partial-color-channel pieces), then cropped the individual technique photos out with PIL, scaling crop-box coordinates by the same factor used when eyeballing the rendered pages. Result: 10 new clean, unlabeled photos (no textbook captions baked in) — OA lateral translation test, AA rotation test, lower cervical diagnosis, an occipital-condyle anatomy shot, superior 1st rib subluxation test, rib 2-10 anterior/posterior subluxation screen, and 4 respiratory rib-motion technique photos (rib 1, pump-handle 2-5, bucket-handle 6-10, caliper 11-12).
- **Row 5** was rewritten from a generic paraphrase into the textbook's actual Position/Action/Results structure for OA, AA, and lower cervical, including its own worked examples (`OA FSlRr`, `C4 ESRr`, `C6 FSRl`) — now has 4 images.
- **Row 9** got a full structural-vs-respiratory rewrite (5mm unleveling criterion for the 1st-rib test, per-rib-group hand positions, the "locked up / locked down" naming mnemonic) — now has 6 images.
- **Row 8** gained one additional image (the ant/post subluxation screening photo).

While making room for all this new photo/text volume, two more layout requests came in:
- **Row numbers moved out of their own column.** They used to live in a dedicated `<td class="row-num">`, which — combined with `vertical-align:middle` and a row height set by the long description text — made each number float alone in a tall, mostly-empty box (visually awkward, and wasted table width). Fixed by deleting the `row-num` column entirely (reclaiming its width into the description column) and instead rendering the number as a small rounded `.row-num-badge` `<span>`, `float:right`, injected as the *first* child inside the description `<td>` — so it sits in the top-right corner of the cell and the row's text wraps around it below/left, instead of owning a whole column. (The user's original ask was actually to move the numbers to the *left* side instead — noted here for whoever picks this up next, but they said not to bother changing it again, so the right-corner-badge version stands.)
- **"Expand to full-size popup" button.** A small circular `+` button now sits in the corner of both the side panel (`#sideExpandBtn`) and the floating popover (`#popExpandBtn`). Clicking it opens the *same* `buildContent()` HTML for whichever row is currently active (tracked in a new `currentKey` variable, set inside `showInPanel()`/`openPopover()`) inside a new large centered modal (`#readerModal` / `#readerContent`), rendered at `zoom:1.35` — a simple, pragmatic way to scale an entire subtree (text *and* images together) without duplicating every font-size rule for a second context. `z-index:1800`, deliberately between the popover (1000) and the lightbox (2000), so clicking a photo inside the expanded reader still opens the full image lightbox on top of it. The image-click delegation selector and all the shared `#popover X, #sidePanelContent X{...}` CSS rules had to be extended to also match `#readerContent X` so the same generated HTML looks right in all three containers.

**A real bug was introduced and caught during this pass, worth flagging for future edits of this style:** the Python regex used to extend those shared CSS selectors (`#sidePanelContent (SEL)\{` → add `, #readerContent (SEL)\{`) was run across the *entire file*, including the `<script>` block. One JS line ended in `...img');` with no immediately-following `{` on that logical statement — so the regex's non-greedy-but-still-`{`-seeking `[^{]+?` kept scanning *forward across many lines* until it found the next real `{` (inside a later arrow function), swallowing several lines of real JavaScript into its "selector" capture group and corrupting them. This silently produced a page that looked fine in a screenshot (no visual sign of a JS syntax error) but had zero working interactivity. **Caught by running `node --check` against the extracted `<script>` contents before declaring the change done** — not by screenshotting. Lesson: any regex/find-replace that spans "from a known start marker to the next occurrence of a common character like `{`" needs either a tighter, safer anchor (e.g. require the `{` on the *same line*) or a full syntax-check pass afterward, especially when it's being run across a mixed HTML+CSS+JS file rather than a single-language one.

### Verifying this round

Same "don't trust a screenshot alone" discipline as the original build, extended with an actual JS syntax check:
- `node --check` (or `new Function(scriptSource)`) on the extracted `<script>` contents — this is what caught the regex-corruption bug above; a visual screenshot alone would not have.
- Confirmed brace-count parity (`{` count === `}` count) in the raw file as a cheap first-pass sanity check before the full syntax check.
- Live-clicked through: `.row-num-badge` count === 11, zero leftover `.row-num`/`col-num` references; the expand button on both the side panel and the popover opens `#readerModal` with the correct `currentKey`'s content, correct image count, and `zoom:1.35` applied; closing via the reader's own × button clears `.open`; all 15 total images (7 original + a few reused/renamed during the re-sourcing pass) preload with `naturalWidth > 0`.
