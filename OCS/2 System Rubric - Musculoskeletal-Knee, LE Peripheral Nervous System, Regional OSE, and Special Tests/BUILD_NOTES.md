# How this was built

A dev log for future-me (or a future Claude session) picking this back up. Written after the fact from the actual build history, so it should be accurate.

## What this is

An interactive, offline HTML study version of the "2 System Rubric — Musculoskeletal-Knee, LE Peripheral Nervous System, Regional OSE, and Special Tests" PDF (the faculty grading rubric for the OSCE practical). Same rows, same `*`/`P`/`0` and `M`/`NI`/`U` grading columns as the paper rubric, but every test row is interactive: hover (desktop) or tap (touch) shows purpose / step-by-step technique / normal-vs-abnormal findings / reference photos for that specific maneuver.

It's a single self-contained HTML file (`2 System Rubric - ....html`) plus an `assets/` folder of images. No build step, no server, no dependencies — just open the HTML file in a browser (or serve the folder for the most reliable local preview — see "Verifying" below).

This is the fourth build of this tool, made by copying the architecture of the third one (the Low Back rubric) almost line-for-line, which itself copied the second (Shoulder) and first (Cranial Nerve/Cardiovascular) builds — same CSS, same JS interaction logic, same two bugs already fixed and carried forward (see "Bugs to avoid" below).

Unlike the Low Back rubric's PDF, this one's own header text ("Musculoskeletal System Exams for the **Knee**" / "Special Tests for Musculoskeletal-**Knee**/related joints...") actually IS knee/ankle-specific content this time — rows 1–11 and 16–36 are genuinely about the hip/knee/ankle, not a leftover mismatched header. Rows 12–15 and 37–42 (the PNS/sensory/cerebellar section) are worded near-identically to the Low Back rubric's equivalent rows, since that content is generic to any LE complaint.

The one deliberate correction made during transcription (matching all three prior builds): the grading-key note said "Give Student the **Maine** Header" in the source PDF — an obvious typo — fixed to "**Main** Header" here.

## The two combined special-test rows (17 and 18)

The rubric lists 42 numbered rows, but two of them each cover a *pair* of related special tests as a single gradable row:

- **Row 17 — "Anterior and Posterior Drawer Tests BL"**: the Roop guide describes and photographs these as two separate techniques (same knee-flexed-90°, sitting-on-the-foot setup, force applied anterior vs. posterior). The row's popover content has an "Anterior Drawer" and a "Posterior Drawer" sub-section in its `steps`, and both photos are attached via `images: [...]` (2 images).
- **Row 18 — "Varus and Valgus Stress Tests BL"**: same pattern — the guide describes varus stress (testing the LCL) and valgus stress (testing the MCL) as two separate techniques with two separate photos, both folded into this one row's content (2 images, "Varus Stress" / "Valgus Stress" sub-sections).

Verified both rows actually render both sub-tests and both images in the popover/side-panel (see "Verifying" below).

## How the content got in there

1. **Rubric skeleton**: transcribed by hand from the OCS 2 Musculoskeletal-Knee rubric PDF — same section headers, same row order, same wording, same 6 Communication/Professionalism M/NI/U rows reused verbatim from the other three rubrics (identical wording across all four OSCEs).
2. **Rows 16–36 (21 rows: Lachman's, combined Anterior/Posterior Drawer, combined Varus/Valgus Stress, Apley Distraction, Apley Compression, McMurray's, Thessaly, Joint Line Tenderness, Tibial Tuberosity Tenderness, Talar Tilt, Ankle Anterior Drawer, Squeeze Test, Thompson's, Tinel's Ankle, Plantar Fasciitis, Metatarsal Squeeze, Hoover's, Ober's, FABER, FADIR, Windshield Wiper)**: sourced from the same 25-page personal study guide written by the course instructor, Katrina Roop, DO ("Musculoskeletal Exam: Student/Facilitator Guide") used for the Shoulder and Low Back rubrics' special tests. This time **pages 14–25 — the guide's entire hip/knee/ankle special-tests section** — covered almost the whole page-2 table. Straight Leg Raising, Contralateral SLR, Thomas Test, Trendelenburg Test, Log Roll Test, Bounce Home Test, and Patellar Apprehension Sign are all on these same pages but are NOT rows on this rubric (the guide's own text even flags Bounce Home and Patellar Apprehension as "not on rubric"), so none of their photos were pulled in. Ober's, FABER, FADIR, and Windshield Wiper photos are the same underlying source images already used in the Low Back rubric (same guide pages), re-extracted fresh into this project's own `assets/` folder rather than referencing the other project's folder.
3. **Rows 1, 5, 15 (Gait, Inspection, LE OSE regional-testing rule)**: sourced from the OCS 2 Week 3 MSK Clinical Skills lecture slides — the same "Gait/Standing Static Exam" overview slide, "look before you touch" inspection slide, and "Osteopathic Regional Testing" ("Lower Extremity Complaint") slide reused from the Low Back build, re-copied into this project's own `assets/`. A quick check for a knee/ankle-specific AROM photo in the Week 3 deck (per the build instructions) didn't turn up anything better than what the Low Back build already used, so the same slides were kept.
4. **Rows 12–14, 37–42 (LE myotomes, dermatomes, DTRs, cerebellar coordination, plantar response, and the 4 sensory-tract rows)**: sourced from the OCS 2 Week 1 neuro lecture/lab slides — identical source and identical images to the Low Back rubric's rows 12–14 and 27–32, since this rubric's PNS/sensory section is worded almost word-for-word the same (same dermatomes, same myotomes, same DTR levels, same sensory-tract technique). Re-copied into this project's own `assets/`.
5. **Rows 2–4, 6–11 (OSE static-screen views, palpation, AROM/PROM/strength of the hip/knee/ankle)**: no clean photo or slide match was found for these in either the Week 1 or Week 3 course notes (consistent with the Low Back build's experience for its analogous rows), and this rubric's page-2 table was already extremely well covered by the Roop guide, so no additional web search was needed. These 9 rows are text-only — see "Row-by-row image sourcing summary" below.

Every image caption ends with a short `(Source: ...)` note — not a legal notice, just so it's traceable later if a citation is ever needed or an image needs replacing. Roop-guide images are captioned "used with permission" per the guide's own attribution.

## How the interactivity works

Identical architecture to the first three rubric tools — everything lives in one `<script>` block at the bottom of the HTML:

- **`DATA`** — an object keyed 1–42 (matches the rubric row numbers), each with `name`, `purpose`, `steps[]`, `normal`, and optionally `images[]` (`{src, caption}`). No row in this build uses the `fallback`/`no-source` pattern (unlike the Low Back build's rows 17–18) — the Roop guide's coverage was thorough enough, and the 9 text-only OSE/AROM/PROM/strength rows are standard technique content, not content assembled without a source.
- **`buildContent(key)`** — turns one `DATA` entry into the HTML shown in a popover/panel (purpose, steps list, normal/abnormal callout, image thumbnails).
- Two display modes, picked automatically by viewport width:
  - **≥1300px (side-panel mode)**: a sticky panel docked to the right of the rubric (`#sidePanel`) shows content directly — hovering a row just swaps `#sidePanelContent`'s innerHTML in place. No positioning, nothing opens or closes.
  - **<1300px (floating-card mode, used on tablets/phones and narrow windows)**: a floating popover (`#popover`) positioned near the hovered/tapped row via `positionPopover()`, with a semi-transparent `#overlay` to catch outside clicks.
- **Click-to-enlarge**: any image in either mode opens in a full-screen `#lightbox` overlay (dark backdrop, tap/click outside or the × to close).
- Touch detection is `matchMedia('(hover: none)')` — real touch devices get tap-only behavior; anything with a mouse gets hover behavior in whichever display mode applies.

### Bugs to avoid (carried forward from the first three builds — do not reintroduce)

1. **`closePopover()` must reset `popover.style.display = ''`.** `positionPopover()` sets an inline `display:block` on the popover to measure its size before positioning it. If `closePopover()` only removes the `.open` class and doesn't also clear that inline style, the popover never actually hides again after the first time it opens — it looks like "the × button doesn't work." Verified fixed in this build: `closePopover()` at the bottom of the script does `popover.style.display = '';` right after removing `.open`, and confirmed programmatically (open → close via × → reopen → close via × again, checking both the CSS class and the computed/inline `display` value at each step — all as expected, no stuck-open state).
2. **CSS source order for `#sidePanel`.** The base `#sidePanel{ display:none; }` rule and the `@media (min-width:1300px){ #sidePanel{ display:block; } }` override have equal specificity (both plain `#sidePanel`), so the base rule **must come before** the media-query block in the stylesheet, or the base rule wins regardless of viewport width and the panel never shows. Verified in this build by checking `getComputedStyle(sidePanel).display` at a 1600px-wide viewport — returned `"block"` as expected.

## If you want to add/fix a row

1. Find the row's entry in the `DATA` object (search for its row number, e.g. `21: {`).
2. Edit `purpose` / `steps` / `normal` as plain strings (double-quoted, so apostrophes like "Ober's Test" are fine as-is; escape any literal double quotes).
3. To add a photo: drop the image file in `assets/` (descriptive lowercase-with-underscores filename, not the raw extraction names), then add `images: [{src:"assets/your_file.jpg", caption:"... (Source: wherever)"}]` to that row's object.
4. For the combined rows (17, 18): if you ever need to split them back into separate rows to match a rubric revision, duplicate the `<tr data-row="17">` markup for the new row, renumber all subsequent `data-row`/`row-num` values and `DATA` keys, and split the `steps`/`images` array between the two new `DATA` entries.
5. Open the file directly in a browser to sanity-check, or better, serve the folder locally and load it over `http://` — see below.

### Verifying (file:// can be unreliable)

`file://` previews of local files can behave unreliably in some sandboxed browser tools — relative image paths can appear to fail even when they're fine, and in this session the *screenshot* tool itself also had the same scroll-related rendering quirk documented in the prior builds' notes (a blank capture at one scroll offset that had nothing to do with the page — confirmed by cross-checking with a direct JS state query showing the side panel was correctly populated with McMurray's Test content and 4 images at that same scroll position, then reproduced correctly in a screenshot after scrolling back to the top). If a screenshot ever looks suspiciously blank, don't trust it blindly — scroll back to the top and re-screenshot, or verify with a JS query instead. To sanity check for real:

```
cd "2 System Rubric - Musculoskeletal-Knee, LE Peripheral Nervous System, Regional OSE, and Special Tests"
python3 -m http.server 8793
```

then load `http://127.0.0.1:8793/...html`. This build was verified this way: zero console errors; at 1600px width the side panel shows and updates content on hover (`getComputedStyle(sidePanel).display === "block"` confirmed, plus hovering rows 17, 18, and 21 and checking `#sidePanelContent` actually contained both sub-tests' text and both images for the combined rows, and all 4 McMurray images for row 21); at 1000px width the floating popover opens/closes/reopens/closes repeatedly via the × close button with no stuck-open state (checked via the popover's CSS class, computed `display`, and inline `style.display` at each step); all 42 unique `<img>` references across the 42 `DATA` rows were preloaded with `naturalWidth > 0` and zero failed to load; every one of the 42 `.hoverable` elements has a matching `DATA[key]`; and the lightbox opens on image click (confirmed the correct `src` loads, e.g. `assets/mcmurray_medial_1.jpg`) and closes via the × button.

## Row-by-row image sourcing summary

Of the 42 gradable rows:

- **33 rows have a real reference image**, split:
  - **21 rows (16–36)** — Katrina Roop, DO's personal MSK special-testing guide, pages 14–25 (her own demonstration photos and diagrams for Lachman's, the combined Anterior/Posterior Drawer row, the combined Varus/Valgus Stress row, Apley Distraction, Apley Compression, McMurray's — 4 images covering medial and lateral technique, Thessaly, Joint Line/Tibial Tuberosity Tenderness — 1 shared image used for both rows 23 and 24, Talar Tilt, Ankle Anterior Drawer, the Squeeze Test — 1 diagram + 1 photo, Thompson's, Tinel's Ankle, Plantar Fasciitis, Metatarsal Squeeze, Hoover's, Ober's, FABER, FADIR, and Windshield Wiper).
  - **3 rows (1, 5, 15)** — OCS 2 Week 3 MSK Clinical Skills lecture slides (gait/static-exam overview, "look before you touch" inspection slide, and the "Lower Extremity Complaint" OSE regional-testing rule slide).
  - **9 rows (12, 13, 14, 37, 38, 39, 40, 41, 42)** — OCS 2 Week 1 neuro lecture/lab slides: the LE myotome chart, LE dermatome map, LE DTR segmental-level list, cerebellar coordination (heel-to-shin/toe-tapping) slide, the Babinski/plantar-response photo pair, and the light-touch/spinothalamic/position/vibration/two-point-discrimination technique slides (row 41 uses 2 images — one for position sense, one for vibration sense — since the source slide deck covers them on separate slides).
- **9 rows are text-only**: rows 2, 3, 4, 6, 7, 8, 9, 10, 11 — the OSE static-screen views (anterior/lateral/posterior) and the pure inspection/palpation/AROM/PROM/strength-testing rows for the hip, knee, and ankle. All 9 have full purpose/steps/normal-vs-abnormal content written from standard OMM/PT exam technique; no course-slide photo match was found for these (consistent with the analogous rows in the Low Back rubric), and given how thoroughly the Roop guide covered the special-tests page, no additional web search was needed or attempted for these.
- **0 rows use the `fallback`/`no-source` pattern** — unlike the Low Back build (which needed it for 2 rows), every row here either has a real image or solid, confidently-sourced text-only content.

No web image search was used at all in this build — the Roop guide plus the two lecture-slide decks fully covered every image-bearing row.

## Rows to double-check for accuracy

- **Rows 23 and 24 (Joint Line Tenderness / Tibial Tuberosity Tenderness)** — both use the same image (`joint_line_tibial_tuberosity_tenderness.jpg`), because the Roop guide covers both palpation points in one combined technique paragraph and photo ("Palpate along the joint line and down the patellar tendon to the tibial tuberosity") even though the rubric splits them into two separate gradable rows. The two rows use different caption framing (joint-line focus vs. tibial-tuberosity focus) but show the identical photo — this was a deliberate choice per the build instructions, not an oversight.
- **Row 21 (McMurray's Test)** — uses 4 images (2 for medial meniscus technique, 2 for lateral meniscus technique) pulled from a 6-photo sequence in the guide (full flexion → rotation → extension, shown separately for medial and lateral). Two of the six source photos (the mid-rotation frames) were dropped as redundant with the full-flexion and final-extension frames already used; worth a look if a more complete step-by-step sequence is wanted later.
- **Row 32 (Hoover's Sign/Test)** — the Roop guide photo for this technique is a small, lower-resolution stock-style image compared to most of the guide's own demonstration photos; content/technique description is still directly from the guide's text, just flagging that the image itself is visually a lower-quality source than most others in this build.
- **Rows 12 and 14 (LE Myotomes, LE DTRs)** — both pulled from Week 1 slides that list UE and LE side-by-side; carried over directly from the Low Back build where this was already double-checked to use only the LE column/content.

## Known remaining gaps (no photo, text-only)

- Rows 2–4 — OSE Static Screen (Anterior/Lateral/Posterior views). A generic posture/plumb-line diagram would help here but nothing was searched for in this build since the Low Back build's equivalent search (Wikimedia Commons) previously came up empty for this same kind of diagram; the full landmark list is still in the popover text.
- Rows 6–11 — Palpate TART, AROM of the hip/knee/ankle, PROM of the knee, strength testing of the knee. Pure motion-testing rows; no photo was needed to convey the instructions clearly, consistent with how the analogous rows were handled in the Low Back and Shoulder rubrics.

If you find good images for these later, same procedure as above.
