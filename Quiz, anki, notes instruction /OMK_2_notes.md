# How to Recreate These Medical Study Notes
> Instructions for future Claude: how to build an HTML study notes page like `Osteoporosis_Pharmacology_Study_Notes.html`.

---

## 1. What These Notes Are

A single-file HTML study document for a medical school lecture, organized around Learning Objectives (LOs). It has one primary display mode, plus an optional condensed view:
- **Normal mode** — full notes covering all LOs for the lecture
- **High-Yield One-Pager** — an optional modal overlay that condenses the whole file into a dense, printable 1–2 page cheat sheet organized by learning objective, with its own Print/Save-PDF button (see Section 12)

The One-Pager is optional — build it when the user wants a condensed pre-exam summary; otherwise the full notes stand alone.

The page is self-contained: no build tools, no frameworks, just one `.html` file with embedded CSS, fonts, and JS.

---

## 2. Fonts & Color System

### Google Fonts (import in `<head>`)
```
Playfair Display — headings (700, 900 weight)
Source Serif 4 — body text (300, 400, 600; italic variants)
JetBrains Mono — labels, badges, captions, monospaced UI
```

### CSS Custom Properties (`:root`)
Define all colors as variables so themes can override them cleanly:

```css
:root {
  --ink: #1a1209;        /* near-black body text */
  --paper: #faf7f2;      /* warm white background */
  --cream: #f2ede4;      /* slightly darker warm bg for cards */
  --accent: #b5341a;     /* red — warnings, oncogenes, section underlines */
  --accent2: #2c5f8a;    /* blue — concepts, h3 borders */
  --gold: #c9922a;       /* gold — exam answers, labels, key callouts */
  --muted: #6b5e4e;      /* muted brown-grey — secondary text */
  --border: #d4cabb;     /* warm grey — dividers, card borders */
  --highlight: #fff3cd;  /* yellow tint — key callout background */
  --highlight2: #ddeeff; /* blue tint — hover state on table rows */
  --green-bg: #e8f5e9;   /* clinical/correct callout background */
  --red-bg: #fce8e8;     /* warning callout background */
  --blue-bg: #e3f0fb;    /* concept callout background */
  --purple-bg: #f0ebff;  /* purple callout background */

  /* Hero-specific vars (override per-theme for correct contrast) */
  --hero-heading: #f5ede0;
  --hero-sub: #c9bcad;
  --hero-meta-bg: rgba(255,255,255,0.07);
  --hero-meta-border: rgba(255,255,255,0.12);
  --hero-meta-label: #8a7a6a;
  --hero-meta-value: #f0e0c8;

  /* Floating UI (font control, controls bar) */
  --floating-ui-bg: #3a3030;
  --floating-ui-fg: #f5ede0;
  --floating-ui-shadow: 0 3px 12px rgba(0,0,0,0.2);

  /* Table quiz cell overlay */
  --quiz-overlay: rgba(44,111,173,0.5);
  --quiz-overlay-hover: rgba(44,111,173,0.78);

  /* Dark-panel components (table headers, exam-q box) — see Section 3 */
  --panel-dark-bg: #1a1209;
  --panel-dark-text: #faf7f2;
}
```

---

## 3. Theme System

The page supports 5 visual themes via a `data-theme` attribute on the `<html>` element. **Paper is the default** — it's what renders when no `data-theme` attribute is present, and it's the theme every file should load with before the person picks something else.

### Available Themes

| Theme | Key Colors | `data-theme` value |
|---|---|---|
| **Paper (Default)** | Warm cream + dark ink | *(no attribute — omit `data-theme` entirely)* |
| Night | Dark navy + gold/blue | `night` |
| Ocean | Light blue + deep navy | `ocean` |
| Forest | Soft green + deep green | `forest` |
| Sepia | Warm tan + brown | `sepia` |

### Theme CSS Structure
Each theme overrides **all** `:root` CSS variables — not just the core palette, but also the hero, floating-ui, quiz-overlay, and dark-panel vars. Example (Night theme, abbreviated):

```css
[data-theme="night"] {
  --ink: #e0e8f0;
  --paper: #0f1923;
  --cream: #162030;
  --accent: #e8b84b;
  --accent2: #4aa8d8;
  /* ... remaining base variables ... */

  /* Hero vars */
  --hero-heading: #f4f9ff;
  --hero-sub: #b8cad8;
  --hero-meta-bg: rgba(255,255,255,0.08);
  --hero-meta-border: rgba(255,255,255,0.12);
  --hero-meta-label: #8fa4b8;
  --hero-meta-value: #f4f9ff;

  /* Floating UI */
  --floating-ui-bg: #070e15;
  --floating-ui-fg: #f4f9ff;
  --floating-ui-shadow: 0 3px 12px rgba(0,0,0,0.36);

  /* Quiz overlay */
  --quiz-overlay: rgba(74,168,216,0.42);
  --quiz-overlay-hover: rgba(74,168,216,0.62);

  /* Dark-panel components — fixed regardless of theme direction, see below */
  --panel-dark-bg: #101a26;
  --panel-dark-text: #eef5fb;
}
/* Then override specific components that need more than variable swaps: */
[data-theme="night"] .hero { background: #070e15; }
[data-theme="night"] .toc-bar { background: #070e15; border-color: #1e3048; }
```

> **Rule:** Every theme must override all four variable groups: base palette, hero vars, floating-ui vars, and the `--panel-dark-*` pair. Copy the full block from a reference file rather than writing it from scratch — it's easy to miss a variable.

### Theme Switcher HTML (in fixed bottom-right controls)
```html
<!-- THEME PANEL (popup above the button row) -->
<div class="theme-panel" id="themePanel">
  <div class="theme-panel-title">Choose Theme</div>
  <div class="theme-option active" data-theme="paper" onclick="setTheme('paper',this)">
    <div class="theme-swatch" style="background:linear-gradient(135deg,#faf7f2,#1a1209)"></div>Paper (Default)
  </div>
  <div class="theme-option" data-theme="night" onclick="setTheme('night',this)">
    <div class="theme-swatch" style="background:linear-gradient(135deg,#0f1923,#e8b84b)"></div>Night
  </div>
  <div class="theme-option" data-theme="ocean" onclick="setTheme('ocean',this)">
    <div class="theme-swatch" style="background:linear-gradient(135deg,#e8f4fd,#1565c0)"></div>Ocean
  </div>
  <div class="theme-option" data-theme="forest" onclick="setTheme('forest',this)">
    <div class="theme-swatch" style="background:linear-gradient(135deg,#f0f7f0,#2e7d32)"></div>Forest
  </div>
  <div class="theme-option" data-theme="sepia" onclick="setTheme('sepia',this)">
    <div class="theme-swatch" style="background:linear-gradient(135deg,#faf3e8,#8b4513)"></div>Sepia
  </div>
</div>
```

### Theme Switcher JS
```js
const STORAGE_THEME_KEY = 'lecture-theme'; // use a unique key per lecture file

let themePanelOpen = false;
function toggleThemePanel() {
  themePanelOpen = !themePanelOpen;
  document.getElementById('themePanel').classList.toggle('open', themePanelOpen);
}
function syncThemeOptions(theme) {
  document.querySelectorAll('.theme-option').forEach(function(option) {
    option.classList.toggle('active', option.dataset.theme === theme);
  });
}
function setTheme(theme, el, skipStorage) {
  if (theme === 'paper') {
    document.documentElement.removeAttribute('data-theme');
  } else {
    document.documentElement.setAttribute('data-theme', theme);
  }
  syncThemeOptions(theme);
  if (!skipStorage) localStorage.setItem(STORAGE_THEME_KEY, theme);
  setTimeout(() => {
    themePanelOpen = false;
    document.getElementById('themePanel').classList.remove('open');
  }, 300);
}
// Close panel on outside click
document.addEventListener('click', function(e) {
  const panel = document.getElementById('themePanel');
  const btn = document.getElementById('themeBtn');
  if (themePanelOpen && !panel.contains(e.target) && !btn.contains(e.target)) {
    themePanelOpen = false;
    panel.classList.remove('open');
  }
});
```

> **Upgrade from older version:** `setTheme()` now accepts a third `skipStorage` parameter and delegates active-class sync to `syncThemeOptions()`. The old approach of querying `.theme-option` inside `setTheme()` is replaced by this helper.

### Known Pitfall: Dark-Panel Components (`th`, `.exam-q`, `.hy-mini-table th`)

A handful of components are meant to **always** render as a dark card with light text, regardless of theme — table headers and the exam-question box are the two built-in examples. The tempting shortcut is `background: var(--ink); color: var(--paper);`, which works fine in every *light* theme (where `--ink` is dark and `--paper` is light) but **silently breaks in dark themes** like Night, where `--ink`/`--paper` are flipped — you end up with dark text on a dark background that's nearly invisible. This shipped as a real bug in one build before being caught by actually rendering the page rather than just reading the CSS.

**Fix:** give these "always-dark" components their own dedicated variable pair that does *not* swap direction with the theme, and set it explicitly per theme:

```css
:root            { --panel-dark-bg: #1a1209; --panel-dark-text: #faf7f2; }
[data-theme="night"]  { --panel-dark-bg: #101a26; --panel-dark-text: #eef5fb; }
[data-theme="ocean"]  { --panel-dark-bg: #0b2436; --panel-dark-text: #eef7fb; }
[data-theme="forest"] { --panel-dark-bg: #16241a; --panel-dark-text: #f2f7f0; }
[data-theme="sepia"]  { --panel-dark-bg: #3a2414; --panel-dark-text: #f7ecd9; }
```

Then use `background: var(--panel-dark-bg); color: var(--panel-dark-text);` on `th`, `.exam-q`, and `.hy-mini-table th` instead of `var(--ink)`/`var(--paper)`. For light themes this pair is just a copy of that theme's `--ink`/`--paper` values (no visual change); for dark themes it's a fixed dark navy/light text pair independent of the flip. **Always spot-check `.exam-q` and a `<table>` header in every theme after writing palettes** — this is the single most common way a theme silently breaks.

### Contrast Checklist for New Themes

Four light themes (Paper, Ocean, Forest, Sepia) were originally shipped with too little contrast between the page background and callout/card backgrounds — everything read as flat and washed out compared to Night, which naturally has more perceptual separation between its near-black page and dark-navy cards. When writing a new theme's palette, check each of these before considering it done:

1. **`--cream` must be clearly, not subtly, different from `--paper`.** Hold them side by side — if you have to squint, deepen `--cream`'s saturation/value gap.
2. **Callout backgrounds (`--highlight`, `--blue-bg`, `--green-bg`, `--red-bg`, `--purple-bg`) need real separation from `--paper`**, not just a 3–5% lightness nudge. Aim for backgrounds that read as a genuine tinted color, not a paper-colored box with a colored border doing all the work.
3. **`--accent2` (used for links and `<strong>` text) must have strong contrast against both `--ink` and every callout background it appears on.** This is where Sepia broke — its `--accent2` was a brown close enough to `--ink` that bold/link text nearly disappeared into body text. Don't default a theme's accent2 to a same-family color as ink; pick a hue that contrasts (e.g. a teal-blue works even in a warm brown Sepia theme).
4. **`.drug-card` should use `var(--cream)`, not `var(--paper)`, as its background** (see Section 5.12) — otherwise drug cards blend into the page in every light theme and only Night (which had a manual per-theme override) looked layered.
5. Give each theme actual color *personality* tied to its name instead of reusing the same blue for "concept" callouts everywhere — e.g. Ocean's concept callout can lean teal, Forest's can lean toward a mossy green-blue, Sepia's toward a vintage muted teal-ink — while keeping the same semantic role (concept = a cool color, warning = red-family, clinical = green-family, key = gold/yellow, purple = purple) so the callout system stays predictable across themes.
6. After writing a palette, **render it** (screenshot or open in a browser) rather than reasoning about hex codes in the abstract — several of these issues were only obvious once actually seen on screen.

### Reference Palette (contrast-tuned, copy directly for new files)

```css
:root {
  --ink: #1a1209; --paper: #faf7f2; --cream: #ece1cd;
  --accent: #b5341a; --accent2: #2c5f8a; --gold: #c9922a; --muted: #6b5e4e; --border: #d4cabb;
  --highlight: #fbe4a0; --highlight2: #cfe4f7; --green-bg: #d7f0da; --red-bg: #f8d6d0;
  --blue-bg: #d2e7f9; --purple-bg: #e6dbfa; --hero-bg: #1a1209;
  --panel-dark-bg: #1a1209; --panel-dark-text: #faf7f2;
}
[data-theme="night"] {
  --ink: #e0e8f0; --paper: #0f1923; --cream: #162030;
  --accent: #e8b84b; --accent2: #4aa8d8; --gold: #e8b84b; --muted: #94abc0; --border: #1e3048;
  --highlight: #3a3016; --highlight2: #12283a; --green-bg: #10281c; --red-bg: #2e1616;
  --blue-bg: #10233a; --purple-bg: #201a38; --hero-bg: #070e15;
  --panel-dark-bg: #101a26; --panel-dark-text: #eef5fb;
}
[data-theme="ocean"] {
  --ink: #0b2436; --paper: #eef7fb; --cream: #cdeaf5;
  --accent: #d1495b; --accent2: #0f6fb0; --gold: #d9a441; --muted: #4f7185; --border: #a8d4e8;
  --highlight: #ffe6ad; --highlight2: #bfe3f2; --green-bg: #c9f0dc; --red-bg: #fad9d5;
  --blue-bg: #c3e4f6; --purple-bg: #e1d7f6; --hero-bg: #0a3a5c;
  --panel-dark-bg: #0b2436; --panel-dark-text: #eef7fb;
}
[data-theme="forest"] {
  --ink: #16241a; --paper: #f2f7f0; --cream: #d7ead2;
  --accent: #a3401f; --accent2: #1f7a4d; --gold: #b8860b; --muted: #52684f; --border: #b7d4ae;
  --highlight: #f3e6a0; --highlight2: #cbe4c4; --green-bg: #c7ecc0; --red-bg: #f7ddd0;
  --blue-bg: #cbe6df; --purple-bg: #e1dbee; --hero-bg: #12301c;
  --panel-dark-bg: #16241a; --panel-dark-text: #f2f7f0;
}
[data-theme="sepia"] {
  --ink: #3a2414; --paper: #f7ecd9; --cream: #ecd7ae;
  --accent: #9c3b17; --accent2: #2f5f6b; --gold: #8b5a17; --muted: #7a614a; --border: #d9bd8c;
  --highlight: #f0d38a; --highlight2: #d7c39a; --green-bg: #dbe3bc; --red-bg: #f0d0c0;
  --blue-bg: #cfdedd; --purple-bg: #e3d3e0; --hero-bg: #3f2814;
  --panel-dark-bg: #3a2414; --panel-dark-text: #f7ecd9;
}
```

`--hero-heading`, `--hero-sub`, `--hero-meta-*`, `--floating-ui-*`, and `--quiz-overlay*` still need to be set per theme as before (unchanged pattern from the example above) — only the core palette and the new `--panel-dark-*` pair are shown here for brevity.

> **Also remove this dead rule if you find it copied from an older file:** `:root strong { color: var(--accent2); }` placed *after* `[data-theme] strong { color: var(--gold); }` in the stylesheet silently cancels the gold override in every theme, because `:root strong` matches unconditionally with equal specificity and wins by source order. Keep a single `strong { color: var(--accent2); }` rule and delete both of the others — simpler and it avoids this trap entirely.

---

## 4. Overall Page Structure

```
<body>
  .hero                ← dark hero header with title + meta stats (+ optional High-Yield button)
  .toc-bar             ← sticky top nav with anchor links
  [.section × N]       ← one per LO topic
  .hy-modal            ← optional: High-Yield One-Pager overlay (Section 12), hidden by default
  .lightbox            ← full-screen image overlay
  .floating-stack      ← fixed bottom-right: Font Size control + Theme switcher
  .theme-panel         ← popup above controls; hidden by default
  <footer>
  <script>             ← theme switcher + table quiz + lightbox (+ One-Pager logic if used)
```

> Note: an older version of this template used a `.quiz-score-bar` / `.quiz-panel` pair of fixed global elements for the table quiz feature. That's been replaced entirely — see Section 7, "Architecture note."

---

## 5. Component Reference

### 5.1 Hero Block
Dark background (`var(--ink)`), large serif title, subtitle, and a row of stat chips.

```html
<div class="hero">
  <div class="container">
    <div class="hero-tag">Instructor · Institution Name</div>
    <h1>Topic of <span>Lecture</span></h1>      <!-- span gets --accent color -->
    <p class="hero-sub">Short description.</p>
    <!-- Optional: <button class="hy-btn" onclick="openHY()">🎯 High-Yield One-Pager</button> — see Section 12 -->
    <div class="hero-meta">
      <div class="hero-meta-item">
        <span class="label">STAT LABEL</span>
        <span class="value">Stat Value</span>
      </div>
      <!-- repeat hero-meta-item as needed -->
    </div>
  </div>
</div>
```

### 5.2 Sticky TOC Bar
Horizontal scrolling nav, one anchor link per section.

```html
<div class="toc-bar">
  <nav>
    <a href="#section-id">Section Name</a>
  </nav>
</div>
```

### 5.3 Section Wrapper
Each topic is a `.section` with a `.container` inside.

```html
<div class="section" id="section-id">
  <div class="container">

    <div class="badge-row">
      <div class="lo-badge">LO N — Short Objective Name</div>
    </div>
    <p class="section-label">Category Label</p>
    <h2 class="section-title">Full Section Title</h2>

    <p>Introductory paragraph...</p>

    <!-- Use components below as needed -->

  </div>
</div>
```

**Note:** When displaying multiple badges together, wrap them in a `<div class="badge-row">` (flex container with gap). For a single badge you can use it unwrapped.

### 5.4 Callout Boxes
Five flavors. All share the `.callout` base class plus a modifier:

| Modifier | Color | Use for |
|---|---|---|
| `callout-key` | Yellow | Key concept or definition |
| `callout-concept` | Blue | Mechanism or theory |
| `callout-clinical` | Green | Clinical pearl or application |
| `callout-warning` | Red | Pitfall, exception, or danger |
| `callout-purple` | Purple | Special/nuanced concept |

```html
<div class="callout callout-key">
  <div class="callout-title">🔑 Title of Callout</div>
  <p>Content goes here.</p>
</div>
```

### 5.5 Box Warning (FDA Boxed Warning)
A distinct component for US Boxed Warnings — heavier border treatment than a standard callout, with a bold label block. Do not use `.callout-warning` for Boxed Warnings; use `.box-warning` instead.

```html
<div class="box-warning">
  <span class="bw-label">☐ US Boxed Warnings</span>
  <p><strong>1. Warning text here.</strong> Explanation.<br>
  <strong>2. Second warning.</strong> Explanation.</p>
</div>
```

### 5.6 Compare Grid (Two-Column Cards)
Side-by-side contrast. Built-in `.antiresorptive` (blue gradient) and `.anabolic` (green gradient) presets for pharmacology content. Custom gradient overrides work inline too.

```html
<div class="compare-grid">
  <div class="compare-card antiresorptive">
    <span class="card-emoji">🛡️</span>
    <h4>Antiresorptive (Preservation)</h4>
    <p>Description here.</p>
    <ul class="notes-list">
      <li>Point 1</li>
    </ul>
  </div>
  <div class="compare-card anabolic">
    <span class="card-emoji">🏗️</span>
    <h4>Anabolic (Formation)</h4>
    <p>Description here.</p>
    <ul class="notes-list">
      <li>Point 1</li>
    </ul>
  </div>
</div>
```

For other color combos (e.g. agonist vs. antagonist), override with inline `style` on `.compare-card`:

```html
<div class="compare-card" style="background: var(--green-bg); border-color: #2e7d32;">
```

> **Note:** The original `.gas`/`.brake` presets (oncogene analogy) are replaced in this lecture by `.antiresorptive`/`.anabolic`. Use whichever fits the content, or use inline overrides for anything else.

### 5.7 Numbered Step List
Auto-numbered steps with red circle counters.

```html
<ol class="step-list">
  <li>
    <div>
      <strong>Step Name</strong>
      Description of this step.
    </div>
  </li>
</ol>
```

### 5.8 Notes List (Bulleted)
Replaces default `<ul>` with styled `›` bullets.

```html
<ul class="notes-list">
  <li>First point</li>
  <li>Second point with <strong>emphasis</strong></li>
</ul>
```

### 5.9 Table
Standard HTML `<table>`. `<th>` gets dark background automatically; every even row gets cream background. No extra classes needed. **Tables also participate in the Table Quiz system** — columns can be hidden and revealed interactively.

```html
<table>
  <tr><th>Column A</th><th>Column B</th><th>Column C</th></tr>
  <tr><td>Data</td><td>Data</td><td>Data</td></tr>
</table>
```

### 5.10 Exam Question Block
Dark card with a hidden/revealed answer. The red "EXAM Q" label is injected via CSS `::before`.

```html
<div class="exam-q">
  <p><strong>Q:</strong> Write the question here.</p>
  <div class="answer">
    <div class="label">Answer</div>
    <p>Write the answer here with <strong>key terms bolded</strong>.</p>
  </div>
</div>
```

### 5.11 Slide Image + Caption
Images use `.slide-img` and are automatically wired to the click-to-zoom lightbox by the JS at the bottom of the file. Always add a `.slide-caption` below.

```html
<img src="path/to/slide.png" alt="Description of image content" class="slide-img">
<p class="slide-caption">Slide N — Title of Slide</p>
```

#### Option A — Relative path (simplest, but file must travel with the HTML)
Point `src` at a file next to (or in a subfolder of) the HTML file. The page will only display correctly if the image file is present in the same relative location.

```html
<img src="slides/slide-04-cell-cycle.png" alt="Cell cycle diagram" class="slide-img">
<p class="slide-caption">Slide 4 — Cell Cycle Overview</p>
```

This is fine while working locally, but **breaks if you send the HTML file without the images folder**.

#### Option B — Base64 inline (self-contained, recommended for sharing)
Embed the image data directly in the `src` attribute. The file becomes larger but is completely portable — one file, no dependencies.

**How to get the base64 string:**

*In a terminal (macOS/Linux):*
```bash
base64 -i slide-04.png | tr -d '\n'
```

*In Python (any OS):*
```python
import base64
with open("slide-04.png", "rb") as f:
    print(base64.b64encode(f.read()).decode())
```

*In a browser console (if you already have the file open):*
```js
// Paste this into DevTools console after dragging the image into a tab
const img = document.querySelector('img');
const canvas = document.createElement('canvas');
canvas.width = img.naturalWidth; canvas.height = img.naturalHeight;
canvas.getContext('2d').drawImage(img, 0, 0);
console.log(canvas.toDataURL('image/png'));
```

**Then paste the result into the HTML:**
```html
<img
  src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."
  alt="Cell cycle diagram"
  class="slide-img"
>
<p class="slide-caption">Slide 4 — Cell Cycle Overview</p>
```

Use `image/jpeg` for JPEGs and `image/webp` for WebP files:
```html
src="data:image/jpeg;base64,/9j/4AAQSkZJRgAB..."
src="data:image/webp;base64,UklGRlAA..."
```

#### Option C — Paste a screenshot directly (Claude workflow)
If you're asking Claude to build the notes file, you can paste or upload screenshots of lecture slides directly in the chat. Claude will embed them as base64 automatically and place them with the correct `.slide-img` + `.slide-caption` markup.

#### Sizing and layout notes
- `.slide-img` is `width: 100%` by default — it fills the content column (max 860px)
- To display two images side by side, wrap them in a flex container:

```html
<div style="display:flex; gap:16px; margin:16px 0;">
  <div style="flex:1;">
    <img src="..." alt="..." class="slide-img" style="margin:0;">
    <p class="slide-caption">Slide 3A</p>
  </div>
  <div style="flex:1;">
    <img src="..." alt="..." class="slide-img" style="margin:0;">
    <p class="slide-caption">Slide 3B</p>
  </div>
</div>
```

- To constrain a small image to half-width, use `style="width:50%;"` on the `<img>`
- The lightbox always shows the image at its natural size (up to 92vw / 88vh), so high-resolution source images zoom in nicely

### 5.12 Drug Grid / Drug Card
Auto-fit card grid for listing individual drugs within a class. Similar visual structure to the Hallmarks Grid, but with a blue top border and a `.generic` subtitle line for dosing/route info. Use one `.drug-card` per drug.

```html
<div class="drug-grid">
  <div class="drug-card">
    <h4>Drug Name</h4>
    <div class="generic">Route / dosing schedule</div>
    <p style="font-size:0.83rem; margin-top:6px; color:var(--muted);">Key distinguishing clinical note</p>
  </div>
  <!-- repeat per drug -->
</div>
```

```css
.drug-card { border: 1px solid var(--border); border-top: 4px solid var(--accent2);
  border-radius: 10px; padding: 14px 16px; background: var(--cream); }
```

> **Use `var(--cream)`, not `var(--paper)`, for the card background.** Since `.drug-card` sits directly on the page background, giving it the same color as the page (`--paper`) makes it blend in with no visual separation except the border — this was a real bug that made drug cards look flat in every light theme. `--cream` is deliberately a step darker/more tinted than `--paper` in every theme (see Section 3's contrast checklist), so using it here gives the card genuine visual layering without needing a per-theme override.

A single card can span the full row with `style="grid-column: span 2;"` when there's only one drug in a class.

### 5.13 Hallmarks Grid
Auto-fit card grid. Each card gets a different top-border color cycling through accents (applied via `:nth-child` in CSS — no classes needed). Use for enumerated concepts like disease hallmarks or functional roles.

```html
<div class="hallmarks-grid">
  <div class="hallmark-card">
    <div class="hallmark-num">1</div>
    <h4>Hallmark Name</h4>
    <p>Brief description of this hallmark.</p>
  </div>
  <!-- repeat up to ~8 cards -->
</div>
```

### 5.14 p53 Function Grid
Small icon cards for listing functional roles.

```html
<div class="p53-grid">
  <div class="p53-card">
    <div class="icon">🛑</div>
    <h4>Function Name</h4>
    <p>One sentence explanation.</p>
  </div>
</div>
```

### 5.15 Tech Card
Larger card for describing a technology or test (e.g. FISH, PCR, MammaPrint).

```html
<div class="tech-card">
  <h4>Technology Name</h4>
  <p>Description. Mechanism. Clinical use.</p>
  <ul class="notes-list">
    <li>Key fact 1</li>
  </ul>
</div>
```

### 5.16 REMS Badge
Inline purple badge for calling out FDA Risk Evaluation and Mitigation Strategy (REMS) requirements. Place immediately after the drug name or within a sentence.

```html
Denosumab <span class="rems-badge">REMS</span>
```

### 5.17 Potency Bar
Visual horizontal bar for representing relative potency. Set width as a percentage of some maximum in the series.

```html
<div class="potency-bar">
  <div class="potency-fill" style="width: 70%;"></div>
  <span>Drug Name — Relative potency: 2,000×</span>
</div>
```

### 5.17 Font Size Control
A floating A+/A− control rendered as part of the fixed `.floating-stack` (bottom-right, alongside the Theme switcher). Adjusts `document.body.style.fontSize` between 12px and 24px. No external state — resets to 16px on page reload.

```html
<!-- Inside .floating-stack, above the theme-btn -->
<div class="font-btn-row">
  <span class="font-label">Text</span>
  <button class="font-btn" onclick="changeFontSize(1)" title="Increase font size">A+</button>
  <span class="font-sep">|</span>
  <button class="font-btn" onclick="changeFontSize(-1)" title="Decrease font size">A−</button>
</div>
```

```css
.font-btn-row { display: flex; align-items: center; background: var(--floating-ui-bg);
  color: var(--floating-ui-fg); padding: 7px 10px; border-radius: 30px;
  box-shadow: var(--floating-ui-shadow); font-family: 'JetBrains Mono', monospace;
  font-size: 0.62rem; letter-spacing: 0.1em; gap: 2px; }
.font-btn { background: none; border: none; cursor: pointer; color: var(--floating-ui-fg);
  font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 1rem;
  padding: 2px 8px; border-radius: 6px; transition: background 0.15s; line-height: 1; }
.font-btn:hover { background: rgba(255,255,255,0.18); }
.font-sep { color: rgba(255,255,255,0.2); padding: 0 3px; }
.font-label { font-size: 0.58rem; opacity: 0.7; padding: 0 5px;
  text-transform: uppercase; letter-spacing: 0.1em; }
```

```js
let currentFontSize = 16;
function changeFontSize(delta) {
  currentFontSize = Math.min(24, Math.max(12, currentFontSize + delta));
  document.body.style.fontSize = currentFontSize + 'px';
}
```

### 5.18 Inline Text Elements (Domain-Specific)
Two inline elements for genetics/genomics content. Can be adapted for other domains.

```html
<!-- SNP identifier chip — monospaced, cream background -->
<span class="snp-code">rs2736098</span>

<!-- Gene name — blue, monospaced, slightly smaller -->
<span class="gene-tag">TP53</span>
```

```css
.snp-code { font-family: 'JetBrains Mono', monospace; background: var(--cream);
  border: 1px solid var(--border); padding: 2px 7px; border-radius: 4px; font-size: 0.82rem; }
.gene-tag { font-family: 'JetBrains Mono', monospace; color: var(--accent2);
  font-size: 0.88rem; font-weight: 500; }
```

> These are deliberately un-themed (they inherit well from variable-based colors), so no per-theme overrides are needed. Adapt names for other domains — e.g. `.drug-code`, `.pathway-tag`.

### 5.19 Floating Controls Stack (fixed bottom-right)

Font Size control and Theme switcher live together in one fixed stack. If the file also has a High-Yield One-Pager (Section 12), its button lives in the hero instead, not in this stack.

```html
<div class="floating-stack">
  <div class="theme-panel" id="themePanel">
    <!-- see Section 3 Theme Switcher HTML -->
  </div>
  <div class="font-btn-row">
    <span class="font-label">Text</span>
    <button class="font-btn" onclick="changeFontSize(1)" title="Increase font size">A+</button>
    <span class="font-sep">|</span>
    <button class="font-btn" onclick="changeFontSize(-1)" title="Decrease font size">A−</button>
  </div>
  <button class="theme-btn" id="themeBtn" onclick="toggleThemePanel()" title="Switch theme">
    <span>🎨</span>
    <span>Theme</span>
  </button>
</div>
```

```css
.floating-stack { position: fixed; bottom: 20px; right: 20px; z-index: 100;
  display: flex; flex-direction: column; align-items: flex-end; gap: 10px; }
```

### Persistence: restoring theme on load
Call `initVisualState()` on `DOMContentLoaded` to restore the saved theme from `localStorage`:

```js
function initVisualState() {
  var savedTheme = localStorage.getItem(STORAGE_THEME_KEY) || 'paper';
  setTheme(savedTheme, null, true); // skipStorage=true avoids re-writing same value
}
document.addEventListener('DOMContentLoaded', function() {
  initVisualState();
  initTableQuiz(); // see Section 7
});
```

> **Storage key naming:** Use a unique key per lecture file (e.g. `'harrison-cancer-genomics-theme'`) so that different lecture files don't overwrite each other's saved state.

---

## 7. Table Quiz System

An interactive self-testing feature. A quiz toolbar (`.tq-bar`) is **automatically injected above every `<table>` by JavaScript** — no manual HTML needed. Users select columns to hide, start the quiz, then click blurred cells to reveal answers one by one.

### How it works (per-table inline approach)
1. On `DOMContentLoaded`, `initTableQuiz()` loops over all `<table>` elements
2. For each table it injects a `.tq-bar` directly above the table in the DOM
3. User clicks **🧩 Quiz this table** → column name buttons appear
4. User selects which columns to hide → **▶ Start** button enables
5. On Start: selected column cells are wrapped in `.tq-cell-content` (content blurred) and the cell gets `.quiz-hidden-cell` class + a "tap to reveal" overlay
6. Clicking a hidden cell removes the class and restores the original HTML
7. A live `N / total revealed` score shows in the toolbar; displays 🎉 on completion
8. **↺ Reset** restores all cells and returns the toolbar to its initial state

### Required CSS
```css
/* Inline quiz toolbar — injected above each table */
.tq-bar { display: flex; align-items: center; flex-wrap: wrap; gap: 8px;
  margin-bottom: 6px; padding: 8px 12px; background: var(--cream);
  border: 1px solid var(--border); border-radius: 8px; }
.tq-toggle { font-family: 'JetBrains Mono', monospace; font-size: 0.65rem;
  letter-spacing: 0.1em; text-transform: uppercase; background: var(--accent2);
  color: #fff; border: none; border-radius: 20px; padding: 5px 12px; cursor: pointer; }
.tq-toggle.active { background: var(--accent); }
.tq-cols { display: flex; flex-wrap: wrap; gap: 5px; flex: 1; }
.tq-col-btn { font-size: 0.72rem; padding: 3px 9px; border: 1px solid var(--border);
  border-radius: 12px; background: var(--paper); cursor: pointer;
  font-family: 'JetBrains Mono', monospace; transition: all 0.15s; }
.tq-col-btn.sel { background: var(--accent2); color: #fff; border-color: var(--accent2); }
.tq-start { font-family: 'JetBrains Mono', monospace; font-size: 0.65rem;
  background: #2e7d32; color: #fff; border: none; border-radius: 20px; padding: 5px 12px; cursor: pointer; }
.tq-start:disabled { opacity: 0.35; cursor: not-allowed; }
.tq-reset { font-family: 'JetBrains Mono', monospace; font-size: 0.65rem;
  background: #b5341a; color: #fff; border: none; border-radius: 20px; padding: 5px 13px; cursor: pointer; }
.tq-score { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: var(--muted); }
.tq-score.done { color: #2e7d32; font-weight: 700; }

/* Hidden cell: content blurred, overlay shows "tap to reveal" */
.quiz-hidden-cell { position: relative !important; cursor: pointer !important; }
.quiz-hidden-cell .tq-cell-content { filter: blur(5px) !important; user-select: none !important;
  pointer-events: none !important; opacity: 0.4 !important; }
.quiz-hidden-cell::after { content: 'tap to reveal' !important; position: absolute !important;
  inset: 0 !important; display: flex !important; align-items: center !important;
  justify-content: center !important; background: var(--quiz-overlay) !important;
  color: #fff !important; font-family: 'JetBrains Mono', monospace !important;
  font-size: 0.6rem !important; font-weight: 700 !important; letter-spacing: 0.12em !important;
  text-transform: uppercase !important; border-radius: 4px !important; }
.quiz-hidden-cell:hover::after { background: var(--quiz-overlay-hover) !important; }
```

The toolbar already uses theme-aware variables (`--cream`, `--border`, `--paper`, `--accent2`), so it automatically adapts to whichever theme is active — no per-theme overrides needed.

### No special markup needed on tables
The quiz JS automatically queries all `<table>` elements. No classes or `data-` attributes are required. Column labels are read from `<th>` text content.

### JS (Table Quiz — call `initTableQuiz()` from `DOMContentLoaded`)
`initTableQuiz()` is ~130 lines. It creates per-table state (selectedCols Set, hiddenCells Map, running flag, score counters) and builds the entire `.tq-bar` DOM dynamically. Copy the full function from the source file — key functions inside: `toggleBtn.onclick`, `startBtn.onclick`, `resetBtn.onclick`, `updateScore()`.

> **Architecture note:** This replaces the older global `.quiz-panel` / `.quiz-score-bar` approach. There is no longer a single quiz panel or a quiz button in the floating controls — everything is self-contained per table.

---

## 8. Lightbox (Click-to-Zoom Images)

```html
<!-- Place once before </body> -->
<div class="lightbox" id="lightbox" aria-hidden="true">
  <img id="lightboxImg" alt="Zoomed slide image">
</div>
```

```js
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightboxImg');

function openLightbox(img) {
  lightboxImg.src = img.src;
  lightbox.classList.add('active');
  lightbox.setAttribute('aria-hidden', 'false');
}
function closeLightbox() {
  lightbox.classList.remove('active');
  lightbox.setAttribute('aria-hidden', 'true');
  lightboxImg.src = '';
}
document.querySelectorAll('.slide-img').forEach(img => {
  img.addEventListener('click', () => openLightbox(img));
});
lightbox.addEventListener('click', closeLightbox);
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeLightbox();
});
```

---

## 9. Section Checklist

When adding a new topic section, go through this checklist:

- [ ] `.section` has a unique `id` (for TOC anchor)
- [ ] TOC link added in `.toc-bar nav`
- [ ] Section has a `.lo-badge` (wrap in `.badge-row` if more than one)
- [ ] At least one callout box used per major concept
- [ ] At least one exam question (`exam-q`) per section
- [ ] Use `.box-warning` (not `.callout-warning`) for any US Boxed Warnings
- [ ] Drug sections use `.drug-grid` + `.drug-card` to list individual agents
- [ ] Add `.rems-badge` inline for any drug with an FDA REMS program

When setting up a new lecture file:

- [ ] `STORAGE_THEME_KEY` constant is unique to this file
- [ ] `initVisualState()` and `initTableQuiz()` both called in `DOMContentLoaded`
- [ ] All theme variable groups overridden in each `[data-theme="..."]` block, **plus the `--panel-dark-bg`/`--panel-dark-text` pair (Section 3)**
- [ ] After writing/copying theme palettes, **render each theme and check an `.exam-q` box and a `<table>` header specifically** — this is where dark-theme bugs hide (Section 3)
- [ ] Decide whether this file gets a High-Yield One-Pager (Section 12) — optional, build it only if the user wants a condensed pre-exam summary
- [ ] If using the One-Pager: `.hy-mini-table` excluded from `initTableQuiz()`, print output actually tested (Section 12.6), not just assumed to work

---

## 10. Adapting for a New Lecture

1. **Update the hero** — new title, instructor, institution, relevant stats
2. **Add/remove sections** — one `<div class="section">` per LO
3. **Pick the right components** — use drug grids for drug class breakdowns, compare grids for binary contrasts, step lists for processes, hallmark grids for enumerated concepts, p53 grid for function lists
4. **Keep the color system** — don't introduce new colors; map new content onto existing callout types. Use `.box-warning` for regulatory/safety warnings, `.callout-warning` for clinical pitfalls.
5. **Theme system is plug-and-play** — copy the full theme CSS block (all variable groups, including `--panel-dark-bg`/`--panel-dark-text`) and JS verbatim; no edits needed per lecture. Still worth a quick visual spot-check per theme (Section 3).
6. **Change the localStorage key** — update the `STORAGE_THEME_KEY` constant to a unique per-lecture string so different files don't share state
7. **Table Quiz is automatic** — `initTableQuiz()` requires no per-table setup; just include it and call it from `DOMContentLoaded`
8. **Font size control** — copy the `.font-btn-row` HTML and `changeFontSize()` JS verbatim; no edits needed
9. **If building the High-Yield One-Pager** — draft its content only after the full notes are otherwise done, since it's meant to be a condensed extraction of the real content, not written independently (Section 12)

---

## 11. File Delivery

- Single `.html` file, no external dependencies except Google Fonts CDN
- Works offline if fonts are cached
- No framework, no build step — just open in a browser
- **Images:** use base64-embedded `src` for true portability (one file, zero broken images); use relative paths only if the image folder will always travel with the HTML — see Section 5.11 for the full workflow

---

## 12. High-Yield One-Pager (Optional Feature)

An optional condensed-summary feature (see Section 1). A **self-contained modal** with its own hand-written, dense, LO-organized summary — plus a working Print/Save-PDF button that outputs a clean 1–2 page document, not the whole 30+ page file.

### 12.1 The Button (place in the hero, high visibility)

```html
<p class="hero-sub">Short description.</p>
<button class="hy-btn" onclick="openHY()">🎯 High-Yield One-Pager</button>
<div class="hero-meta">...</div>
```

```css
.hy-btn { display: inline-flex; align-items: center; gap: 8px; background: var(--gold);
  color: #2a1a00; border: none; padding: 12px 22px; border-radius: 30px;
  font-family: 'JetBrains Mono', monospace; font-size: .78rem; font-weight: 700;
  letter-spacing: .04em; cursor: pointer; margin-top: 4px;
  box-shadow: 0 4px 14px rgba(0,0,0,0.3); transition: transform .15s, box-shadow .15s; }
.hy-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(0,0,0,0.35); }
```

### 12.2 Modal Structure

Place once before `</body>`, alongside the lightbox:

```html
<div class="hy-modal" id="hyModal">
  <div class="hy-modal-card">
    <div class="hy-modal-header">
      <h2>🎯 [Lecture Topic] — High-Yield One-Pager</h2>
      <div class="hy-modal-actions">
        <button class="hy-action-btn" onclick="printHY()">🖨️ Print / Save PDF</button>
        <button class="hy-action-btn hy-close-btn" onclick="closeHY()">✕ Close</button>
      </div>
    </div>
    <p class="hy-subhead">Condensed by learning objective — LO1 ... · LO2 ... · LO3 ...</p>

    <div class="hy-cols">
      <div> <!-- Column 1: LO1 -->
        <span class="hy-lo-tag">LO 1 · [NAME]</span>
        <div class="hy-block">
          <h4>Block Title</h4>
          <ul><li><strong>Term:</strong> compressed fact</li></ul>
        </div>
        <!-- repeat hy-block per topic cluster, 3-5 blocks per column -->
      </div>
      <div> <!-- Column 2: LO2 --> ... </div>
      <div> <!-- Column 3: LO3 --> ... </div>
    </div>

    <!-- Optional: full-width appendix table, e.g. a master drug reference -->
    <div class="hy-block" style="margin-top:4px;">
      <h4>Master Drug Reference — Generic, Brand, MOA, Indications, Contraindications</h4>
      <table class="hy-mini-table">
        <tr><th>Generic (Brand)</th><th>Class</th><th>MOA</th><th>Key Indications</th><th>Key Contraindications</th></tr>
        <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
      </table>
    </div>
  </div>
</div>
```

The 3-column grid is one `<div>` per learning objective (not per topic) — this is the whole point of the feature, so don't organize it by section instead. A full-width block (outside `.hy-cols`, as a sibling after it, still inside `.hy-modal-card`) is the right place for one comprehensive appendix table, like a master drug list, that doesn't belong to a single LO.

### 12.3 CSS

```css
.hy-modal { position: fixed; inset: 0; background: rgba(0,0,0,0.75); z-index: 300;
  display: none; align-items: flex-start; justify-content: center; overflow-y: auto; padding: 30px 16px; }
.hy-modal.open { display: flex; }
.hy-modal-card { background: var(--paper); color: var(--ink); max-width: 1000px; width: 100%;
  border-radius: 14px; padding: 26px 30px 34px; position: relative; box-shadow: 0 20px 60px rgba(0,0,0,0.45); }
.hy-modal-header { display: flex; align-items: center; justify-content: space-between; gap: 12px;
  margin-bottom: 14px; border-bottom: 3px solid var(--accent2); padding-bottom: 10px; flex-wrap: wrap; }
.hy-modal-actions { display: flex; gap: 8px; flex: none; }
.hy-action-btn { font-family: 'JetBrains Mono', monospace; font-size: .66rem; letter-spacing: .05em;
  text-transform: uppercase; border: 1px solid var(--border); background: var(--cream); color: var(--ink);
  padding: 7px 13px; border-radius: 20px; cursor: pointer; }
.hy-close-btn { background: var(--accent); color: #fff; border: none; }
.hy-subhead { font-family: 'JetBrains Mono', monospace; font-size: .68rem; color: var(--muted); margin: 0 0 14px; }

.hy-cols { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
@media (max-width: 760px) { .hy-cols { grid-template-columns: 1fr; } }
.hy-block { border: 1px solid var(--border); border-radius: 8px; padding: 9px 11px;
  background: var(--cream); margin-bottom: 10px; }
.hy-block h4 { margin: 0 0 6px; font-size: .78rem; color: var(--accent2);
  border-bottom: 1px solid var(--border); padding-bottom: 4px; }
.hy-block p, .hy-block li { font-size: .68rem; line-height: 1.4; margin: 0 0 4px; }
.hy-lo-tag { display: block; font-family: 'JetBrains Mono', monospace; font-size: .62rem; font-weight: 700;
  color: #fff; background: var(--accent2); padding: 3px 9px; border-radius: 10px; margin-bottom: 8px;
  letter-spacing: .05em; text-align: center; }
.hy-mini-table { width: 100%; border-collapse: collapse; font-size: .65rem; margin-top: 4px; }
.hy-mini-table th, .hy-mini-table td { border: 1px solid var(--border); padding: 3px 5px; text-align: left; line-height: 1.3; }
.hy-mini-table th { background: var(--panel-dark-bg); color: var(--panel-dark-text); font-size: .58rem; text-transform: uppercase; }
```

### 12.4 JS

```js
function openHY() {
  document.getElementById('hyModal').classList.add('open');
  document.body.classList.add('hy-mode');
  document.body.style.overflow = 'hidden';
}
function closeHY() {
  document.getElementById('hyModal').classList.remove('open');
  document.body.classList.remove('hy-mode');
  document.body.style.overflow = '';
}
function printHY() { window.print(); }
document.addEventListener('DOMContentLoaded', function() {
  const hyModal = document.getElementById('hyModal');
  hyModal.addEventListener('click', function(e) { if (e.target === this) closeHY(); });
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && hyModal.classList.contains('open')) closeHY();
  });
});
```

**Exclude `.hy-mini-table` from the Table Quiz system** (Section 7) — the quiz toolbar injected above every table would clutter a dense printable reference. Add one guard line at the top of `initTableQuiz()`'s loop:

```js
document.querySelectorAll('table').forEach(function(table) {
  if (table.classList.contains('hy-mini-table')) return;  // <-- add this line
  // ... rest of function unchanged
});
```

### 12.5 Print CSS — the two mistakes to avoid

Getting the print output to be *just* the one-pager (not the whole 30-page document) took two iterations to get right:

**Mistake 1 — using `visibility: hidden` instead of `display: none`.** `visibility: hidden` hides an element visually but it still occupies its layout space, so the total page height used for print pagination stays the same as the full document — this produced **40 blank pages** on the first attempt. Always use `display: none` for anything meant to be excluded from the printed flow, not `visibility`.

**Mistake 2 — applying print rules unconditionally.** If `@media print` rules unconditionally hide the hero/sections/footer and show only `.hy-modal`, then printing the page *without opening the modal first* (e.g. a normal Ctrl+P to print the full notes) would incorrectly show only the one-pager instead of the full document. Fix: toggle a class on `<body>` from `openHY()`/`closeHY()` (`hy-mode` above) and scope every print rule to `body.hy-mode`, so print behavior depends on whether the modal is actually open:

```css
@media print {
  body.hy-mode .hero, body.hy-mode .toc-bar, body.hy-mode .section,
  body.hy-mode .lightbox, body.hy-mode .floating-stack, body.hy-mode footer { display: none !important; }
  body.hy-mode .hy-modal { position: static !important; inset: auto !important; background: none !important;
    padding: 0 !important; display: block !important; overflow: visible !important; }
  body.hy-mode .hy-modal-card { position: static !important; max-width: 100% !important; width: 100% !important;
    box-shadow: none !important; padding: 4px !important; }
  .hy-modal-actions, .tq-bar { display: none !important; }
  .hy-cols { grid-template-columns: repeat(3, 1fr); gap: 8px; }

  /* Shrink typography for print only — screen view stays at normal, readable size */
  .hy-modal-header h2 { font-size: 1.05rem; }
  .hy-subhead { font-size: .58rem; margin-bottom: 8px; }
  .hy-block { padding: 5px 7px; margin-bottom: 6px; }
  .hy-block h4 { font-size: .68rem; margin-bottom: 3px; padding-bottom: 2px; }
  .hy-block p, .hy-block li { font-size: .585rem; line-height: 1.28; margin-bottom: 2px; }
  .hy-mini-table { font-size: .555rem; }
  .hy-mini-table th, .hy-mini-table td { padding: 1.5px 3px; }
  .hy-lo-tag { font-size: .55rem; padding: 2px 7px; margin-bottom: 5px; }
}
```

The print-only font shrink at the bottom is optional and content-dependent — add it only if the one-pager's content overflows past 1 page in testing (see 12.6). It has no effect on the on-screen modal, which keeps its normal, comfortably readable size.

### 12.6 Verifying the print output actually works

**Do not just eyeball the CSS — actually render it.** If you have computer/browser tooling available, open the modal, switch to print media emulation, and export to PDF, then check the page count and read the rendered output:

```python
# Example verification approach (Playwright)
page.click(".hy-btn")
page.emulate_media(media="print")
page.pdf(path="onepager.pdf", format="Letter", print_background=True)
# then check page count (pdfinfo) and render to images to actually look at it
```

A 40-page PDF means Mistake 1 above; a full-document printout when the modal was never opened means Mistake 2. If the one-pager itself is fine but runs 2+ pages, either trim content or add the print-only font-size shrink from 12.5 — verify by re-running the export, don't assume a CSS tweak worked.

### 12.7 Content-Writing Guidance

- **Organize strictly by learning objective**, one column per LO (or merge into fewer/more columns if there are more or fewer than 3 LOs) — this is what makes it a "high-yield" page rather than just a shorter version of the full notes.
- Each `.hy-block` should be a tight cluster of 3–8 bullet points or a small table — mnemonics, duration/threshold tables, drug-class rankings, "gold standard" facts, and scenario→treatment quick-picks compress especially well.
- **Don't just rename class-level content — include the actual named drugs/entities.** A first pass that only lists "SSRI," "SNRI," "TCA" without naming sertraline/fluoxetine/etc. defeats the purpose of a differentiation-focused study aid; go back through the full document's drug-grid cards and pull the individual names and their one-line differentiators into the one-pager.
- End with the full-width master reference table (12.2) pulling together every named entity in the document (drug generic + brand, MOA, indications, contraindications, or the equivalent for non-pharm content) — this is worth doing even if it pushes the print output to 2 pages, since completeness matters more than a strict 1-page limit for this kind of appendix.
