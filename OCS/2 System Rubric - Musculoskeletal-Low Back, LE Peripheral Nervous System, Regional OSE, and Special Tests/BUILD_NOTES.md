# How this was built

A dev log for future-me (or a future Claude session) picking this back up. Written after the fact from the actual build history, so it should be accurate.

## What this is

An interactive, offline HTML study version of the "2 System Rubric — Musculoskeletal-Low Back, LE Peripheral Nervous System, Regional OSE, and Special Tests" PDF (the faculty grading rubric for the OSCE practical). Same rows, same `*`/`P`/`0` and `M`/`NI`/`U` grading columns as the paper rubric, but every test row is interactive: hover (desktop) or tap (touch) shows purpose / step-by-step technique / normal-vs-abnormal findings / reference photos for that specific maneuver.

It's a single self-contained HTML file (`2 System Rubric - ....html`) plus an `assets/` folder of images. No build step, no server, no dependencies — just open the HTML file in a browser (or serve the folder for the most reliable local preview — see "Verifying" below).

This is the third build of this tool. It was made by copying the architecture of the second one (the Shoulder rubric) almost line-for-line, which itself copied the first (Cranial Nerve/Cardiovascular rubric) — same CSS, same JS interaction logic, same two bugs already fixed and carried forward (see "Bugs to avoid" below).

## A quirk in the source PDF, preserved on purpose

The PDF's own section headers say "Musculoskeletal System Exams for the **Knee**" and "Special Tests for Musculoskeletal-**Knee**/related joints and Nervous Systems" — but the actual row content in both sections is entirely low back / hip / SI-joint / lower-extremity focused; there is no knee-specific content anywhere on this rubric. This looks like the "Knee" header text was copy-pasted from a different rubric version and never updated. Per instruction, the header text was transcribed exactly as printed rather than "corrected" to something like "Low Back" — if this turns out to be an actual typo in the source document, it's worth flagging to faculty, but the tool intentionally reflects the PDF as written.

The one deliberate correction made during transcription: the grading-key note said "Give Student the **Maine** Header" in the source PDF — an obvious typo — fixed to "**Main** Header" here (same fix already made in the Cranial Nerve and Shoulder builds' grading-key text, which is otherwise reused verbatim across all three rubrics).

## How the content got in there

1. **Rubric skeleton**: transcribed by hand from the OCS 2 Musculoskeletal-Low Back rubric PDF — same section headers (including the "Knee" quirk above), same row order, same wording, same 6 Communication/Professionalism M/NI/U rows reused verbatim from the first two rubrics (identical wording across all three OSCEs).
2. **Rows 16, 19–26 (9 special tests: Adam's, SLR, Contralateral SLR, Thomas, Trendelenburg, Ober's, FABER, FADIR, Windshield Wiper)**: sourced from the same 25-page personal study guide written by the course instructor, Katrina Roop, DO ("Musculoskeletal Exam: Student/Facilitator Guide") used for the Shoulder rubric's special tests — her own demonstration photos plus Technique/Interpretation/Sensitivity-Specificity write-ups. This time the relevant pages were page 5 (Adam's Test — Adson's and Roos Test on the same page weren't needed here), pages 14–17 (Straight Leg Raise + Hoover, Thomas, Ober's + Ober's Variation + FABER, FADIR + Windshield Wiper + Log Roll), and page 17/18 boundary (Trendelenburg). Hoover Test, Log Roll Test, and Lachman Test are on these same pages but aren't rubric rows, so they were skipped. Contralateral Straight Leg Raising Test (row 20) is described as a note within the same SLR text block/photo in the guide rather than as its own photographed test, so it reuses the SLR image with its own caption/explanation, per the guide's own structure.
3. **Rows 1, 5, 15 (Gait, Inspection, LE OSE regional-testing rule)**: sourced from the OCS 2 Week 3 MSK Clinical Skills lecture slides — a "Gait/Standing Static Exam" overview slide, the "look before you touch" inspection slide (reused from the Shoulder build with a fresh copy in this project's own `assets/`), and an "Osteopathic Regional Testing" slide that spells out the "Lower Extremity Complaint" rule almost word-for-word matching row 15.
4. **Rows 12–14, 27–32 (LE myotomes, dermatomes, DTRs, cerebellar coordination, plantar response, and the 4 sensory-tract rows)**: sourced from the OCS 2 Week 1 neuro lecture/lab slides — the same slide deck used for the Shoulder rubric's UE version of these rows, but this time pulling the **lower-extremity** side of each dual-column slide (e.g. the "Motor Assessment: Strength" slide lists both UE and LE myotomes; only the LE column was used here) or a slide that's LE-specific by nature (the Babinski/plantar-response slide, the position/vibration-sense demo photos which happen to show a foot/toe rather than a hand).
5. **Rows 17–18 (Standing Flexion Test, ASIS Compression Test)** and **rows 2–4, 6–11 (OSE static screen views, palpation, AROM/PROM/strength of the thoracic/lumbar spine and hips)**: no clean photo or slide match was found in either the Week 1 or Week 3 course notes, and a web search for an openly-licensed technique photo (Standing Flexion / ASIS Compression) or a postural plumb-line diagram (for the 3 static-screen views) came up empty on Wikimedia Commons. These 11 rows are text-only — see "Known remaining gaps" below. Rows 17 and 18 specifically use the `fallback`/`no-source` pattern (see below) since even the Week 3 "Osteopathic Regional Testing" slide only names these tests in a bulleted list rather than describing technique; the step-by-step content for those two rows was written from standard SI-joint-exam technique descriptions instead of a single course-slide source.

Every image caption ends with a short `(Source: ...)` note — not a legal notice, just so it's traceable later if a citation is ever needed or an image needs replacing. Roop-guide images are captioned "used with permission" per the guide's own attribution.

## How the interactivity works

Identical architecture to the first two rubric tools — everything lives in one `<script>` block at the bottom of the HTML:

- **`DATA`** — an object keyed 1–32 (matches the rubric row numbers), each with `name`, `purpose`, `steps[]`, `normal`, and optionally `images[]` (`{src, caption}`) and/or `fallback` (a short italic note shown above the purpose, used only for rows 17–18 where no course-slide technique description existed and standard technique language was used instead).
- **`buildContent(key)`** — turns one `DATA` entry into the HTML shown in a popover/panel (fallback note if present, purpose, steps list, normal/abnormal callout, image thumbnails).
- Two display modes, picked automatically by viewport width:
  - **≥1300px (side-panel mode)**: a sticky panel docked to the right of the rubric (`#sidePanel`) shows content directly — hovering a row just swaps `#sidePanelContent`'s innerHTML in place. No positioning, nothing opens or closes.
  - **<1300px (floating-card mode, used on tablets/phones and narrow windows)**: a floating popover (`#popover`) positioned near the hovered/tapped row via `positionPopover()`, with a semi-transparent `#overlay` to catch outside clicks.
- **Click-to-enlarge**: any image in either mode opens in a full-screen `#lightbox` overlay (dark backdrop, tap/click outside or the × to close).
- Touch detection is `matchMedia('(hover: none)')` — real touch devices get tap-only behavior; anything with a mouse gets hover behavior in whichever display mode applies.

### Bugs to avoid (carried forward from the first two builds — do not reintroduce)

1. **`closePopover()` must reset `popover.style.display = ''`.** `positionPopover()` sets an inline `display:block` on the popover to measure its size before positioning it. If `closePopover()` only removes the `.open` class and doesn't also clear that inline style, the popover never actually hides again after the first time it opens — it looks like "the × button doesn't work." Verified fixed in this build: `closePopover()` at the bottom of the script does `popover.style.display = '';` right after removing `.open`, and confirmed programmatically (open → close → reopen → close via toggle, checking both the CSS class and the computed `display` value at each step, all as expected).
2. **CSS source order for `#sidePanel`.** The base `#sidePanel{ display:none; }` rule and the `@media (min-width:1300px){ #sidePanel{ display:block; } }` override have equal specificity (both plain `#sidePanel`), so the base rule **must come before** the media-query block in the stylesheet, or the base rule wins regardless of viewport width and the panel never shows. Verified in this build by checking `getComputedStyle(sidePanel).display` at a 1600px-wide viewport — returned `"block"` as expected.

## If you want to add/fix a row

1. Find the row's entry in the `DATA` object (search for its row number, e.g. `17: {`).
2. Edit `purpose` / `steps` / `normal` as plain strings (double-quoted, so apostrophes like "Ober's Test" are fine as-is; escape any literal double quotes).
3. To add a photo: drop the image file in `assets/` (descriptive lowercase-with-underscores filename, not the raw extraction names), then add `images: [{src:"assets/your_file.jpg", caption:"... (Source: wherever)"}]` to that row's object. If you add a real photo to rows 17 or 18, also remove their `fallback` field and the `no-source` class on the matching `<span class="hoverable no-source" data-key="17">` element in the table markup (and update the "Known remaining gaps" section below).
4. Open the file directly in a browser to sanity-check, or better, serve the folder locally and load it over `http://` — see below.

### Verifying (file:// can be unreliable)

`file://` previews of local files can behave unreliably in some sandboxed browser tools — relative image paths can appear to fail even when they're fine, and in this session the *screenshot* tool itself also had the same scroll-related rendering quirk documented in the Shoulder build's notes (blank captures at certain scroll offsets that had nothing to do with the page — confirmed by cross-checking with `get_page_text` and direct JS state checks, which all showed the content was there and correctly positioned). If a screenshot ever looks suspiciously blank, don't trust it blindly — scroll back to the top and re-screenshot, or verify with a JS query instead of a screenshot. To sanity check for real:

```
cd "2 System Rubric - Musculoskeletal-Low Back, LE Peripheral Nervous System, Regional OSE, and Special Tests"
python3 -m http.server 8792
```

then load `http://127.0.0.1:8792/...html`. This build was verified this way: zero console errors; at 1600px width the side panel shows and updates content on hover (`getComputedStyle(sidePanel).display === "block"` confirmed, plus hovering row 21 and checking `#sidePanelContent` actually contained "Thomas Test" and its image reference); at 1000px width the floating popover opens/closes/reopens/closes repeatedly via both click-to-toggle and the × close button, with no stuck-open state (checked via the popover's CSS class, computed `display`, and inline `style.display` at each step); all 25 unique `<img>` references across the 32 `DATA` rows were preloaded with `naturalWidth > 0` and zero failed to load; every one of the 32 `.hoverable` elements has a matching `DATA[key]`; and the lightbox opens on image click (confirmed the correct `src` loads) and closes via the × button.

## Row-by-row image sourcing summary

Of the 32 gradable rows:

- **21 rows have a real reference image**, split:
  - **9 rows (16, 19–26)** — Katrina Roop, DO's personal MSK special-testing guide (her own demonstration photos for the SLR, Thomas, Ober's, FABER, FADIR, and Windshield Wiper tests; a labeled illustration for the Trendelenburg test; a scoliosis illustration for Adam's forward bending test).
  - **3 rows (1, 5, 15)** — OCS 2 Week 3 MSK Clinical Skills lecture slides (gait/static-exam overview, "look before you touch" inspection slide, and the "Lower Extremity Complaint" OSE regional-testing rule slide — the last one is a near word-for-word match to the rubric's own row 15 wording).
  - **9 rows (12, 13, 14, 27, 28, 29, 30, 31, 32)** — OCS 2 Week 1 neuro lecture/lab slides: the LE myotome chart, LE dermatome map, LE DTR segmental-level list, cerebellar coordination (heel-to-shin/toe-tapping) slide, the Babinski/plantar-response photo pair, and the light-touch/spinothalamic/position/vibration/two-point-discrimination technique slides (row 31 uses 2 images — one for position sense, one for vibration sense — since the source slide deck covers them on separate slides).
- **11 rows are text-only**: rows 2, 3, 4, 6, 7, 8, 9, 10, 11 (the OSE static-screen views and the pure motion/palpation/strength-testing rows for the thoracic/lumbar spine and hips) plus rows 17 and 18 (Standing Flexion Test, ASIS Compression Test). All 11 have full purpose/steps/normal-vs-abnormal content; a targeted web search for open-licensed images for the static-screen plumb-line views and for the two SI-joint provocation tests didn't turn up anything on Wikimedia Commons clean enough to embed, so they were left as high-quality text rather than force a bad match. Rows 17 and 18 are additionally marked with the `no-source`/`fallback` pattern (a small italic note above the purpose) since even their written content had to be assembled from standard technique descriptions rather than a single course-slide source — see the CSS/JS notes above for how that pattern works.

## Rows to double-check for accuracy

- **Row 20 (Contralateral Straight Leg Raising Test)** — this reuses the same photo as row 19 (standard SLR) with a different caption/explanation, because the Roop guide describes the contralateral/crossed SLR as a note within the same text block as the standard SLR rather than as a separately photographed test. The image shows the standard SLR setup, not literally the opposite leg being raised — worth a second look if a dedicated crossed-SLR photo becomes available later.
- **Row 22 (Trendelenburg Test)** — uses a labeled anatomical illustration (A = negative, B = positive) from the Roop guide rather than a demonstration photo of an actual person performing the test. It's a clean, explicit match to the guide's own text ("See left: A is negative, B is positive"), but it's a diagram rather than a photo, unlike most of the other Roop-guide rows.
- **Rows 17 and 18 (Standing Flexion Test, ASIS Compression Test)** — text-only with no course-slide source; the technique descriptions were written from standard SI-joint-exam references rather than transcribed from a specific slide, so double-check the technique wording against current course materials before relying on it for the exam itself.
- **Row 12 (LE Myotomes) and row 14 (LE DTRs)** — both pulled from slides that list UE and LE side-by-side (Motor Assessment: Strength; Segmental Innervation of DTRs); double-checked that only the LE column's content was used, but worth a glance since the slides themselves are shared with the Shoulder rubric's UE rows.

## Known remaining gaps (no photo, text-only)

- Rows 2–4 — OSE Static Screen (Anterior/Lateral/Posterior views). A generic posture/plumb-line diagram would help here but nothing suitably open-licensed turned up in a Wikimedia Commons search; the full landmark list is still in the popover text. (Same gap as rows 1–3 in the Shoulder rubric build.)
- Rows 6–11 — Palpate TART, AROM thoracic/lumbar, AROM hips, PROM lumbar, strength testing of the lumbar spine. Pure motion-testing rows; no photo was needed to convey the instructions clearly, consistent with how the analogous Shoulder-rubric rows were handled.
- Rows 17–18 — Standing Flexion Test, ASIS Compression Test. No course-slide or open-licensed photo found; see "Rows to double-check" above.

If you find good images for these later, same procedure as above.
