# How this was built

A dev log for future-me (or a future Claude session) picking this back up. Written after the fact from the actual build history, so it should be accurate.

## What this is

An interactive, offline HTML study version of the "2 System Rubric — Cardiovascular, Abdominal, Regional OSE, and Special Tests" PDF (the faculty grading rubric for the OSCE practical). Same rows, same `*`/`P`/`0` and `M`/`NI`/`U` grading columns as the paper rubric, but every test row is interactive: hover (desktop) or tap (touch) shows purpose / step-by-step technique / normal-vs-abnormal findings / reference photos for that specific maneuver.

It's the seventh rubric in this series and was built directly from the six earlier ones plus new source material — see "How the content got in there" below. It's a single self-contained HTML file (`2 System Rubric - ....html`) plus an `assets/` folder of images. No build step, no server, no dependencies — just open the HTML file in a browser.

## How the content got in there

This rubric is roughly half cardiovascular (already fully built in an earlier project) and half abdominal (brand new, from a rich Week 6 study-notes source):

1. **Rows 1–10 and 32–39 (18 rows, all cardiovascular)** — copied directly from `2 System Rubric - Cranial Nerve, Cardiovascular, Regional OSE, and Special Tests` (its rows 10–19 and 27–33/35), including `purpose`/`steps`/`normal` text and images verbatim, with small wording tweaks where this rubric's row text differs (e.g. rows 5–6 here add "One side at a time" to the carotid auscultation/palpation rows — the underlying steps already described one-side-at-a-time technique, so this was just a title/phrasing match, not a content change).
2. **Row 8 (Visual Inspection of the Skin, Trachea, Chest, and Breathing)** — deliberately used the RICHER version of this row from `2 System Rubric - HEENT, Pulmonary, Regional OSE, and Special Tests` (its row 16), which has a fuller normal/abnormal callout and a barrel-chest/flail-chest reference image, instead of the plainer version from the CN/Cardio project. The CN/Cardio project's own BUILD_NOTES flagged this exact mix-up as a mistake made and fixed in the prior build, so this was called out explicitly up front instead of being repeated.
3. **Rows 11–18 and 20–31 (20 rows, all abdominal)** — new content pulled from the Week 6 "Abdominal/GI/GU Clinical Skills" study notes, which had an unusually clean technique/finding/interpretation table covering essentially every special test in rows 20–31, plus labeled diagrams for the 4 quadrants, 9 regions (+ this course's added epigastric/suprapubic), aortic/renal/iliac auscultation sites, liver percussion/palpation landmarks, spleen percussion (Traube's space/Castell sign), and posterior kidneys/CVA anatomy. The exam-sequence language (I-A-P-P: Inspect → Auscultate → Percuss → Palpate) from that source is reflected directly in the row ordering and step text for rows 11–18.
4. **Row 19 (Lumbar Spine OSE)** — the Week 3 MSK notes were checked for lumbar-specific segmental-diagnosis technique and, as expected, only had a one-line category heading ("screen symmetry, palpate TART, and diagnose L1–L5 with neutral/flexion/extension mechanics") with no further detail — the same situation the CN/Cardio project hit for its Thoracic Spine row. This row reuses that project's `fallback` pattern verbatim, reworded for lumbar/L1-L5 instead of thoracic/T1-T12.
5. **Gap-filling with open-licensed images** — for special-test rows without a dedicated photo in the Week 6 notes (the appendicitis cluster and some ascites tests), Wikimedia Commons was searched for open-licensed diagrams. This found a strong match for McBurney's point (exact anatomical landmark diagram) and for shifting dullness/central tympany (a clean before/after percussion diagram used for both of those two rows, since they're sequential steps of the same maneuver). A psoas-muscle anatomy dissection photo was also found and considered for the Psoas Sign row, but rejected as too cluttered/tangential to be a genuinely useful reference — better to leave that row text-only than force a bad match (see "Known remaining gaps" below).

Every image caption ends with a short `(Source: ...)` note — not a legal notice, just so it's traceable later if a citation is ever needed or an image needs replacing.

## Row-by-row source breakdown

- **18 rows** (1–10, 32–39) — reused directly from the CN/Cardio project, all with their original images.
- **1 row** (8) — reused from the HEENT/Pulm project (richer chest-inspection version), with its image.
- **12 rows** (11–18, 27, 28, 30) — new content from the Week 6 Abdominal/GI notes, each with at least one matched image from that source.
- **1 row** (23, McBurney's Point) — new content from Week 6 notes, illustrated with an open-licensed Wikimedia Commons image (the Week 6 notes themselves are text-only for this specific test).
- **7 rows** (20, 21, 22, 24, 25, 26, 29, 31 — rebound tenderness, heel strike, Rovsing's sign, psoas sign, obturator sign, Murphy's sign, ventral hernia, bimanual kidney palpation) — new content from Week 6 notes, text-only. A web search was done for each of these (per the build brief) but nothing suitable turned up: Rovsing's/Murphy's/obturator sign have essentially no open-licensed technique diagrams available, and the one psoas-related image found (a labeled femoral-triangle cadaver dissection) was rejected as a poor pedagogical fit rather than forced in.
- **1 row** (19, Lumbar Spine) — no matching source content anywhere (same situation as the CN/Cardio project's Thoracic Spine row) — uses the `fallback` red-banner pattern.

So of the 20 new abdominal rows, 13 ended up with an image and 7 (all special tests, mostly the appendicitis cluster) are text-only.

## How the interactivity works

Everything lives in one `<script>` block at the bottom of the HTML — this is unchanged from the earlier six rubrics in this series:

- **`DATA`** — an object keyed 1–39 (matches the rubric row numbers), each with `name`, `purpose`, `steps[]`, `normal`, and optionally `images[]` (`{src, caption}`) or `fallback` (used only for row 19, Lumbar Spine OSE/TART).
- **`buildContent(key)`** — turns one `DATA` entry into the HTML shown in a popover/panel.
- Two display modes, picked automatically by viewport width:
  - **≥1300px (side-panel mode)**: a sticky panel docked to the right of the rubric (`#sidePanel`) shows the content directly — hovering a row just swaps `#sidePanelContent`'s innerHTML in place.
  - **<1300px (floating-card mode)**: a floating popover (`#popover`) positioned near the hovered/tapped row via `positionPopover()`, with a semi-transparent `#overlay` to catch outside clicks.
- **Click-to-enlarge**: any image in either mode opens in a full-screen `#lightbox` overlay.
- Touch detection is `matchMedia('(hover: none)')`.

### Known bugs from the original build — verified NOT reintroduced here

Two real bugs were found and fixed during the first (CN/Cardio) build of this rubric series. Both were checked explicitly in this build:

1. `closePopover()` must reset `popover.style.display = ''` (otherwise the inline `display:block` set by `positionPopover()` for measurement purposes permanently overrides the CSS that's supposed to hide the popover again after the first open). Confirmed present at the bottom of `closePopover()`.
2. The base `#sidePanel{ display:none; }` CSS rule must come BEFORE its `@media (min-width:1300px){ #sidePanel{ display:block; } }` override in source order (equal-specificity selectors mean source order decides the winner). Confirmed correct order in this file.

## If you want to add/fix a row

1. Find the row's entry in the `DATA` object (search for its row number, e.g. `19: {`).
2. Edit `purpose` / `steps` / `normal` as plain strings.
3. To add a photo: drop the image file in `assets/` (descriptive lowercase-with-underscores filename), then add `images: [{src:"assets/your_file.jpg", caption:"... (Source: wherever)"}]` to that row's object.
4. Verify with a real local server if testing via `file://` looks unreliable: `python3 -m http.server` from inside the folder, then load `http://127.0.0.1:PORT/`.

## Known remaining gaps (no photo, text-only)

- Row 19 — Lumbar Spine OSE/TART (also has no matched *source text* — flagged in the UI with the red fallback banner)
- Row 20 — Rebound Tenderness x4 Quadrants
- Row 21 — Heel Strike BL
- Row 22 — Rovsing's Sign (no open-licensed technique diagram found; the LLQ-anatomy image found was judged too tangential to the actual maneuver to be worth including)
- Row 24 — Psoas Sign (a labeled femoral-triangle cadaver dissection photo was found and considered, but rejected — iliopsoas was one small label among ~15 others, not a clear or useful reference for this specific test)
- Row 25 — Obturator Sign
- Row 26 — Murphy's Sign
- Row 29 — Ventral Hernia screen
- Row 31 — Bimanual Kidney Palpation

If you find good images for these later, same procedure as above.
