# How this was built

A dev log for future-me (or a future Claude session) picking this back up. Written after the fact from the actual build history, so it should be accurate.

## What this is

An interactive, offline HTML study version of the "2 System Rubric — Cranial Nerve, Cardiovascular, Regional OSE, and Special Tests" PDF (the faculty grading rubric for the OSCE practical). Same rows, same `*`/`P`/`0` and `M`/`NI`/`U` grading columns as the paper rubric, but every test row is interactive: hover (desktop) or tap (touch) shows purpose / step-by-step technique / normal-vs-abnormal findings / reference photos for that specific maneuver, pulled from the Week 1/2/5 OCS study notes plus some web research.

It's a single self-contained HTML file (`2 System Rubric - ....html`) plus an `assets/` folder of images. No build step, no server, no dependencies — just open the HTML file in a browser. Everything (CSS, JS, and the content data) lives inline in that one file except the images.

## How the content got in there

1. **Rubric skeleton**: transcribed by hand from the original PDF (`2026 OCS 2 Cranial Nerve, Cardiovascular, Regional OSE, and Special Tests Rubric.pdf` in Downloads) — same section headers, same row order, same wording.
2. **Per-row instructions/images**: the original build extracted the embedded photos out of five HTML "study notes" files (Week 1 Neuro/CN, Week 2 HEENT, Week 5 Cardiovascular, plus Week 4/6 checked for overlap) by stripping the base64 image data out of the HTML (huge blobs otherwise) and decoding each image to its own file. A background agent then matched each of the 35 gradable rubric rows to the relevant text/photo from those files. About half the rows got a real matched photo this way; the rest got real instructional text but no photo (nothing suitable existed in the source notes).
3. **Gap-filling with open-licensed images**: a second pass web-searched (Wikimedia Commons, OpenStax, etc.) for photos/diagrams for the rows that still had no image, preferring openly-licensed sources over random copyrighted reposts since images get embedded directly into the file. Filled about half of the remaining gaps this way; a few maneuvers (CN11 shoulder/head resistance, chest draping, CN1 smell test, etc.) just don't have good open-licensed photos out there.
4. **User-supplied images**: a few more (Allen's test sequence, Adson's test, carotid auscultation landmarks) came from URLs the user found and pasted in directly — downloaded, dropped into `assets/`, and wired into the matching row with a short attribution note in the caption. Since this file never leaves personal use, source-quality mattered more than license-purity for these.

Every image caption ends with a short `(Source: ...)` note — not a legal notice, just so it's traceable later if a citation is ever needed or an image needs replacing.

## How the interactivity works

Everything lives in one `<script>` block at the bottom of the HTML:

- **`DATA`** — a big object keyed 1–35 (matches the rubric row numbers), each with `name`, `purpose`, `steps[]`, `normal`, and optionally `images[]` (`{src, caption}`) or `fallback` (used only for row 20, Thoracic OSE/TART, which had no matching source text at all — it's flagged with a red "no exact source match" banner in the UI, driven by the `no-source` CSS class on that row's trigger element).
- **`buildContent(key)`** — turns one `DATA` entry into the HTML shown in a popover/panel (purpose, steps list, normal/abnormal callout, image thumbnails).
- Two display modes, picked automatically by viewport width:
  - **≥1300px (side-panel mode)**: a sticky panel docked to the right of the rubric (`#sidePanel`) shows the content directly — hovering a row just swaps `#sidePanelContent`'s innerHTML in place. No positioning math, nothing opens or closes.
  - **<1300px (floating-card mode, used on tablets/phones and narrow windows)**: the old-style floating popover (`#popover`) that's positioned near the hovered/tapped row via `positionPopover()`, with a semi-transparent `#overlay` to catch outside clicks.
- **Click-to-enlarge**: any image in either mode opens in a full-screen `#lightbox` overlay (dark backdrop, tap/click outside or the × to close).
- Touch detection is `matchMedia('(hover: none)')` — real touch devices get tap-only behavior; anything with a mouse gets hover behavior in whichever display mode applies.

### Why the side panel exists (bug history)

The original design was hover-only floating popovers everywhere. That had a real bug: `positionPopover()` set the popover's `display` via an inline style (to measure its size before positioning it), but `closePopover()` never cleared that inline style — so after the first time any popover opened, the inline `display:block` permanently overrode the CSS that was supposed to hide it again. Closing did remove the `.open` class, but the box just stayed visible, which looked like "the X button doesn't work." Fixed by having `closePopover()` reset `popover.style.display = ''`.

Separately, floating popovers positioned relative to the cursor have an inherent flicker risk: if the popover ends up rendered directly under the mouse (e.g. the "not enough room below, place above" fallback), the browser can fire a `mouseleave` on the row that triggered it (because the popover is now the topmost element at that point), which schedules a close, which un-covers the row, which can re-trigger `mouseenter` — a fight that reads as blinking. The real fix for desktop use was to stop repositioning a floating box near the cursor at all: the side panel sits in a fixed location and just swaps content, so there's no positioning, no open/close race, and nothing to blink. The floating-card fallback still exists for narrow/touch screens (where this matters less — touch doesn't hover-fight, and iPad-width screens don't have room for a side panel anyway) but inherits the same close-button fix.

One more easy-to-repeat mistake if editing the CSS: the base `#sidePanel{ display:none; }` rule and the `@media (min-width:1300px){ #sidePanel{ display:block; } }` override have equal specificity (both plain `#sidePanel`), so **source order matters** — the media query block must come *after* the base rule in the stylesheet, or the base rule wins regardless of viewport width and the panel never shows. (This exact bug happened once during the build — caught by checking `getComputedStyle(sidePanel).display` at a wide viewport and seeing `none` when it should've been `block`.)

## If you want to add/fix a row

1. Find the row's entry in the `DATA` object (search for its row number, e.g. `20: {`).
2. Edit `purpose` / `steps` / `normal` as plain strings (double-quoted, so apostrophes like "Allen's Test" are fine as-is; escape any literal double quotes).
3. To add a photo: drop the image file in `assets/` (descriptive lowercase-with-underscores filename), then add `images: [{src:"assets/your_file.jpg", caption:"... (Source: wherever)"}]` to that row's object.
4. Open the file directly in a browser to sanity-check — no build step needed. For anything involving relative image paths, testing via `file://` can be unreliable in some sandboxed preview tools (they can mangle relative paths); if an image looks broken, try `python3 -m http.server` from inside the folder and load `http://127.0.0.1:PORT/` instead before assuming it's a real bug.

## Known remaining gaps (no photo, text-only)

As of the last update, these rows still have real instructional text but no image — nothing suitable was found in the source notes or in an open-licensed web search:

- Row 8 — CN11 Spinal Accessory (shoulder shrug / head rotation resistance)
- Row 16 — Appropriately Drapes the Chest
- Row 17 — Visual Inspection (skin/trachea/chest/breathing)
- Row 20 — Thoracic Spine OSE/TART (also has no matched *source text* — flagged in the UI)
- Row 21 — CN1 Sense of Smell
- Row 10 — reuses the LE edema grading image (legitimate reuse, not a gap, just noting it's shared)

If you find good images for these later, same procedure as above.
