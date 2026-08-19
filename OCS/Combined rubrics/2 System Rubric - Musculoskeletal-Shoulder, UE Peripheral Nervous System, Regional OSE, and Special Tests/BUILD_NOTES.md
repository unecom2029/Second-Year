# How this was built

A dev log for future-me (or a future Claude session) picking this back up. Written after the fact from the actual build history, so it should be accurate.

## What this is

An interactive, offline HTML study version of the "2 System Rubric — Musculoskeletal-Shoulder, UE Peripheral Nervous System, Regional OSE, and Special Tests" PDF (the faculty grading rubric for the OSCE practical). Same rows, same `*`/`P`/`0` and `M`/`NI`/`U` grading columns as the paper rubric, but every test row is interactive: hover (desktop) or tap (touch) shows purpose / step-by-step technique / normal-vs-abnormal findings / reference photos for that specific maneuver.

It's a single self-contained HTML file (`2 System Rubric - ....html`) plus an `assets/` folder of images. No build step, no server, no dependencies — just open the HTML file in a browser (or serve the folder for the most reliable local preview — see "Verifying" below).

This is the second build of this tool. It was made by copying the architecture of the first one almost line-for-line (`../2 System Rubric - Cranial Nerve, Cardiovascular, Regional OSE, and Special Tests/`) and swapping in new rubric content — same CSS, same JS interaction logic, same two bugs already fixed and carried forward (see "Bugs to avoid" below).

## How the content got in there

1. **Rubric skeleton**: transcribed by hand from the OCS 2 Musculoskeletal-Shoulder rubric PDF — same section headers, same row order, same wording, same 6 Communication/Professionalism M/NI/U rows reused verbatim from the first rubric (identical wording across both OSCEs).
2. **Rows 16–41 (all 26 special tests)**: sourced from a 25-page personal study guide written by the course instructor, Katrina Roop, DO ("Musculoskeletal Exam: Student/Facilitator Guide"), which includes her own demonstration photos (credited in the guide itself: "my personal photos throughout were taken by Jay Roop, DO and Christopher Medina, DO, images used with permission") plus Technique / Interpretation / Sensitivity-Specificity write-ups for each test. The guide's pages 3–13 map directly onto rubric rows 16–41 (pages 1–2 are gait/general-rules content used for rows 1–11 instead; pages 14–25 cover lower-extremity tests that aren't on this rubric and were skipped entirely).
3. **Rows 1–15 and 42–47 (regional exam technique, myotomes/dermatomes/DTRs, sensory/cortical testing)**: sourced from two other OCS course study-note pages built earlier this session — the Week 3 MSK Clinical Skills notes (static screening exam, regional testing template, motions-by-region, special-test quick map — covered rows 1–11 and 15 almost verbatim) and the Week 1 neuro notes (myotome chart, DTR segmental levels, dermatome map, and the sensory-exam slide deck covering light touch / spinothalamic / dorsal column / discriminative sensation — covered rows 12–14 and 42–47, several as exact word-for-word matches to the rubric wording).
4. **Gap-filling**: a couple of the OSE static-screen rows (1–3) and pure motion-testing rows (6–10, 31) ended up text-only — see "Known remaining gaps" below.

Every image caption ends with a short `(Source: ...)` note — not a legal notice, just so it's traceable later if a citation is ever needed or an image needs replacing. Roop-guide images that were her own demonstration photos are captioned "used with permission"; a couple of diagrams she herself sourced from elsewhere (an external illustration for Tromner's sign, a stock photo for the medial-epicondylitis test) are captioned with their original attribution instead, since that credit belongs to the original source, not to her.

## How the interactivity works

Identical architecture to the first rubric tool — everything lives in one `<script>` block at the bottom of the HTML:

- **`DATA`** — an object keyed 1–47 (matches the rubric row numbers), each with `name`, `purpose`, `steps[]`, `normal`, and optionally `images[]` (`{src, caption}`). No row in this build needed the `fallback`/`no-source` pattern from the first rubric — every row had a real matching source (Roop guide, Week 3 notes, or Week 1 notes) — but the CSS/JS support for it (`.no-source` class, `.pop-fallback` styling) was left in place unused, in case a future edit needs it.
- **`buildContent(key)`** — turns one `DATA` entry into the HTML shown in a popover/panel (purpose, steps list, normal/abnormal callout, image thumbnails).
- Two display modes, picked automatically by viewport width:
  - **≥1300px (side-panel mode)**: a sticky panel docked to the right of the rubric (`#sidePanel`) shows content directly — hovering a row just swaps `#sidePanelContent`'s innerHTML in place. No positioning, nothing opens or closes.
  - **<1300px (floating-card mode, used on tablets/phones and narrow windows)**: a floating popover (`#popover`) positioned near the hovered/tapped row via `positionPopover()`, with a semi-transparent `#overlay` to catch outside clicks.
- **Click-to-enlarge**: any image in either mode opens in a full-screen `#lightbox` overlay (dark backdrop, tap/click outside or the × to close).
- Touch detection is `matchMedia('(hover: none)')` — real touch devices get tap-only behavior; anything with a mouse gets hover behavior in whichever display mode applies.

### Bugs to avoid (carried forward from the first build — do not reintroduce)

1. **`closePopover()` must reset `popover.style.display = ''`.** `positionPopover()` sets an inline `display:block` on the popover to measure its size before positioning it. If `closePopover()` only removes the `.open` class and doesn't also clear that inline style, the popover never actually hides again after the first time it opens — it looks like "the × button doesn't work." Verified fixed in this build: `closePopover()` at the bottom of the script does `popover.style.display = '';` right after removing `.open`.
2. **CSS source order for `#sidePanel`.** The base `#sidePanel{ display:none; }` rule and the `@media (min-width:1300px){ #sidePanel{ display:block; } }` override have equal specificity (both plain `#sidePanel`), so the base rule **must come before** the media-query block in the stylesheet, or the base rule wins regardless of viewport width and the panel never shows. Verified in this build by checking `getComputedStyle(sidePanel).display` at a 1600px-wide viewport — returned `"block"` as expected (confirmed via the automated test described below, not just by eye).

## If you want to add/fix a row

1. Find the row's entry in the `DATA` object (search for its row number, e.g. `31: {`).
2. Edit `purpose` / `steps` / `normal` as plain strings (double-quoted, so apostrophes like "O'Brien's Test" are fine as-is; escape any literal double quotes).
3. To add a photo: drop the image file in `assets/` (descriptive lowercase-with-underscores filename, not the raw extraction names), then add `images: [{src:"assets/your_file.jpg", caption:"... (Source: wherever)"}]` to that row's object.
4. Open the file directly in a browser to sanity-check, or better, serve the folder locally and load it over `http://` — see below.

### Verifying (file:// can be unreliable)

`file://` previews of local files can behave unreliably in some sandboxed browser tools — relative image paths can appear to fail even when they're fine, and in this session the *screenshot* tool itself also had a scroll-related rendering quirk (blank captures at certain scroll offsets that had nothing to do with the page — confirmed by cross-checking with `document.body.scrollHeight` / `getBoundingClientRect()` and `get_page_text`, which all showed the content was there and correctly positioned). If a screenshot ever looks suspiciously blank, don't trust it blindly — scroll back to the top and re-screenshot, or verify with a JS query instead of a screenshot. To sanity check for real:

```
cd "2 System Rubric - Musculoskeletal-Shoulder, UE Peripheral Nervous System, Regional OSE, and Special Tests"
python3 -m http.server 8791
```

then load `http://127.0.0.1:8791/...html`. This build was verified this way: zero console errors; at ≥1300px the side panel shows and swaps content on hover (`getComputedStyle(sidePanel).display === "block"` confirmed); at <1300px the floating popover opens/closes repeatedly via both `click()` (JS) and a real mouse click on the × button, with no stuck-open state; every one of the 45 `<img>` references across all 47 `DATA` rows was preloaded with `naturalWidth > 0`; every `.hoverable` element (47 of them) has a matching `DATA[key]`; the lightbox opens on image click and closes via the × button; and single-select checkbox behavior (per-row radio-like toggling, plus the enlarged `td.col-check` tap target) was verified on the Communication/Professionalism rows.

## Row-by-row image sourcing summary

Of the 47 gradable rows:

- **36 rows have a real reference image**, split roughly:
  - **25 rows (16–41 except 31)** — Katrina Roop, DO's personal MSK special-testing guide (mostly her own demonstration photos; a couple of diagrams/illustrations reproduced within her guide from other named sources).
  - **5 rows (4, 12, 13, 14, 15)** — Week 3 MSK Clinical Skills notes and Week 1 neuro lecture slides (exact-match lecture-slide content, e.g. the myotome chart for row 12, the DTR segmental-level list for row 14).
  - **6 rows (42–47)** — Week 1 neuro sensory-exam lecture slides (light touch, spinothalamic, position/vibration, and the combined two-point/stereognosis/graphesthesia slide, reused across rows 45–47 since one slide covers all three tests).
- **11 rows are text-only**, all in the Musculoskeletal-Shoulder section (rows 1, 2, 3, 5, 6, 7, 8, 9, 10, 11) plus Speed's Test (row 31). These are plain motion/OSE-screen/palpation rows or a single special test where no clean photo match was found in either source set; a targeted web search for an open-licensed postural plumb-line diagram (for rows 1–3) didn't turn up anything clean enough to embed, so they were left as high-quality text (steps/normal-vs-abnormal) rather than force a bad match.

## Rows to double-check for accuracy

A few image matches were made by visual inspection of extracted guide photos without an explicit caption in the source text confirming which test each photo illustrates — worth a second look if something seems off:

- **Row 17 (Hoffman's/Tromner's)** — the Tromner's illustration is a diagram reused within the Roop guide from an external source (neupsykey.com per the guide's own text), not one of her personal photos; captioned accordingly.
- **Row 18 (Adson's Test)** and **row 32 (Yergason's Test)** — both involve an examiner holding the patient's wrist near shoulder height; these were told apart by elbow position (Adson's: arm abducted/extended/externally rotated while monitoring the radial pulse; Yergason's: elbow flexed ~90° near the body while resisting supination), but there was no in-image caption to confirm, only proximity to each test's text block on the source page.
- **Row 33 (Shoulder Apprehension Test)** — the "relocation" photo has an explicit "Relocation test" caption baked into the image itself, which is a strong confirmation; the paired "apprehension" photo (no caption) was inferred as the same setup without the posterior-pressure step.

## Known remaining gaps (no photo, text-only)

- Rows 1–3 — OSE Static Screen (Anterior/Lateral/Posterior views). A generic posture/plumb-line diagram would help here but nothing suitably open-licensed turned up in a quick search; the full landmark list is still in the popover text.
- Rows 5–10 — Palpate TART, AROM cervical/thoracic, AROM elbow, AROM shoulder, PROM shoulder. Pure motion-testing rows; no photo was needed to convey the instructions clearly.
- Row 11 — Strength testing of the shoulder. A generic "strength grading" lecture slide existed in the Week 3 notes but was mostly text and didn't add enough over the written steps, so it was left out rather than force a low-value image.
- Row 31 — Speed's Test. The Roop guide's page 9/10 photos couldn't be confidently distinguished from the neighboring Yergason's Test photo (both show a bent-vs-extended elbow position that's easy to mix up from a still photo), so this row was left text-only rather than risk mislabeling an image.

If you find good images for these later, same procedure as above.
