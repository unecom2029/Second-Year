# Illness Scripts — Tabbed Comparison Note Format
**Build guide & design system spec**
*Reference file: `illness_scripts_42K.html` (Ocular Pathology — Conjunctivitis / AMD / Glaucoma / Cataract)*
*Quiz shell reference: `quiz_format_instructions.md` (launch screen + full-screen overlay quiz), reskinned per §11*

Paste this whole file into a new chat along with new source material (lecture slides, PDFs, Steve's notes) to get another note in this exact format.

---

## 1. What this format is for

Use this format when the studying goal is **discriminating between several related conditions** that get confused with each other on exam — not a single deep-dive topic. Good fits:

- Differentials for a chief complaint (red eye, chest pain, headache, joint pain)
- A cluster of diseases in one organ system covered in one lecture block
- Anything where the professor's exam style hinges on "which finding distinguishes X from Y"
- **The Disease Index assignment** (see §2) — this is now the primary use case, including larger multi-category units (see §4 for navigation at scale)

Each condition gets its own panel; the illness-script table and pathophys "chain" visuals are what make cross-condition comparison fast when switching between them. How you switch — a top tab row or a sidebar — depends on how many conditions there are; see §4.

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

Mark the range visibly wherever the disease is referenced — a pill next to the condition title (e.g. `<span class="pill pill-accent">LO 1–5</span>`), and, if using the sidebar nav (§4.3), a small badge next to its name in the sidebar too — so the intended depth is obvious at a glance without reading the source material again.

---

## 3. Architecture overview

Single self-contained `.html` file, no external dependencies except Google Fonts. Structure:

```
<head> — theme CSS variables (3 themes) + full stylesheet
<body>
  <header class="site-header">     — title, LO tag, print-text button, theme switcher
  <nav class="tab-nav"> OR <div class="layout-shell"><aside class="sidebar-nav">  — see §4
  <div id="panel-X" class="panel"> — repeated per condition, only one .active at a time
  <div class="qo" id="qo">         — one shared full-screen quiz overlay (see §11)
  <script>                         — theme/nav logic, print logic, quiz engine, question bank arrays
```

Everything lives in one file: fonts via CDN link, all else inline. No build step — open directly in a browser.

---

## 4. Navigation variants

Two ways to move between conditions, depending on how many there are and whether they're naturally grouped.

### 4.1 When to use which

| Condition count | Structure | Example |
|---|---|---|
| ≤ ~6–7, one flat comparison set | **Tab nav** (§4.2 — original) | Ocular pathology (4 conditions, no sub-categories) |
| > ~7, and/or naturally grouped into named categories | **Sidebar nav** (§4.3) | Primary Muscle Diseases (13 diseases across 5 categories) |

Both drive the same underlying panel-swap mechanism (`.panel` / `.panel.active`) — only the trigger element changes. Everything from §5 onward (design tokens, components, content skeleton, print, images, quiz) applies identically regardless of which nav is used.

### 4.2 Tab nav (small, flat sets)
Horizontal row of tab buttons at the top, one per condition, `overflow-x:auto` for scrolling if tight. See `.tab-nav` / `.tab-btn` in §6 — unchanged from earlier notes.

### 4.3 Sidebar nav (large sets, grouped by category)
Sticky left sidebar below the header, with collapsible category sections. Each category header shows the category name and disease count; expanding it reveals disease links; clicking one swaps the active panel exactly like a tab click would.

```html
<body>
  <header class="site-header">...</header>
  <div class="layout-shell">
    <aside class="sidebar-nav" id="sidebarNav">
      <div class="sidebar-category">
        <button class="cat-header" onclick="toggleCategory('md')">
          <span class="cat-toggle">▾</span>
          <span class="cat-name">Muscular Dystrophies</span>
          <span class="cat-count">4</span>
        </button>
        <div class="cat-items" id="cat-md">
          <button class="sidebar-link" data-panel="duchenne" onclick="showPanel('duchenne')">
            <span>Duchenne MD</span><span class="lo-badge">1–5</span>
          </button>
          <!-- one per disease in this category -->
        </div>
      </div>
      <!-- one .sidebar-category per category -->
    </aside>
    <main class="content-area">
      <!-- .panel elements, same as always -->
    </main>
  </div>
</body>
```

```css
.layout-shell{display:flex;align-items:flex-start;min-height:calc(100vh - 60px)}
.sidebar-nav{width:260px;flex-shrink:0;background:var(--bg-mid);border-right:1px solid var(--border);padding:14px 0;position:sticky;top:60px;max-height:calc(100vh - 60px);overflow-y:auto}
.cat-header{width:100%;display:flex;align-items:center;gap:8px;padding:10px 16px;background:transparent;border:none;cursor:pointer;font-family:'IBM Plex Mono',monospace;font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;color:var(--text-dim)}
.cat-header:hover{color:var(--text)}
.cat-toggle{transition:transform .2s;font-size:.8rem}
.cat-header.collapsed .cat-toggle{transform:rotate(-90deg)}
.cat-count{margin-left:auto;opacity:.5;font-size:.64rem}
.cat-items{display:flex;flex-direction:column}
.cat-items.collapsed{display:none}
.sidebar-link{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:8px 16px 8px 30px;background:transparent;border:none;border-left:3px solid transparent;text-align:left;font-family:'Nunito',sans-serif;font-size:.84rem;color:var(--text-dim);cursor:pointer;transition:all .15s;width:100%}
.sidebar-link:hover{background:var(--bg-hover);color:var(--text)}
.sidebar-link.active{border-left-color:var(--accent);background:var(--accent-faint);color:var(--accent);font-weight:700}
.lo-badge{font-family:'IBM Plex Mono',monospace;font-size:.6rem;opacity:.55}
.content-area{flex:1;min-width:0;padding:26px}
```

```js
function toggleCategory(catId){
  const items=document.getElementById('cat-'+catId);
  items.previousElementSibling.classList.toggle('collapsed');
  items.classList.toggle('collapsed');
}
function showPanel(id){
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.sidebar-link').forEach(l=>l.classList.remove('active'));
  document.getElementById('panel-'+id).classList.add('active');
  document.querySelector('.sidebar-link[data-panel="'+id+'"]').classList.add('active');
  window.scrollTo({top:0,behavior:'smooth'});
}
```

**LO badge:** each sidebar link shows the disease's LO range (§2) inline, muted, right-aligned — depth is visible while browsing, not just after opening the panel.

**Mobile (< 900px):** sidebar becomes an off-canvas drawer instead of a persistent rail, toggled from the header:
```html
<button class="sidebar-toggle-btn" id="sidebarToggleBtn">☰ Diseases</button>
```
```css
.sidebar-toggle-btn{display:none}
@media(max-width:900px){
  .sidebar-toggle-btn{display:inline-flex}
  .sidebar-nav{position:fixed;left:-280px;top:0;bottom:0;z-index:150;transition:left .25s;box-shadow:var(--shadow);background:var(--bg-mid)}
  .sidebar-nav.open{left:0}
  .layout-shell{display:block}
  .content-area{padding:18px}
}
```
```js
document.getElementById('sidebarToggleBtn').addEventListener('click', () => {
  document.getElementById('sidebarNav').classList.toggle('open');
});
```

**Default state:** first category expanded, others collapsed, first disease's panel active — same "start on the first one" convention as the tab-nav format.

**Category-only "introduction" pages:** if the source material has an overview page per category with no LO range of its own, it isn't a disease panel — fold anything worth keeping into a one-line subtitle under the category header rather than giving it a `.sidebar-link`/`.panel` of its own.

---

## 5. Design tokens (CSS variables)

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

Plus one color pair per condition (`--{condition}` / `--{condition}-f`), reused across all three themes with the same hue, only shifting lightness/saturation per theme so conditions stay recognizable when switching themes. With a sidebar nav (§4.3) and many conditions, it's fine to reuse a smaller set of hues across conditions within the same category rather than inventing 13 distinct colors — category membership already does most of the visual grouping.

**LO-section colors** (§7, added for the Disease Index format) — distinct from the condition palette, same across every note:

```css
--tx:      #4f8ff5; --tx-f:      rgba(79,143,245,0.10);   /* treatment */
--monitor: #2fb0a3; --monitor-f: rgba(47,176,163,0.10);   /* monitoring & complications */
--prevent: #3fae67; --prevent-f: rgba(63,174,103,0.10);   /* prevention & health promotion */
```

**Generic grading states** (added for the quiz system, §11) — independent of any condition's color, so correct/incorrect/highlight stay visually consistent no matter which condition's quiz is open:

```css
--success:   #2f9e5c; --success-f:   rgba(47,158,92,0.10);   /* correct answer, positive state */
--danger:    #d64545; --danger-f:    rgba(214,69,69,0.10);   /* incorrect answer, negative state */
--highlight: #d4a843; --highlight-f: rgba(212,168,67,0.10);  /* highlight tool, gold accents */
```

(All illustrative hex — tune lightness/saturation per theme the same way the existing condition colors are tuned. Keep them visually distinct from the condition palette chosen for that note.)

Typography: `Crimson Pro` (serif — headings, MCQ/quiz stems), `Nunito` (sans — body), `IBM Plex Mono` (labels, section-heads, pills, stat callouts). Load all three from Google Fonts in one `<link>` — used by the note, the sidebar, and the quiz overlay, no second font import needed.

---

## 6. Component library

| Component | Class | Use |
|---|---|---|
| Sticky header | `.site-header` | Title, LO/week tag, print-text button, theme switcher — always visible |
| Print-text button | `.print-btn` | Prints all panels' text as a plain PDF — see §8 |
| Theme switcher | `.theme-switcher` / `.theme-btn` | 3 colored dots, active state ring, **cream active by default** |
| Tab nav *(small sets)* | `.tab-nav` / `.tab-btn.{condition}` | One per condition; active tab gets condition color underline — see §4.2 |
| Sidebar nav *(large sets)* | `.layout-shell` / `.sidebar-nav` / `.cat-header` / `.sidebar-link` | Collapsible categories + disease links — see §4.3 |
| Panel | `.panel` / `.panel.active` | One per condition; `display:none` unless active, fade-in on switch |
| Condition title | `.condition-title` | Emoji + pills (quick-fact tags + **LO range pill**) + h2 in condition color |
| Section head | `.section-head` | Mono, uppercase, letter-spaced label with a trailing rule line |
| Callout | `.callout.{variant}` | Colored left-border box. Variants: `epi` (accent, natural history), `path` (purple, pathophys), `clin` (orange, clinical presentation), `warn` (red, red-flags/danger), `tip` (green, pearls), `gold` (amber, special/high-yield), `tx` (blue, treatment), `monitor` (teal, monitoring/complications), `prevent` (green, prevention) |
| Grid | `.grid-2` / `.grid-3` | Responsive card grid, collapses to 1 col under 640px |
| Mini card | `.mini-card` | Compact colored-top-border card, used to split a category into sub-types or treatment modalities (Medical/Surgical/Pharm/OMM) |
| Table | plain `<table>` | Diagnostic workup — "what will the question show me" section |
| Pill | `.pill.pill-{variant}` | Small inline tag, one per condition color plus `accent`/`purple`/`orange`, the LO-range pill, and quiz launch-screen chips (§11.4) |
| Chain | `.chain` / `.chain-step` / `.chain-arrow` | Horizontal pathophys flow (A → B → C), mono font, arrow in accent color |
| Video card | `.video-card`, `.video-thumb` | Clickable YouTube thumbnail that opens the video in a new tab — see §10 |
| Quiz launch card | `.mcq-section` → `.quiz-launch-btn` | Per-condition button that opens the shared full-screen quiz overlay — see §11 |
| Quiz overlay | `.qo`, `.qt-bar`, `.qin`, etc. | Full-screen launch + question experience, ported and reskinned from `quiz_format_instructions.md` — see §11 |

---

## 7. Content skeleton (per condition panel, in order)

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
| — | Practice Questions (optional) | Quiz launch card → opens the full-screen quiz overlay, see §11 | optional, any range |

---

## 8. Print Text button (full PDF of the whole note, images included)

A single button that prints **every condition panel — not just the active one** — as a clean PDF, images included but sized sensibly rather than stretched to fill the page. Works the same regardless of nav variant (§4): the print stylesheet forces all `.panel`s visible and hides the sidebar/tab-nav alike. The browser's native print dialog produces the actual PDF ("Save as PDF" / "Microsoft Print to PDF"); no JS PDF library needed.

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

Print stylesheet — forces every panel to render (normally `display:none` unless `.active`), keeps images but caps their size and stops them splitting across a page break, converts multi-column grids to a single stacked column (grids don't paginate reliably), and strips only the things that are genuinely non-content (nav, buttons, video thumbnails):

```css
@media print {
  .panel { display: block !important; page-break-after: always; }
  .panel:last-of-type { page-break-after: auto; }

  /* Chrome/nav/interactive elements never belong on paper */
  .site-header, .tab-nav, .sidebar-nav, .sidebar-toggle-btn, .print-btn, .theme-switcher,
  .mcq-reset, .qo, .launch-wrap, .quiz-launch-btn,
  .video-card { display: none !important; }

  .layout-shell { display: block !important; }
  .content-area { padding: 24px !important; }

  * { background: #fff !important; color: #000 !important;
      border-color: #000 !important; box-shadow: none !important; }
  body { font-size: 11pt; line-height: 1.5; }

  /* Grids don't paginate reliably — stack everything for predictable page breaks */
  .grid-2, .grid-3 { display: block !important; }
  .grid-2 > *, .grid-3 > * { margin-bottom: 10px !important; }

  /* Keep these from splitting awkwardly across a page boundary */
  .callout, .mini-card, table, .fig-card, tr {
    page-break-inside: avoid; break-inside: avoid;
  }
  .callout, .mini-card, table, .pill, .fig-card, .mcq-card { border: 1px solid #000 !important; }

  /* Images print — sized sensibly rather than stretched to full page width */
  img { display: block !important; }
  .fig-card img {
    width: auto !important; max-width: 5in !important; max-height: 6in !important;
    margin: 0 auto !important; page-break-inside: avoid; break-inside: avoid;
  }
  .fig-card { page-break-inside: avoid; break-inside: avoid; }

  a { text-decoration: none; color: #000 !important; }
}
```

**Included:** all LO sections built for every condition (respecting each disease's stratification range) across every category, plus all `.fig-card` images/figures, sized to fit the page. **Excluded:** header/nav controls (tabs or sidebar alike), video thumbnail cards (§10 — not clickable on paper, so not useful there), and the quiz overlay (it has its own separate print feature — §11.5).

---

## 9. Image insertion (use only if source material has usable images)

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
7. Images now print too (§8) — sized to fit the page rather than stretched, and prevented from splitting across a page break.

---

## 10. Video embeds (thumbnail-link, not iframe)

Practice videos (YouTube walkthroughs, mechanism explainers) get embedded as a **clickable thumbnail card that opens the video on YouTube in a new tab** — not a live `<iframe>` player.

**Why not `<iframe>`:** these notes are meant to be downloaded and opened locally (`file://`), not served from a website. YouTube's embedded player validates the page's origin before it'll play, and a local file has no real origin — so an `<iframe src="youtube.com/embed/...">` fails with a player error even for videos that allow embedding everywhere else. A thumbnail image + link has no such restriction; it works identically whether the file is local or hosted.

### 10.1 Getting the video ID
Whatever the person pastes — a plain URL (`https://youtube.com/watch?v=VIDEO_ID`) or a full `<iframe src="https://www.youtube.com/embed/VIDEO_ID" title="...">` embed snippet — pull the 11-character video ID out of it. The title attribute (if given) becomes the caption/overlay text; otherwise use the video's own title if known.

### 10.2 Markup
```html
<div class="video-card">
  <a class="video-link" href="https://www.youtube.com/watch?v=VIDEO_ID" target="_blank" rel="noopener noreferrer">
    <div class="video-thumb">
      <img src="https://img.youtube.com/vi/VIDEO_ID/hqdefault.jpg" alt="{Video title} thumbnail">
      <div class="play-btn">▶</div>
      <div class="video-title-overlay">▶ {Video title}</div>
    </div>
  </a>
  <div class="fig-caption">Video — "{Video title}" (YouTube)</div>
</div>
```
`img.youtube.com/vi/{VIDEO_ID}/hqdefault.jpg` is YouTube's public thumbnail CDN — always exists for any public video, no API key needed, and loads as a plain image (no origin restriction, unlike the player).

### 10.3 CSS
```css
.video-card{background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:10px;margin:9px 0}
.video-link{display:block;text-decoration:none}
.video-thumb{position:relative;width:100%;padding-bottom:56.25%;height:0;border-radius:5px;overflow:hidden;background:#000}
.video-thumb img{position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;opacity:.82;transition:opacity .15s}
.video-link:hover .video-thumb img{opacity:1}
.play-btn{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:60px;height:60px;background:rgba(0,0,0,.7);border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;border:2px solid rgba(255,255,255,.85);pointer-events:none}
.video-title-overlay{position:absolute;bottom:0;left:0;right:0;padding:8px 10px 7px;background:linear-gradient(transparent,rgba(0,0,0,.78));color:#fff;font-family:'Nunito',sans-serif;font-size:.78rem;font-weight:700;line-height:1.3}
```

### 10.4 Placement
One video per topic is typical; place it as its own `.video-card` near the top of the panel (after the quick-compare table if there is one, before Natural History) as an orientation resource. For a condition with multiple videos, wrap them in `.grid-2` or `.grid-3` (each card `style="margin:0"` to avoid doubled spacing) rather than stacking several full-width cards in a row — three stacked video cards push all the actual content below the fold.

### 10.5 Print
`.video-card` is hidden entirely in the Print Text output (§8) — a thumbnail isn't clickable on paper and doesn't carry information on its own, unlike a `.fig-card` image.

---

## 11. Quiz system (launch screen + full-screen overlay, reskinned from `quiz_format_instructions.md`)

Practice questions use the full launch-screen + full-screen-overlay quiz shell described in `quiz_format_instructions.md`, not a simple inline question list. Build it exactly as that file specifies — same HTML structure, same two-column layout, same Learn/Exam modes, timers, highlight/strikeout tools, nav dots, font-size control, and its own internal print-review feature — but **reskin every hardcoded color to pull from this note's own theme variables** instead of the fixed teal/navy/coral/gold palette in the source file. Structure, JS logic, breakpoints, and animations carry over unchanged.

### 11.1 Where it lives
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

### 11.2 Color mapping — reskin, don't reuse the source file's hardcoded hex

| Source file variable | Replace with |
|---|---|
| `--teal`, `--teal-deep`, `--teal-mid`, `--teal-glow`, `--teal-light` | `var(--accent)` / `var(--accent-faint)` — or the launching condition's own color, see §11.3 |
| `--navy`, `--navy2` (top bar) | `var(--bg-mid)` background, `var(--accent)` 2px bottom border, `var(--text)` text — i.e. reuse `.site-header`'s own look, see §11.4 |
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

### 11.3 Condition-colored launch
When the quiz opens from a specific condition, scope `--accent` on the overlay to that condition's color for the session (e.g. `qo.style.setProperty('--accent', getComputedStyle(document.documentElement).getPropertyValue('--conj'))`). This makes the progress bar, mode-toggle active state, and stem accents match whichever condition is being tested, instead of one fixed brand color for every quiz in the file.

### 11.4 Structural simplifications
- Launch-screen `.chip`s → use the existing `.pill`/`.pill-accent` component (§6) instead of a second badge system
- `.qt-bar` → reuse `.site-header`'s exact treatment: `background:var(--bg-mid); border-bottom:2px solid var(--accent); color:var(--text)` — so the quiz top bar and the note's own header read as the same product
- Fonts: unchanged, already loaded once in `<head>` and shared with the rest of the note

### 11.5 Everything else ports directly
Two-column overlay layout, score panel, mode toggle (Learn/Exam), stopwatch + countdown timers, tool panel (highlight/strikeout on stem and choices), exam submit flow, question card with progress bar + nav dots, answer-choice grading states, font-size control (A-/A/A+/A++), animations, and responsive breakpoints — all per the source file's §§3–11, unchanged except for the color substitutions in §11.2.

The quiz's own internal **Print** button (source file §8) — prints just the current question's review sheet — is a **separate feature** from the note-wide Print Text button in §8 of this doc. Reskin its print CSS to plain black-on-white the same way §8 does, rather than the source file's hardcoded green/red/teal hex.

### 11.6 Question data shape
Use `quiz_format_instructions.md`'s own §11 shape — `stem`, `choices`, `correct` (0-indexed), `explanation.correct/teaching/wrongs` — rather than the older `{text, correct, exp}` per-option shape used elsewhere in this doc. It's the shape the exam-mode grading, highlight/strikeout tools, and nav dots are all built around.

---

## 12. Technical build standards (carry over from established workflow)

- Single self-contained HTML output, base64 for any embedded images
- `node --check` the assembled `<script>` block before delivering, to catch syntax errors
- For large question banks or many conditions, use a Python assembly script rather than hand-writing the full file in one pass
- Use `str_replace` for any surgical post-hoc edits rather than regenerating the whole file
- If quiz/MCQ data is ever serialized through `json.dumps`, guard `</` → `<\/` to avoid breaking the embedding `<script>` tag

---

## 13. Naming convention

`{topic}_{LO-or-week-tag}.html` — e.g. `illness_scripts_42K.html` for OCS Week 40, LO 42K. Keep the sub tag in the header (`<span class="sub">`) matching the actual LO/week reference from the syllabus.

---

## 14. Build workflow checklist

1. For each disease in the source material, note its LO range (`1-2` / `1-3` / `1-4` / `1-5` / `1-6`). If any disease is missing a range, ask before proceeding.
2. Count conditions and check whether they're grouped into named categories — decide tab nav vs. sidebar nav per §4.1.
3. Scan source material for embeddable images (§9) — note which conditions will get one, and which LO section they belong in
4. Pick the condition palette + accent, define all three theme blocks including `--tx`/`--monitor`/`--prevent` and `--success`/`--danger`/`--highlight` (§5). Confirm `cream` is the default theme.
5. Build header (cream active by default, includes the print-text button) and the chosen nav (§4.2 tab-nav or §4.3 sidebar-nav)
6. For each condition, build the panel in the §7 order, stopping at the LO given by its range, using the components from §6
7. Add the LO-range pill to each condition title (and sidebar badge, if using §4.3)
8. Add the `@media print` stylesheet and wire the Print Text button (§8)
9. Build the shared quiz overlay once (§11), write each condition's question bank in the §11.6 shape, wire each condition's launch button to open it with that condition's color and questions
10. `node --check` the script, fix any syntax issues
11. Sanity-check in a browser: cream loads by default, theme switching, nav switching (tabs or sidebar categories), each panel stops at the correct LO, Print Text produces all panels in plain text, and the quiz overlay opens/grades/resets correctly from each condition
12. Save with the naming convention in §12

---

## 15. Quick-paste prompt for future sessions

> "Build a new Disease Index note in this format (see `illness-scripts-format.md`) for [conditions], based on [source material]. Each disease has its LO range marked in the source — build only through that range per §2/§7. Use [tab nav / sidebar nav] per §4. Default theme is cream, with a Print Text button (§8), video embeds per §10, and a quiz overlay per §11. Insert images per §9 if the source has usable figures."
