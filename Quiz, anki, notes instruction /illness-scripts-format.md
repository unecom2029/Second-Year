# Illness Scripts — Tabbed Comparison Note Format
**Build guide & design system spec**
*Reference file: `illness_scripts_42K.html` (Ocular Pathology — Conjunctivitis / AMD / Glaucoma / Cataract)*
*Quiz shell reference: `quiz_format_instructions.md` (launch screen + full-screen overlay quiz), reskinned per §9*

Paste this whole file into a new chat along with new source material (lecture slides, PDFs, Steve's notes) to get another note in this exact format.

---

## 1. What this format is for

Use this format when the studying goal is **discriminating between several related conditions** that get confused with each other on exam — not a single deep-dive topic. Good fits:

- Differentials for a chief complaint (red eye, chest pain, headache, joint pain)
- A cluster of diseases in one organ system covered in one lecture block
- Anything where the professor's exam style hinges on "which finding distinguishes X from Y"
- **The Disease Index assignment** (see §2) — this is now the primary use case

Each condition gets its own tab; the illness-script table and pathophys "chain" visuals are what make cross-condition comparison fast when flipping tabs.

If the source material is one big topic without natural sub-categories, use the **cumulative review** or **block pharm notes** format instead, not this one.

---

## 2. Disease Index assignment — the six objectives & stratification

This format is the build spec for the Disease Index assignment. Every disease has up to six learning objectives (LOs):

1. **Natural history** — etiology, epidemiology, pathology, pathophysiology, and prognosis if left untreated
2. **Typical clinical presentation**
3. **Diagnostic workup** — history, physical exam, labs, and relevant imaging needed to confirm the diagnosis
4. **Treatment** — medical, surgical, pharmaceutical, and OMM approaches
5. **Monitoring & long-term complications** — how treatment/management is tracked, and complications of the disorder over time
6. **Prevention & health promotion** — risk factor identification and prevention strategies

Not every disease needs all six. The source material marks each disease with a number range (e.g. `1-2`, `1-5`, `1-6`) right after its name, telling you how far to go:

| Range | Meaning | Build sections for |
|---|---|---|
| `1-2` | Rare / low morbidity | Natural history + Clinical presentation only |
| `1-3` | | + Diagnostic workup |
| `1-4` | | + Treatment |
| `1-5` | Common or higher morbidity | + Monitoring & complications |
| `1-6` | Good evidence for prevention | + Prevention & health promotion |

**Build rule:** for each disease, find its number range in the source material and build *only* the sections up through that number. Don't add treatment/monitoring/prevention content to a disease marked `1-2` — the stratification exists specifically to cap how deep you go, and over-building defeats the point of the assignment.

**If a disease has no range listed**, ask before building rather than guessing — getting the depth wrong is a correctness issue for this assignment, not a style choice.

Mark the range visibly on each condition panel: add a pill next to the condition title, e.g. `<span class="pill pill-accent">LO 1–5</span>`, so the intended depth is obvious at a glance without reading the source material again.

---

## 3. Architecture overview

Single self-contained `.html` file, no external dependencies except Google Fonts. Structure:

```
<head> — theme CSS variables (3 themes) + full stylesheet
<body>
  <header class="site-header">     — title, LO tag, print-text button, theme switcher
  <nav class="tab-nav">            — one button per condition
  <div id="panel-X" class="panel"> — repeated per condition, only one .active at a time
  <div class="qo" id="qo">         — one shared full-screen quiz overlay (see §9)
  <script>                         — theme/tab logic, print logic, quiz engine, question bank arrays
```

Everything lives in one file: fonts via CDN link, all else inline. No build step — open directly in a browser.

---

## 4. Design tokens (CSS variables)

Three themes, toggled via `data-theme` attribute on `<html>`, persisted to `localStorage` under a topic-specific key (e.g. `ocular-theme` — rename per topic).

**Default theme is `cream`.** Set `data-theme="cream"` on `<html>`, mark the cream theme button `active` by default in the header markup (`class="theme-btn t-cream active"`, and remove `active` from the dark button), and only let `localStorage` override it if the person has previously picked dark or slate in that browser:

```js
(function(){const t=localStorage.getItem('{topic}-theme'); setTheme(t || 'cream');})();
```

```css
[data-theme="dark"]  { /* ...as before... */ }
[data-theme="cream"] { /* ...as before — this is now the default rendered theme... */ }
[data-theme="slate"] { /* ...as before... */ }
```

Base palette per theme: `--bg`, `--bg-mid`, `--bg-card`, `--bg-hover`, `--border`, `--border-strong`, `--text`, `--text-dim`, `--text-faint`, `--accent`/`--accent-faint`, `--shadow`.

Plus one color pair per condition tab (`--{condition}` / `--{condition}-f`), reused across all three themes with the same hue, only shifting lightness/saturation per theme so tabs stay recognizable when switching themes.

**LO-section colors** (§6, added for the Disease Index format) — distinct from the condition palette, same across every note:

```css
--tx:      #4f8ff5; --tx-f:      rgba(79,143,245,0.10);   /* treatment */
--monitor: #2fb0a3; --monitor-f: rgba(47,176,163,0.10);   /* monitoring & complications */
--prevent: #3fae67; --prevent-f: rgba(63,174,103,0.10);   /* prevention & health promotion */
```

**Generic grading states** (added for the quiz system, §9) — independent of any condition's color, so correct/incorrect/highlight stay visually consistent no matter which condition's quiz is open:

```css
--success:   #2f9e5c; --success-f:   rgba(47,158,92,0.10);   /* correct answer, positive state */
--danger:    #d64545; --danger-f:    rgba(214,69,69,0.10);   /* incorrect answer, negative state */
--highlight: #d4a843; --highlight-f: rgba(212,168,67,0.10);  /* highlight tool, gold accents */
```

(All illustrative hex — tune lightness/saturation per theme the same way the existing condition colors are tuned. Keep them visually distinct from the condition palette chosen for that note.)

Typography: `Crimson Pro` (serif — headings, MCQ/quiz stems), `Nunito` (sans — body), `IBM Plex Mono` (labels, section-heads, pills, stat callouts). Load all three from Google Fonts in one `<link>` — used by both the note and the quiz overlay, no second font import needed.

---

## 5. Component library

| Component | Class | Use |
|---|---|---|
| Sticky header | `.site-header` | Title, LO/week tag, print-text button, theme switcher — always visible |
| Print-text button | `.print-btn` | Prints all panels' text as a plain PDF — see §7 |
| Theme switcher | `.theme-switcher` / `.theme-btn` | 3 colored dots, active state ring, **cream active by default** |
| Tab nav | `.tab-nav` / `.tab-btn.{condition}` | One per condition; active tab gets condition color underline |
| Panel | `.panel` / `.panel.active` | One per condition; `display:none` unless active, fade-in on switch |
| Condition title | `.condition-title` | Emoji + pills (quick-fact tags + **LO range pill**) + h2 in condition color |
| Section head | `.section-head` | Mono, uppercase, letter-spaced label with a trailing rule line |
| Callout | `.callout.{variant}` | Colored left-border box. Variants: `epi` (accent, natural history), `path` (purple, pathophys), `clin` (orange, clinical presentation), `warn` (red, red-flags/danger), `tip` (green, pearls), `gold` (amber, special/high-yield), `tx` (blue, treatment), `monitor` (teal, monitoring/complications), `prevent` (green, prevention) |
| Grid | `.grid-2` / `.grid-3` | Responsive card grid, collapses to 1 col under 640px |
| Mini card | `.mini-card` | Compact colored-top-border card, used to split a category into sub-types or treatment modalities (Medical/Surgical/Pharm/OMM) |
| Table | plain `<table>` | Diagnostic workup — "what will the question show me" section |
| Pill | `.pill.pill-{variant}` | Small inline tag, one per condition color plus `accent`/`purple`/`orange`, the LO-range pill, **and quiz launch-screen chips (§9.4)** |
| Chain | `.chain` / `.chain-step` / `.chain-arrow` | Horizontal pathophys flow (A → B → C), mono font, arrow in accent color |
| Quiz launch card | `.mcq-section` → `.quiz-launch-btn` | Per-condition button that opens the shared full-screen quiz overlay — see §9 |
| Quiz overlay | `.qo`, `.qt-bar`, `.qin`, etc. | Full-screen launch + question experience, ported and reskinned from `quiz_format_instructions.md` — see §9 |

---

## 6. Content skeleton (per condition panel, in order)

Build only through the objective number given for that disease (§2). Order is always the same — stop earlier for lower-stakes diseases, don't skip ahead.

| LO | Section | How to build it | Required when |
|---|---|---|---|
| — | Condition title | Emoji + LO-range pill + quick-fact pills + h2 in condition color | always |
| 1 | Natural history | `section-head` + `callout.epi` (etiology/epidemiology/risk factors) → `callout.path` + `.chain` flow diagrams (pathophysiology, split into `.grid-2` mini-cards if the condition has subtypes) → short prognosis-if-untreated line, folded into the epi callout or its own line | range ≥ 1-2 |
| 2 | Clinical presentation | `callout.clin`, `.grid-3` subtype mini-cards if relevant, `callout.warn` for red flags/referral triggers | range ≥ 1-2 |
| 3 | Diagnostic workup | Plain table — history/PE findings + labs/imaging | range ≥ 1-3 |
| 4 | Treatment | `section-head` + `.grid-2`/`.grid-3` of `.mini-card`s split by modality (Medical / Surgical / Pharmaceutical / OMM, only the modalities that actually apply) inside a `callout.tx` wrapper, or `callout.tx` alone if treatment is simple | range ≥ 1-4 |
| 5 | Monitoring & complications | `callout.monitor` — what to track, follow-up interval/tests, long-term complications list | range ≥ 1-5 |
| 6 | Prevention & health promotion | `callout.prevent` — modifiable risk factors, screening recommendations | range = 1-6 |
| — | Pearl (optional) | `callout.tip`/`.gold` — one high-yield fact, doesn't count as an LO | optional, any range |
| — | Practice Questions (optional) | Quiz launch card → opens the full-screen quiz overlay, see §9 | optional, any range |

---

## 7. Print Text button (plain-text PDF of the whole note)

A single button that prints **every condition panel's text — not just the active tab** — as a clean, black-on-white, image-free document. The browser's native print dialog produces the actual PDF ("Save as PDF" / "Microsoft Print to PDF"); no JS PDF library needed.

Add to the header, in `.header-right`, before the theme switcher:

```html
<button class="print-btn" id="printTextBtn" title="Print all text as PDF">🖨️ Print Text</button>
```

```css
.print-btn{font-family:'IBM Plex Mono',monospace;font-size:.66rem;background:transparent;border:1px solid var(--border);border-radius:5px;color:var(--text-dim);padding:5px 10px;cursor:pointer;transition:all .15s}
.print-btn:hover{border-color:var(--accent);color:var(--accent)}
```

```js
document.getElementById('printTextBtn').addEventListener('click', () => window.print());
```

Print stylesheet — forces every panel to render (normally `display:none` unless `.active`), strips all color/decoration to plain text, hides anything that isn't content, and breaks pages between conditions:

```css
@media print {
  .panel { display: block !important; page-break-after: always; }
  .panel:last-of-type { page-break-after: auto; }

  .site-header, .tab-nav, .print-btn, .theme-switcher,
  .mcq-reset, img, .fig-card img, .qo, .launch-wrap,
  .quiz-launch-btn { display: none !important; }

  * { background: #fff !important; color: #000 !important;
      border-color: #000 !important; box-shadow: none !important; }
  body { font-size: 11pt; line-height: 1.5; }
  .callout, .mini-card, table, .pill, .mcq-card { border: 1px solid #000 !important; }
  a { text-decoration: none; color: #000 !important; }
}
```

**Included:** all six LO sections built for every condition (respecting each disease's stratification range), tables, callout text, pill labels, and any inline MCQ stem/choice/explanation text. **Excluded:** images/figures, header/nav/theme controls, and the quiz overlay (it has its own separate print feature — §9.5).

---

## 8. Image insertion (use only if source material has usable images)

Apply this step whenever the lecture slides, PDF, or notes contain histology, fundoscopic/gross photos, imaging studies (X-ray/CT/MRI/OCT/ECG), or diagrams that clarify a finding described in the text.

1. **Scan first.** Before writing content, check the source material for embeddable figures. If nothing diagnostically relevant exists, skip this section entirely — do not source stock/generic images from elsewhere.
2. **Extract.** For PDF slide decks, rasterize the relevant slide with `pdftoppm` at 120–150 DPI, then crop to just the figure (strip slide chrome, titles, unrelated text) with an image tool.
3. **Compress & embed.** Keep each cropped image reasonably small (resize so the longest edge is ~600–900px, save as JPEG/PNG at reasonable quality) then base64-encode and embed inline — `<img src="data:image/png;base64,...">`. The file must stay single, self-contained, no external image links.
4. **Component.** Add a `.fig-card` matching the existing system (new class — build to match):
   ```css
   .fig-card{background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:10px;margin:9px 0}
   .fig-card img{width:100%;border-radius:5px;display:block}
   .fig-caption{font-family:'IBM Plex Mono',monospace;font-size:.66rem;text-transform:uppercase;letter-spacing:.08em;opacity:.6;margin-top:6px}
   ```
   Give the card a top border in the condition's accent color, matching `.mini-card` convention.
5. **Placement.** Place each image next to the content it illustrates, not batched at the end — e.g. a fundoscopy photo goes in "Diagnostic Workup" (LO 3), a histology slide goes in "Pathophysiology" (LO 1).
6. **Caption.** One line, mono font, stating what the image is and what to notice (e.g. "Fundoscopy — drusen with RPE atrophy, dry AMD").
7. Images are stripped in the Print Text output (§7) — figures only ever live in the on-screen note.

---

## 9. Quiz system (launch screen + full-screen overlay, reskinned from `quiz_format_instructions.md`)

Practice questions use the full launch-screen + full-screen-overlay quiz shell described in `quiz_format_instructions.md`, not a simple inline question list. Build it exactly as that file specifies — same HTML structure, same two-column layout, same Learn/Exam modes, timers, highlight/strikeout tools, nav dots, font-size control, and its own internal print-review feature — but **reskin every hardcoded color to pull from this note's own theme variables** instead of the fixed teal/navy/coral/gold palette in the source file. Structure, JS logic, breakpoints, and animations carry over unchanged.

### 9.1 Where it lives
Replace the old inline `.mcq-section` question list at the bottom of each panel with a compact **launch card**:
```html
<div class="mcq-section">
  <div class="mcq-section-title">🧠 Practice Questions — {Condition}</div>
  <button class="quiz-launch-btn" data-quiz="{condition}">Open Quiz →</button>
</div>
```
Build **one shared `.qo` overlay** for the whole file (not one per condition) — clicking a condition's launch button opens it and swaps in that condition's question array and accent color.

```css
.quiz-launch-btn{font-family:'Nunito',sans-serif;font-weight:800;font-size:.82rem;padding:9px 18px;border-radius:8px;border:1.5px solid var(--accent);background:var(--accent-faint);color:var(--accent);cursor:pointer;transition:all .15s}
.quiz-launch-btn:hover{background:var(--accent);color:#fff}
```

### 9.2 Color mapping — reskin, don't reuse the source file's hardcoded hex

| Source file variable | Replace with |
|---|---|
| `--teal`, `--teal-deep`, `--teal-mid`, `--teal-glow`, `--teal-light` | `var(--accent)` / `var(--accent-faint)` — or the launching condition's own color, see §9.3 |
| `--navy`, `--navy2` (top bar) | `var(--bg-mid)` background, `var(--accent)` 2px bottom border, `var(--text)` text — i.e. reuse `.site-header`'s own look, see §9.4 |
| `--coral`, `--coral-bg` | `var(--danger)` / `var(--danger-f)` |
| `--gold`, `--gold-bg`, `--gold-warm` | `var(--highlight)` / `var(--highlight-f)` |
| `--plum`, `--plum-bg`, `--sky`, `--sky-bg` | drop, or `var(--purple)` if a second decorative accent is wanted |
| `--warm`, `--cream`, `--white` | `var(--bg)`, `var(--bg-mid)`, `var(--bg-card)` |
| `--ink`, `--ink2`, `--slate`, `--mist` | `var(--text)`, `var(--text)`, `var(--text-dim)`, `var(--text-faint)` |
| `--rule`, `--rule2` | `var(--border)`, `var(--border-strong)` |
| `--green`, `--green-bg` | `var(--success)`, `var(--success-f)` |
| `--red`, `--red-bg` | `var(--danger)`, `var(--danger-f)` |
| `--amber`, `--amber-bg` | `var(--highlight)`, `var(--highlight-f)` |

`--r`, `--rs`, `--sh`, `--sh2`, `--sh3`, `--tr` (radii/shadows/easing) carry over unchanged — they're structural, not color.

### 9.3 Condition-colored launch
When the quiz opens from a specific condition tab, scope `--accent` on the overlay to that condition's color for the session (e.g. `qo.style.setProperty('--accent', getComputedStyle(document.documentElement).getPropertyValue('--conj'))` when opened from the conjunctivitis tab). This makes the progress bar, mode-toggle active state, and stem accents match whichever condition is being tested, instead of one fixed brand color for every quiz in the file.

### 9.4 Structural simplifications
- Launch-screen `.chip`s → use the existing `.pill`/`.pill-accent` component (§5) instead of a second badge system
- `.qt-bar` → reuse `.site-header`'s exact treatment: `background:var(--bg-mid); border-bottom:2px solid var(--accent); color:var(--text)` — so the quiz top bar and the note's own header read as the same product
- Fonts: unchanged, already loaded once in `<head>` and shared with the rest of the note

### 9.5 Everything else ports directly
Two-column overlay layout, score panel, mode toggle (Learn/Exam), stopwatch + countdown timers, tool panel (highlight/strikeout on stem and choices), exam submit flow, question card with progress bar + nav dots, answer-choice grading states, font-size control (A-/A/A+/A++), animations, and responsive breakpoints — all per the source file's §§3–11, unchanged except for the color substitutions in §9.2.

The quiz's own internal **Print** button (source file §8) — prints just the current question's review sheet — is a **separate feature** from the note-wide Print Text button in §7 of this doc. Reskin its print CSS to plain black-on-white the same way §7 does, rather than the source file's hardcoded green/red/teal hex.

### 9.6 Question data shape
Use the source file's §11 shape — `stem`, `choices`, `correct` (0-indexed), `explanation.correct/teaching/wrongs` — rather than the older `{text, correct, exp}` per-option shape used elsewhere in this doc. It's the shape the exam-mode grading, highlight/strikeout tools, and nav dots are all built around.

---

## 10. Technical build standards (carry over from established workflow)

- Single self-contained HTML output, base64 for any embedded images
- `node --check` the assembled `<script>` block before delivering, to catch syntax errors
- For large question banks or many conditions, use a Python assembly script rather than hand-writing the full file in one pass
- Use `str_replace` for any surgical post-hoc edits rather than regenerating the whole file
- If quiz/MCQ data is ever serialized through `json.dumps`, guard `</` → `<\/` to avoid breaking the embedding `<script>` tag

---

## 11. Naming convention

`{topic}_{LO-or-week-tag}.html` — e.g. `illness_scripts_42K.html` for OCS Week 40, LO 42K. Keep the sub tag in the header (`<span class="sub">`) matching the actual LO/week reference from the syllabus.

---

## 12. Build workflow checklist

1. For each disease in the source material, note its LO range (`1-2` / `1-3` / `1-4` / `1-5` / `1-6`). If any disease is missing a range, ask before proceeding.
2. Scan source material for embeddable images (§8) — note which conditions will get one, and which LO section they belong in
3. Pick the condition palette + accent, define all three theme blocks including `--tx`/`--monitor`/`--prevent` and `--success`/`--danger`/`--highlight` (§4). Confirm `cream` is the default theme.
4. Build header (cream active by default, includes the print-text button), theme switcher, tab nav
5. For each condition, build the panel in the §6 order, stopping at the LO given by its range, using the components from §5
6. Add the LO-range pill to each condition title
7. Add the `@media print` stylesheet and wire the Print Text button (§7)
8. Build the shared quiz overlay once (§9), write each condition's question bank in the §9.6 shape, wire each condition's launch button to open it with that condition's color and questions
9. `node --check` the script, fix any syntax issues
10. Sanity-check in a browser: cream loads by default, theme switching, tab switching, each panel stops at the correct LO, Print Text produces all panels in plain text, and the quiz overlay opens/grades/resets correctly from each condition
11. Save with the naming convention in §11

---

## 13. Quick-paste prompt for future sessions

> "Build a new Disease Index note in the tabbed comparison format (see `illness-scripts-format.md`) for [conditions], based on [source material]. Each disease has its LO range marked in the source — build only through that range per §2/§6. Default theme is cream, with a Print Text button (§7) and a quiz overlay per §9. Insert images per §8 if the source has usable figures."
