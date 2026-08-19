# How this was built

A dev log for future-me (or a future Claude session) picking this back up. Written after the fact from the actual build history, so it should be accurate.

## What this is

An interactive, offline HTML study version of the "2 System Rubric — Cardiovascular, Pulmonary, Regional OSE, and Special Tests" PDF (the faculty grading rubric for the OSCE practical). Same rows, same `*`/`P`/`0` and `M`/`NI`/`U` grading columns as the paper rubric, but every test row is interactive: hover (desktop) or tap (touch) shows purpose / step-by-step technique / normal-vs-abnormal findings / reference photos for that specific maneuver.

It's a single self-contained HTML file (`2 System Rubric - ....html`) plus an `assets/` folder of images. No build step, no server, no dependencies — just open the HTML file in a browser. Everything (CSS, JS, and the content data) lives inline in that one file except the images.

This is the **sixth** rubric built in this series, and by far the fastest — see "How the content got in there" below.

## How the content got in there

Unlike the earlier five rubrics (which needed real content extraction from course notes plus web research for gaps), this one is ~97% pure reuse. Every organ-system tested here — cardiovascular and pulmonary — was already fully built out, with matched instructional text and reference photos, in two earlier projects in this same folder:

- `2 System Rubric - Cranial Nerve, Cardiovascular, Regional OSE, and Special Tests/` (the CV rows)
- `2 System Rubric - HEENT, Pulmonary, Regional OSE, and Special Tests/` (the pulmonary rows)

1. **Rubric skeleton**: transcribed by hand from the new PDF — 31 gradable rows across Cardiovascular Systems Exams, Pulmonary System Exams, OSE TART/Boney Regional Testing, and Special Tests, plus the 6-item Communication/Professionalism/Patient Care section (note this rubric's header is "Communication, Professionalism, and Patient Care" — worded slightly differently from the earlier rubrics' "Communication and Professionalism").
2. **30 of 31 rows copied directly** from the two source projects' `DATA` objects — `purpose`, `steps`, `normal`, and `images` entries copied verbatim (row-label wording adjusted only where this rubric's PDF phrasing differed trivially from the source, e.g. "Palpates the Carotid Pulses" vs. the source's "Palpate the Carotid Pulses"). Row 15 (Thoracic Spine OSE/TART) carries over the `fallback`/no-source red-banner treatment unchanged from the CN/Cardio project — it never had a matched source there either.
3. **Row 30 is the only row that needed new work.** The new rubric asks for "Palpates for Head/Neck, Supraclavicular, Infraclavicular, & Axillary Lymphadenopathy BL" — broader than the HEENT/Pulm project's row 11 ("Palpates for Head, Cervical, and Supraclavicular Lymphadenopathy BL"), which doesn't mention infraclavicular or axillary nodes at all. Used HEENT/Pulm row 11 as the base (`purpose`/`steps`/`normal`/its lymph node image), then added two new `steps` describing infraclavicular (apical, deltopectoral groove) and axillary (arm supported, sweep into the axilla checking central/anterior/posterior/lateral groups) palpation using standard technique, and expanded `normal` to mention axillary drainage territory.
4. **Row 30's second image** came from a Week 7 OCS notes file (`OCS/Week 7/Sensitive_Exams_Lymph_Nodes_LO_Organized_Transcript_Enhanced_with_Exam_Popups.html`, "Sensitive Exams, STIs, Breast, GU, and Lymph Nodes") that hadn't been used in any of the five prior rubric builds. That file is ~6 MB because of embedded base64 images, so it was processed the same way as other week-notes files in earlier builds: a small Python script (`strip_images.py`, run from the OS scratchpad, not saved in this repo) regex-matched `data:image/...;base64,...` blobs, decoded each to its own file, and replaced them with `[[IMAGE:filename]]` placeholders in a stripped copy of the HTML so the surrounding text could be read without loading huge blobs into context. One of the decoded slides (a breast-exam lecture slide, "Breast exam Continued...") contained a labeled anatomical diagram of the axillary/infraclavicular/supraclavicular lymph node groups (lateral, central, posterior/subscapular, anterior/pectoral, apical/infraclavicular, supraclavicular) with drainage arrows. That diagram was cropped down to just the illustration (Pillow, installed via `pip3 install --user pillow` since neither ImageMagick nor `PIL` were already available) and saved as `assets/axillary_infraclavicular_node_groups.png`.
5. **One deliberate deviation from the literal source-mapping instructions, worth flagging**: row 8 ("Visual Inspection of the Skin, Trachea, Chest, and Breathing") was mapped to the CN/Cardio project's row 17, which is text-only (purpose + steps, no image, no `normal`) — a known documented gap in that project's own BUILD_NOTES. The HEENT/Pulm project's equivalent row 16 for the *identical* maneuver actually has both a `normal` block and a reference image (`chest_inspection_barrel_flail.png`, barrel chest / flail chest). Per the explicit row-by-row source mapping given for this build, CN/Cardio row 17 was used as specified, so row 8 in this rubric is text-only (no image, no normal/abnormal callout) even though a richer version of the same content exists one folder over. If this rubric gets revisited, swapping in the HEENT/Pulm version (and copying `chest_inspection_barrel_flail.png` into `assets/`) would be a trivial, worthwhile upgrade.

Every image caption ends with a short `(Source: ...)` note — not a legal notice, just so it's traceable later if a citation is ever needed or an image needs replacing. These captions were carried over unchanged from whichever source project the image came from.

## How the interactivity works

Identical architecture to the other five rubrics in this series — copied verbatim except for content:

- **`DATA`** — an object keyed 1–31 (matches the rubric row numbers), each with `name`, `purpose`, `steps[]`, `normal`, and optionally `images[]` (`{src, caption}`) or `fallback` (row 15 only, Thoracic OSE/TART — flagged with a red "no exact source match" banner in the UI via the `no-source` CSS class).
- **`buildContent(key)`** — turns one `DATA` entry into the HTML shown in a popover/panel.
- Two display modes, picked automatically by viewport width:
  - **≥1300px (side-panel mode)**: a sticky panel docked to the right of the rubric (`#sidePanel`) shows content directly — hovering a row just swaps `#sidePanelContent`'s innerHTML in place. No positioning math, nothing opens or closes.
  - **<1300px (floating-card mode)**: a floating popover (`#popover`) positioned near the hovered/tapped row via `positionPopover()`, with a semi-transparent `#overlay` to catch outside clicks.
- **Click-to-enlarge**: any image opens in a full-screen `#lightbox` overlay.
- Touch detection is `matchMedia('(hover: none)')`.

### Two known bugs from the original (CN/Cardio) build — both already fixed here, do not reintroduce

1. `closePopover()` must reset `popover.style.display = ''` after use — `positionPopover()` sets an inline `display:block` to measure the popover before positioning it, and if `closePopover()` doesn't clear that inline style, the box stays visibly stuck open (even though the `.open` class gets removed) after the first time it's ever opened.
2. In the CSS, the base `#sidePanel{ display:none; }` rule must come **before** the `@media (min-width:1300px){ #sidePanel{ display:block; } }` override in source order — both selectors have identical specificity (`#sidePanel`), so if the media-query block appears first, the base rule wins regardless of viewport width and the side panel never shows.

## If you want to add/fix a row

1. Find the row's entry in the `DATA` object (search for its row number, e.g. `30: {`).
2. Edit `purpose` / `steps` / `normal` as plain strings.
3. To add a photo: drop the image file in `assets/`, then add `images: [{src:"assets/your_file.jpg", caption:"... (Source: wherever)"}]` to that row's object.
4. Open the file directly in a browser to sanity-check. If `file://` behaves unreliably (relative image paths sometimes mangled by sandboxed preview tools), run `python3 -m http.server` from inside the folder and load `http://127.0.0.1:PORT/` instead.

## Known remaining gaps / notes

- Row 7 (Appropriately Drapes the Chest) and row 15 (Thoracic Spine OSE/TART) have no image — same as in the source projects (documented gaps there too).
- Row 8 (Visual Inspection — Skin/Trachea/Chest/Breathing) has no image or `normal` block, per the specified CN/Cardio source row, even though the equivalent HEENT/Pulm row has both — see deviation note above.
- Row 30 (lymphadenopathy) is the only row with newly-written content in this build; everything else (30 of 31 rows) is verbatim or near-verbatim reuse from the CN/Cardio and HEENT/Pulm projects.
