# How this was built

A dev log for future-me (or a future Claude session) picking this back up. Written after the fact from the actual build history, so it should be accurate.

## What this is

An interactive, offline HTML study version of the "2 System Rubric — HEENT, Pulmonary, Regional OSE, and Special Tests" PDF (the faculty grading rubric for the OSCE practical). Same rows, same `*`/`P`/`0` and `M`/`NI`/`U` grading columns as the paper rubric, but every test row is interactive: hover (desktop) or tap (touch) shows purpose / step-by-step technique / normal-vs-abnormal findings / reference photos for that specific maneuver.

It's a single self-contained HTML file (`2 System Rubric - ....html`) plus an `assets/` folder of images. No build step, no server, no dependencies — just open the HTML file in a browser. Everything (CSS, JS, and the content data) lives inline in that one file except the images.

This is the fifth rubric in the series (after Cranial Nerve/Cardiovascular, and the three MSK rubrics) and reuses that series' exact architecture line-for-line — CSS, JS, bug fixes, and all. If you've read one of those `BUILD_NOTES.md`, this one will look very familiar on purpose.

## How the content got in there — the big shortcut

Roughly half of this rubric's 35 gradable rows are the same or near-identical tests to rows already fully built (with verified content and photos) in the **Cranial Nerve/Cardiovascular** rubric — both projects share a lot of the same HEENT and cardiopulmonary maneuvers. Rather than re-deriving that content from scratch, it was copied directly from that project's `DATA` object and its matching image(s) copied into this project's `assets/` folder (same filename in most cases).

**17 of 35 rows were reused this way:**

| This rubric's row | Reused from CN/Cardio rubric's row |
|---|---|
| 4 — CN2 Pupillary Reflex | row 2 |
| 5 — CN2 red reflex / fundoscopic | row 23 |
| 6 — CN3/4/6 H test | row 3 |
| 7 — CN8 hearing finger rub/whisper | row 6 |
| 12 — Palpate Thyroid | row 35 |
| 13 — UE edema/cap refill | row 10 |
| 14 — LE edema/cap refill | row 12 |
| 15 — Drapes the chest | row 16 (text-only, no image, as in the original) |
| 16 — Visual inspection skin/trachea/chest/breathing | row 17 (text-only original — **plus a new image added**, see below) |
| 21 — Thoracic spine OSE/TART | row 20 (the `fallback`/no-source-match red-banner pattern carried over exactly, still no image) |
| 22 — CN2 peripheral fields | row 22 |
| 23 — CN2 Snellen/Rosenbaum | row 1 |
| 24 — CN5 facial sensation + jaw motor | row 4 |
| 25 — CN7 facial movement | row 5 |
| 26 — CN8 Weber/Rinne | row 24 |
| 27 — Sinus headache/pressure | row 25 |
| 28 — Mouth exam (special-test/gloved version) | row 28 |

One enhancement beyond a straight copy: row 16 (Visual Inspection — Skin, Trachea, Chest & Breathing) was text-only with no image in the CN/Cardio original, but a good matching diagram (barrel chest / flail chest inspection reference) turned up in the Week 4 Pulmonary notes while sourcing rows 17–20. That image was added to row 16 here even though its text was otherwise a straight reuse.

## How the remaining ~18 rows got sourced

For the rows with no CN/Cardio equivalent (rows 1, 2, 3, 8, 9, 10, 11, 17–20, and 29–35), content came from two sources:

1. **Week 2 HEENT study notes** (`Week 2` folder) — used for skin/head inspection framing, the sclera/conjunctiva exam (row 3), the otoscopic ear exam (row 8), the otoscopic/speculum nose exam (row 9), the lighter routine mouth/throat exam (row 10 — distinct from the gloved special-test version in row 28, which was reused from CN/Cardio), and head/cervical/supraclavicular lymph node palpation (row 11). All of these got a real photo pulled from that file's embedded lecture-slide images.
2. **Week 4 Pulmonary study notes** (`Week 4` folder) — used for the posterior/anterior lung auscultation-and-percussion ladder rows (17–20), tactile fremitus (29), the three "voice sound" tests — whispered pectoriloquy/bronchophony/egophony (30–32) — diaphragmatic excursion (33), and respiratory excursion (34). This file is thinner than Week 2 (only 7 embedded images), but it happened to have exactly the right diagrams: a labeled 7-point posterior percussion/auscultation ladder, a 5-percussion-notes table, and a posterior fremitus/respiratory-expansion hand-placement diagram — all pulled straight from Bates' Guide to Physical Examination via the course slides. Those three images get reused across the auscultation/percussion/voice-sound/excursion rows since they're literally the same technique points and the same hand placement each time.

3. **Web search (open-licensed) for the two true gaps:**
   - **Row 19/20 — Anterior lung auscultation, 6-point ladder.** Neither Week 2 nor Week 4 had an anterior-specific numbered ladder diagram (Week 4's anterior image was a breath-sounds comparison table, not a point diagram). Found `Thoracic_landmarks_anterior_view_lung_ausc.svg` on Wikimedia Commons (author "Põnn", CC BY 2.5) and used that.
   - **Row 35 — DVT check.** No DVT/Homans-sign content existed in any of the local course notes at all. Sourced a Homans-sign technique illustration from OrthoFixar (`orthofixar.com`) — the same site the CN/Cardio project already used for its Adson's test image, so it's a consistent source choice for this series.

**Rows with no image (text-only), and why:**
- Row 1 — Visual Inspection of the Skin: no dedicated skin-inspection image in Week 2 (the HEENT notes focus on eye/ear/nose/mouth/neck, not general skin), and this maneuver is generic enough that a web search wasn't worth it. Real instructional text is present.
- Row 2 — Palpates the Head for nodules/cysts/rashes: same reasoning — no matching photo in the source notes.
- Row 15 — Drapes the Chest: reused text-only from CN/Cardio (a modesty/consent action, not really photographable).
- Row 21 — Thoracic Spine OSE/TART: reused the CN/Cardio `fallback` banner treatment — this OMM/OSE topic has no matching source text in any of the course notes checked across either project, and it's flagged with the same red "no exact source match" banner (`no-source` class) as before.

## Image sourcing summary (for the record)

Of the 35 gradable rows:
- **17 rows** reused a photo/diagram (and its content) directly from the CN/Cardiovascular rubric's `assets/` folder.
- **10 rows** got a new photo pulled from the Week 2 HEENT or Week 4 Pulmonary course-note files (rows 3, 8, 9, 10 [routine mouth exam], 11 from Week 2; rows 16 [bonus add-on], 17, 18, 19 [lobe-correlation add-on], 20, 29, 33, 34 from Week 4 — several rows share the same Week 4 diagram since it's the same technique/points).
- **2 rows** got a new open-licensed image from a web search (row 19/20's anterior ladder diagram from Wikimedia Commons; row 35's DVT/Homans-sign illustration from OrthoFixar).
- **4 rows** are text-only with real instructional content but no image (rows 1, 2, 15, 21) — nothing suitable existed in either project's source notes or was worth a speculative web search for.

Confidence check: the row 9 "Otoscope and New Speculum" nose exam and the row 30–32 voice-sound rows (whispered pectoriloquy/bronchophony/egophony) reuse a general auscultation/exam-point image rather than a maneuver-specific photo (there's no photo of someone literally saying "99" into a stethoscope) — this is a deliberate "closest available reference" choice, flagged here in case a better image turns up later.

## How the interactivity works

Identical to the other four rubrics in this series — everything lives in one `<script>` block at the bottom of the HTML:

- **`DATA`** — a big object keyed 1–35 (matches the rubric row numbers), each with `name`, `purpose`, `steps[]`, `normal`, and optionally `images[]` (`{src, caption}`) or `fallback` (used only for row 21, Thoracic OSE/TART, flagged with a red "no exact source match" banner in the UI via the `no-source` CSS class).
- **`buildContent(key)`** — turns one `DATA` entry into the HTML shown in a popover/panel (purpose, steps list, normal/abnormal callout, image thumbnails).
- Two display modes, picked automatically by viewport width:
  - **≥1300px (side-panel mode)**: a sticky panel docked to the right of the rubric (`#sidePanel`) shows the content directly — hovering a row just swaps `#sidePanelContent`'s innerHTML in place. No positioning math, nothing opens or closes.
  - **<1300px (floating-card mode, used on tablets/phones and narrow windows)**: the floating popover (`#popover`) positioned near the hovered/tapped row via `positionPopover()`, with a semi-transparent `#overlay` to catch outside clicks.
- **Click-to-enlarge**: any image in either mode opens in a full-screen `#lightbox` overlay (dark backdrop, tap/click outside or the × to close).
- Touch detection is `matchMedia('(hover: none)')` — real touch devices get tap-only behavior; anything with a mouse gets hover behavior in whichever display mode applies.

### The two known bugs from the original build — both carried the fix forward

1. `closePopover()` resets `popover.style.display = ''` after removing the `.open` class. Without this, `positionPopover()`'s inline `display:block` (set to measure the popover's size before positioning it) permanently overrides the CSS hiding rule after the first popover open, and the × button visually does nothing.
2. The base `#sidePanel{ display:none; }` CSS rule comes **before** the `@media (min-width:1300px){ #sidePanel{ display:block; } }` override in source order. Both rules have equal specificity (plain `#sidePanel`), so if the media query block were accidentally moved before the base rule, the base rule would win regardless of viewport width and the panel would never show.

Verified directly in this build: `getComputedStyle(popover).display` reads `"none"` after clicking the close button (not just missing the `.open` class), and `getComputedStyle(sidePanel).display` reads `"block"` at 1600px width / `"none"` at 900px width.

## If you want to add/fix a row

1. Find the row's entry in the `DATA` object (search for its row number, e.g. `35: {`).
2. Edit `purpose` / `steps` / `normal` as plain strings (double-quoted, so apostrophes like "Homans sign" are fine as-is; escape any literal double quotes).
3. To add a photo: drop the image file in `assets/` (descriptive lowercase-with-underscores filename), then add `images: [{src:"assets/your_file.jpg", caption:"... (Source: wherever)"}]` to that row's object.
4. Open the file directly in a browser to sanity-check — no build step needed. For anything involving relative image paths, testing via `file://` can be unreliable in some sandboxed preview tools; if an image looks broken, try `python3 -m http.server` from inside the folder and load `http://127.0.0.1:PORT/` instead before assuming it's a real bug.

## Verification done on this build

Served locally with `python3 -m http.server` and checked in a real browser (not just `file://`):
- No console errors.
- All 35 rows have a matching `DATA[key]` entry (scripted check — zero missing keys).
- All 26 unique image files referenced in `DATA` load successfully (`naturalWidth > 0` for every one — scripted check).
- Side panel: `display:block` at 1600px width, `display:none` at 900px width (confirms the media-query source-order fix is intact).
- Floating popover opens on click at narrow width, and the × button closes it fully (both the `.open` class AND the computed `display` return to hidden — confirms the `closePopover()` fix is intact).
- Lightbox opens on image click with the correct `src` and caption, and closes via the × button.
