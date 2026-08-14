# How to Recreate These Medical Study Notes
> Instructions for future Claude: how to build an HTML study notes page like `Osteoporosis_Pharmacology_Study_Notes.html`.

---

## 1. What These Notes Are

A single-file HTML study document for a medical school lecture, organized around Learning Objectives (LOs). It has one primary display mode, plus an optional condensed view:
- **Normal mode** — full notes covering all LOs for the lecture
- **High-Yield One-Pager** — an optional modal overlay that condenses the whole file into a dense, printable 1–2 page cheat sheet organized by learning objective, with its own Print/Save-PDF button (see Section 12)

The One-Pager is mandatory — build it when the user wants a condensed pre-exam summary; otherwise the full notes stand alone.

The page is self-contained: no build tools, no frameworks, just one `.html` file with embedded CSS, fonts, and JS.

> **Two variants now exist.** Sections 2–12 below are **Variant 1** — the original system, organized strictly by numbered Learning Objectives, with an 8-theme switcher (Paper/Night/Ocean/Forest/Sepia/Lavender/Rose/Slate) and a component vocabulary tuned for pharmacology/pathology content (drug grids, hallmark grids, REMS badges, potency bars). **Section 13 is Variant 2** — a lighter-weight system built for `Introduction_to_Therapy_Study_Notes.html`, better suited to lecture content that isn't cleanly split into 2–3 LOs: a single light/dark toggle instead of named themes, and a component vocabulary built around generic "modality cards," mnemonics, and click-to-reveal cases rather than drug-specific components. Both variants share the same underlying philosophy (self-contained file, base64 images, lightbox, table quiz, optional HY one-pager) — pick whichever fits the lecture's actual content shape, and don't mix components from both within one file. **Section 14 is the Study Tools System** — an optional active-recall/progress layer (Recall Mode, per-section reviewed/confidence tracking, TOC scrollspy, collapsible sections, next-question jumper, pinned compare strip, keyboard shortcuts) first built for `Eating_Disorders_Study_Notes.html` on top of Variant 1; it's designed as an add-on layer and can be applied to either variant.

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
Make sure these pages can be printable or exported as a pdf
add flavicon related to the lecture (can be from image from given class notes (preferred) or emoji
---

## 3. Theme System

The page supports 8 visual themes via a `data-theme` attribute on the `<html>` element. **Paper is the default** — it's what renders when no `data-theme` attribute is present, and it's the theme every file should load with before the person picks something else.

### Available Themes

| Theme | Key Colors | `data-theme` value |
|---|---|---|
| **Paper (Default)** | Warm cream + dark ink | *(no attribute — omit `data-theme` entirely)* |
| Night | Dark navy + gold/blue | `night` |
| Ocean | Light blue + deep navy | `ocean` |
| Forest | Soft green + deep green | `forest` |
| Sepia | Warm tan + brown | `sepia` |
| Lavender | Soft violet + deep purple | `lavender` |
| Rose | Blush pink + wine red / teal accent2 | `rose` |
| Slate | Cool gray + steel blue / burnt orange accent | `slate` |

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
[data-theme="lavender"] {
  --ink: #241a33; --paper: #f6f3fb; --cream: #e7def4;
  --accent: #b03a5b; --accent2: #6a4fa0; --gold: #b8862a; --muted: #6b5f80; --border: #d3c6e8;
  --highlight: #f3e2b0; --highlight2: #e0d2f4; --green-bg: #d8eedd; --red-bg: #f7d8dd;
  --blue-bg: #dcd8f6; --purple-bg: #e6dbfa; --hero-bg: #241a33;
  --panel-dark-bg: #241a33; --panel-dark-text: #f6f3fb;
}
[data-theme="rose"] {
  --ink: #33161f; --paper: #fdf3f5; --cream: #f7dde3;
  --accent: #b02444; --accent2: #2c6a72; --gold: #c07a2a; --muted: #84606c; --border: #ecc4cf;
  --highlight: #fbe4a8; --highlight2: #f4cfd9; --green-bg: #d7efdc; --red-bg: #f9d3d6;
  --blue-bg: #d3e8ec; --purple-bg: #ecd9ec; --hero-bg: #3a1220;
  --panel-dark-bg: #33161f; --panel-dark-text: #fdf3f5;
}
[data-theme="slate"] {
  --ink: #1c2229; --paper: #f4f5f7; --cream: #e3e7ec;
  --accent: #cf4520; --accent2: #33607a; --gold: #a8862a; --muted: #5c6a76; --border: #c8d0d8;
  --highlight: #f2e3ac; --highlight2: #d5e2ec; --green-bg: #d6ead9; --red-bg: #f4d8d0;
  --blue-bg: #d3e2ef; --purple-bg: #dfd9ec; --hero-bg: #1c2530;
  --panel-dark-bg: #1c2530; --panel-dark-text: #f4f5f7;
}
```

> **Contrast notes for the three newest themes:** all three are light themes, so pitfall #3 from the checklist applies directly. Rose deliberately uses a *teal* `--accent2` (#2c6a72) rather than a pink-family color so links/`<strong>` don't melt into the warm pink page; Slate does the same with a burnt-orange `--accent` (#cf4520) against its cool grays so warnings still pop. Lavender's `--accent2` is the purple itself (#6a4fa0), which is far enough from its near-black violet ink to hold contrast.

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

Font Size control and Theme switcher live together in one fixed stack. If the file also has a High-Yield One-Pager (Section 12), its button lives in the hero instead, not in this stack. If the file also has the Study Tools System (Section 14), its buttons live in a *separate* hover-expand menu fixed **bottom-left** — the two stacks never share a corner, so neither covers the other.

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

## 6. Layout Width & Viewport Scaling (16" MacBook Pro Target)

The content column width described in Section 5.11 (`.slide-img` fills a "max 860px" column) and Variant 2's `--maxw:920px` (Section 13.1) were both sized for a generic desktop layout, not tuned to any specific screen. In practice these files are read on a 16" MacBook Pro — a browser window on that screen is typically **~1400–1700px wide** in CSS pixels (native 3456×2234 / 2x scaling puts the default logical resolution around 1728×1117; a maximized or near-maximized browser window commonly sits in the 1400–1728px range). A ~860–920px centered content column on a viewport that wide leaves **large, wasted empty margins on both sides** — the page reads as narrow and letterboxed instead of filling the screen.

**When building or adapting a file, size the layout so it visually fills a 16" MacBook Pro browser window without much empty space on either side:**

- Widen the primary content container. Don't hardcode a single fixed `max-width` like `860px`; instead scale it to the viewport with something like:
  ```css
  .container { max-width: min(1200px, 94vw); margin: 0 auto; }
  ```
  1100–1300px reads as full and well-used on a 16" MacBook Pro while still keeping body text lines from getting uncomfortably long (long-line readability still matters for body paragraphs — don't stretch `<p>` text edge-to-edge; widen the *page*, not necessarily every text block).
- Grid-based components (`.drug-grid`, `.hallmarks-grid`, `.compare-grid`, `.p53-grid`, `.hy-cols`, `.rr-grid`, Variant 2's `.hy-grid`) should use `auto-fit`/`auto-fill` with a `minmax()` track size (e.g. `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));`) rather than a fixed column count — on a wide 16" screen this naturally produces more columns per row and uses the extra horizontal space, instead of leaving it blank beside a narrow fixed-width grid.
- The `.hero`, `.toc-bar`/`.topbar`, and any full-bleed background bands should span the full viewport width (`width: 100%`, no `max-width` cap) even while the text/content *inside* them stays constrained to the narrower reading column — this keeps the page feeling edge-to-edge rather than like a strip down the middle of the screen.
- Don't solve this by cranking up base font size or padding instead of widening the layout — that just makes existing content bigger without using the freed-up horizontal space, and can make a 16" viewport feel cramped vertically (more scrolling) instead of well-proportioned.
- **Test at realistic 16" MacBook Pro widths, not just a phone breakpoint and a generic 1280px "desktop" check.** Render (or resize a browser preview to) roughly **1512px** and **1728px** wide and confirm: the page doesn't look like a narrow column floating in empty space, grids gain extra columns rather than staying stuck at 2–3, and nothing that was fine at 1280px overflows or looks stretched/thin at these wider sizes.
- This applies to both Variant 1 and Variant 2 — update `.container`'s `max-width` (Variant 1) and `--maxw` (Variant 2, Section 13.1) using the same `min(…, …vw)` pattern rather than leaving either as a flat pixel value.

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
8. **🔀 Shuffle rows** (shown alongside Start) randomizes the data-row order via Fisher-Yates so answers can't be memorized by table position — the original row order is captured on first shuffle and restored by Reset (see Section 14.10 for the code)
9. **↺ Reset** restores all cells, restores original row order, and returns the toolbar to its initial state

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
- [ ] Container/grid widths scale to fill a 16" MacBook Pro browser window (~1512–1728px) without large empty side margins (Section 6) — checked by resizing/rendering at those widths, not just at 1280px

---

## 10. Adapting for a New Lecture

1. **Update the hero** — new title, instructor, institution, relevant stats
2. **Add/remove sections** — one `<div class="section">` per LO
3. **Pick the right components** — use drug grids for drug class breakdowns, compare grids for binary contrasts, step lists for processes, hallmark grids for enumerated concepts, p53 grid for function lists
4. **Keep the color system** — don't introduce new colors; map new content onto existing callout types. Use `.box-warning` for regulatory/safety warnings, `.callout-warning` for clinical pitfalls.
5. **Theme system is plug-and-play** — copy the full theme CSS block (all variable groups, including `--panel-dark-bg`/`--panel-dark-text`) and JS verbatim; no edits needed per lecture. Still worth a quick visual spot-check per theme (Section 3).
6. **Change the localStorage key** — update the `STORAGE_THEME_KEY` constant to a unique per-lecture string so different files don't share state
7. **Table Quiz is automatic** — `initTableQuiz()` requires no per-table setup; just include it and call it from `DOMContentLoaded`
7a. **Scale layout width for a 16" MacBook Pro (Section 6)** — use `min(1200px, 94vw)`-style container widths and `auto-fit`/`auto-fill` grids instead of flat pixel `max-width`s, so the page fills a ~1512–1728px browser window instead of sitting as a narrow column with empty space on both sides
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

---

## 13. Variant 2 — "Modality Card" Design System

> Built for `Introduction_to_Therapy_Study_Notes.html` (Lee Wolfrum, DO — Introduction to Therapy). Everything below is a complete, self-contained alternative to Sections 2–12 — use this section on its own, don't mix its components with Variant 1's in the same file.

### 13.0 When to Use This Variant Instead of Variant 1

Reach for Variant 2 when:
- The source lecture doesn't have clean, numbered LOs to organize around — content gets organized by the deck's own topic flow instead (see Section 10's LO-per-section rule, which this variant deliberately drops).
- The content is conceptual/theory-driven (history, modalities, theory comparison) rather than drug- or pathology-enumeration-driven — Variant 1's drug-grid/hallmarks-grid/p53-grid/REMS-badge/potency-bar vocabulary (5.12–5.17) doesn't map cleanly onto it.
- A simpler light/dark toggle is preferable to maintaining five full named-theme palettes.

Both variants are single self-contained `.html` files with base64-embedded images, a click-to-zoom lightbox, an interactive table-quiz feature, and an optional printable High-Yield One-Pager modal — the philosophy is identical, only the visual system and component vocabulary differ.

### 13.1 Fonts & Color System

**Google Fonts:** Crimson Pro (headings — 400/500/600/700, italic), Nunito (body — 400/500/600/700/800), IBM Plex Mono (labels, badges, mnemonics, mono UI).

**CSS Custom Properties** — one light palette plus a single dark override block, not five named themes:

```css
:root{
  --cream:#FBF7EF; --cream-2:#F4EDDC; --card:#FFFFFF;
  --ink:#2B2621; --ink-soft:#5B534A; --border:#E4D8C0;
  --teal:#2F6F6B; --teal-dk:#1F4D4A; --teal-tint:#E6F0EE;
  --gold:#B9862F; --gold-tint:#FBF0DA;
  --rose:#A6524A; --rose-tint:#F7E7E3;
  --plum:#6C5279; --plum-tint:#EFE7F3;
  --shadow:0 4px 16px rgba(43,38,33,0.08);
  --shadow-lg:0 12px 32px rgba(43,38,33,0.14);
  --radius:14px; --font-scale:1; --maxw:920px;
}
[data-theme="dark"]{
  --cream:#1C1815; --cream-2:#221D18; --card:#28221D;
  --ink:#EEE6D6; --ink-soft:#C4B9A4; --border:#3B3226;
  --teal:#5EA39D; --teal-dk:#7FC2BB; --teal-tint:#20302E;
  --gold:#E0AC55; --gold-tint:#332811;
  --rose:#D4897F; --rose-tint:#332019;
  --plum:#B79DC9; --plum-tint:#2A2331;
  --shadow:0 4px 16px rgba(0,0,0,0.35);
  --shadow-lg:0 12px 32px rgba(0,0,0,0.5);
}
```

`--teal` is the primary accent (links, section labels, nav highlight); `--gold` is reserved for high-yield flags and mnemonics; `--rose` and `--plum` are secondary callout/card-border accents. Unlike Variant 1, there is no separate `--panel-dark-*` pair — nothing in this variant renders as an always-dark panel regardless of theme, so that whole class of bug (Section 3's "Known Pitfall") doesn't apply here.

### 13.2 Theme Toggle — Simpler Than Variant 1

One icon button in the topbar flips `data-theme` between `"light"` and `"dark"` on `<html>`. No theme picker panel, no `localStorage` persistence — state resets on reload. (Not persisting theme choice is a deliberate simplification, not an oversight: it also sidesteps needing browser storage inside a portable single-file document at all.)

```html
<button class="icon-btn" id="themeToggle" title="Toggle light/dark">🌓</button>
```
```js
document.getElementById('themeToggle').addEventListener('click', () => {
  const html = document.documentElement;
  html.setAttribute('data-theme', html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
});
```

### 13.3 Overall Page Structure

```
<body>
  .topbar          ← sticky: brand + horizontally-scrolling pill nav + HY button + theme toggle, all one row
  .hero            ← light gradient (not a dark hero like Variant 1) — title/subtitle/meta pills + "yield check" callout
  <main>
    section#id × N   ← one per topic-cluster (not strictly per-LO), each with a "SECTION NN" eyebrow tag + <h2>
  </main>
  #hySummary       ← optional High-Yield modal (13.6), hidden by default
  #lightbox        ← full-screen image overlay (same concept as Variant 1 Section 8)
  #fontctl         ← fixed bottom-right pill, A-/A+ ONLY (theme toggle lives in the topbar here, not in this stack)
  <footer>
  <script>         ← theme toggle, scroll-based active-nav highlight, quiz-table engine, MCQ engine, lightbox, HY modal
```

The topbar nav uses `<a href="#section-id">` pills that gain an `.active` class on scroll (via a `scroll` listener comparing each section's `getBoundingClientRect().top`), rather than Variant 1's plain `.toc-bar` links with no active-state tracking.

### 13.4 Component Reference

#### 13.4.1 Modality Card
The Variant-2 analogue of `.drug-card` — a generic content card for any named concept (a therapy modality, a defense mechanism cluster, a historical figure), not pharmacology-specific.

```html
<div class="modality-card">
  <h4>Dialectical Behavior Therapy (DBT)</h4>
  <div class="tagline">Created by Marsha Linehan, PhD — for borderline personality disorder</div>
  <div class="row"><b>Structure</b>A skills-based, manualized treatment built around <b>4 modules</b>: emotion regulation, mindfulness, distress tolerance, and interpersonal effectiveness.</div>
  <div class="row"><b>Origin</b>Linehan developed DBT partly from her own lived experience with BPD.</div>
</div>
```
```css
.modality-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);
  padding:18px 20px;box-shadow:var(--shadow);margin:16px 0;border-top:5px solid var(--teal);}
.modality-card .row>b:first-child{color:var(--teal-dk);font-size:.82rem;text-transform:uppercase;
  letter-spacing:.03em;font-family:'IBM Plex Mono',monospace;font-weight:600;display:block;margin-bottom:2px;}
```

> **Pitfall — scope the label selector to `:first-child`.** The label styling (`display:block`, small caps, monospace) is meant for only the *first* `<b>` in a `.row` — the one acting as a field label ("Structure", "Origin"). An early version of this rule was written as `.modality-card .row b{display:block;...}`, matching **every** `<b>` in the row. That's harmless until a row's body text itself contains a second bold phrase for ordinary emphasis (e.g. "...built around **4 modules**: emotion regulation...") — the selector forced that inline phrase onto its own block line too, breaking the sentence apart visually. Fixed by changing the selector to `.modality-card .row>b:first-child`, which leaves any *other* `<b>` in the row as normal inline bold text.

#### 13.4.2 Callout Boxes
Five flavors, same base+modifier pattern as Variant 1 Section 5.4, different names/palette:

| Modifier | Color | Use for |
|---|---|---|
| `callout-history` | Plum | Historical context, origin stories |
| `callout-clinical` | Teal | Clinical pearl or practical application |
| `callout-quote` | Cream, italic | A quoted line from the source material |
| `callout-mnemonic` | Gold, dashed border, 🧠 icon | A memory hook / mnemonic |
| `callout-exam` | Rose | Research-methodology or exam-relevant caveat |

```html
<div class="callout callout-mnemonic">
  <div class="ic">🧠</div>
  <div><b>Memory Hook:</b> DBT → BPD. If a question mentions dialectical behavior therapy, think borderline personality disorder first.</div>
</div>
```

#### 13.4.3 Inline High-Yield Flag
A small pill for flagging an exam-critical fact *inline*, mid-sentence or in a heading — lighter-weight than opening a whole callout box for one flagged phrase:

```html
<h3>Skinner's Operant Conditioning Quadrants <span class="hy-flag">⭐ HY</span></h3>
```
```css
.hy-flag{display:inline-flex;align-items:center;gap:3px;background:var(--gold-tint);color:var(--gold);
  border:1px solid var(--gold);font-family:'IBM Plex Mono',monospace;font-weight:700;
  font-size:.68rem;padding:2px 8px;border-radius:20px;letter-spacing:.03em;vertical-align:middle;}
```

#### 13.4.4 Click-to-Reveal Case Box
Native `<details>`/`<summary>` instead of a custom exam-q div (Variant 1 Section 5.10) — good for a framing clinical vignette that expands on click, with zero JS needed for the open/close mechanic itself:

```html
<details class="case">
  <summary>A 54-year-old financial broker, recently fired</summary>
  <div class="case-body">
    <p>Presentation and teaching discussion go here...</p>
  </div>
</details>
```
```css
details.case{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);
  margin:16px 0;box-shadow:var(--shadow);overflow:hidden;}
details.case summary{cursor:pointer;padding:16px 20px;font-weight:700;font-family:'Crimson Pro',serif;
  font-size:1.1rem;color:var(--teal-dk);list-style:none;display:flex;align-items:center;gap:10px;}
details.case summary::-webkit-details-marker{display:none;}
details.case summary::before{content:"▸";transition:transform .2s;color:var(--teal);}
details.case[open] summary::before{transform:rotate(90deg);}
details.case .case-body{padding:0 20px 20px;border-top:1px solid var(--border);}
```

#### 13.4.5 Comp-Table Quiz — Per-Cell Inline Approach (Different Architecture Than Variant 1 Section 7)
Variant 1's table quiz auto-injects a column-picker toolbar above *every* `<table>` with no markup needed. Variant 2 instead marks specific tables opt-in with `class="comp-table"` and specific cells with `class="quiz-cell"` (wrapping the real content in `<span class="qc-inner">`), and puts one toggle button above each such table:

```html
<div class="quiz-toggle-row"><button class="quiz-toggle" data-target="defense-table">Take as quiz</button></div>
<table class="comp-table" id="defense-table">
  <tr><th>Defense</th><th>Definition</th><th>Example</th></tr>
  <tr><td>Denial</td>
    <td class="quiz-cell"><span class="qc-inner">Refusing to accept an unbearable piece of reality</span></td>
    <td class="quiz-cell"><span class="qc-inner">...</span></td>
  </tr>
</table>
```

**Critical default-state rule — quiz mode must be OFF until the user opts in:**
```css
/* Plain, fully-readable table content by default */
.comp-table .quiz-cell .qc-inner{transition:filter .2s, opacity .2s;}
/* Only blur/hide once the table has explicitly entered quiz mode */
.comp-table.quiz-active .quiz-cell{cursor:pointer;position:relative;background:var(--teal-tint)!important;}
.comp-table.quiz-active .quiz-cell:not(.revealed) .qc-inner{filter:blur(5px);opacity:.35;user-select:none;}
.comp-table.quiz-active .quiz-cell:not(.revealed)::after{
  content:"tap to reveal";position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  font-family:'IBM Plex Mono',monospace;font-size:.68rem;color:var(--teal);font-weight:600;
  background:var(--teal-tint);
}
```
```js
document.querySelectorAll('.comp-table .quiz-cell').forEach(cell => {
  cell.addEventListener('click', () => {
    if (cell.closest('.comp-table').classList.contains('quiz-active')) cell.classList.toggle('revealed');
  });
});
document.querySelectorAll('.quiz-toggle').forEach(btn => {
  const defaultLabel = btn.textContent;
  btn.addEventListener('click', () => {
    const table = document.getElementById(btn.dataset.target);
    const turningOn = !table.classList.contains('quiz-active');
    table.classList.toggle('quiz-active', turningOn);
    btn.classList.toggle('is-active', turningOn);
    if (turningOn) { table.querySelectorAll('.quiz-cell').forEach(c => c.classList.remove('revealed'));
      btn.textContent = 'Show answers / exit quiz'; }
    else btn.textContent = defaultLabel;
  });
});
```

> **Pitfall — a table isn't a study reference if it defaults to hidden.** An earlier pass of this component set every `.quiz-cell` to blurred-and-hidden as its *resting* state (no `.quiz-active` gate at all) — meaning the table was unusable as a plain reference until the reader clicked something first, which defeats the point of also using it as a normal-mode note. The fix is the `.quiz-active` gate above: "hidden" is only ever a state the table opts into, never the default.

#### 13.4.6 Multiple-Choice Question Box
```html
<div class="qbox">
  <div class="qnum">Practice Question</div>
  <div class="qtext">Which of the following is <b>NOT</b> an example of classical conditioning?</div>
  <div class="opts">
    <div class="opt" data-correct="false">A. ...</div>
    <div class="opt" data-correct="true">B. ...</div>
  </div>
  <div class="explain">Answer: <b>B</b>. Explanation text.</div>
</div>
```
```js
document.querySelectorAll('.qbox').forEach(box => {
  const opts = box.querySelectorAll('.opt'); const explain = box.querySelector('.explain');
  opts.forEach(opt => opt.addEventListener('click', () => {
    if (box.dataset.answered) return; box.dataset.answered = "1";
    opts.forEach(o => { if (o.dataset.correct === "true") o.classList.add('correct');
      else if (o === opt) o.classList.add('incorrect'); });
    explain.classList.add('show');
  }));
});
```

#### 13.4.7 Rapid Review Grid
A closing 2-column grid of short recap cards — the high-yield "last thing before the gallery" section:
```html
<div class="rr-grid">
  <div class="rr-item"><b>Classical conditioning</b><br>Innate response + neutral stimulus → response transfers.</div>
</div>
```

#### 13.4.8 Timeline
Left-border timeline with dot markers, for chronological content (history of a field, a research timeline):
```html
<div class="timeline">
  <div class="tl-item"><div class="tl-year">1977</div><div>A landmark meta-analysis found an effect size of 0.8...</div></div>
</div>
```
```css
.timeline{border-left:3px solid var(--border);margin:20px 0 20px 8px;padding-left:22px;}
.tl-item{position:relative;margin-bottom:22px;}
.tl-item::before{content:"";position:absolute;left:-29px;top:3px;width:12px;height:12px;
  border-radius:50%;background:var(--teal);border:2px solid var(--cream);}
```

#### 13.4.9 Gallery + Lightbox
Same concept as Variant 1 Section 8 (click any `img.zoomable` to open a full-screen overlay with caption), reused here for a closing figure-gallery grid. Supports arrow-key navigation between all zoomable images on the page, not just the one clicked.

#### 13.4.10 Font-Size Control
Same A-/A+ idea as Variant 1 Section 5.17, but scales via a CSS custom property multiplying the base font-size, so every `rem`-based size on the page scales together — not just the body's own pixel size:
```css
body{font-size:calc(16px * var(--font-scale));}
```
```js
let fontScale = 1;
document.getElementById('fontPlus').addEventListener('click', () => {
  fontScale = Math.min(1.35, fontScale + 0.08);
  document.documentElement.style.setProperty('--font-scale', fontScale);
});
```

### 13.5 High-Yield One-Pager — Topic-Cluster Grid, Not LO Columns

Variant 2's HY modal (`#hySummary`) uses a 2-column CSS Grid of small `.hy-card` blocks, one per **topic-cluster** (Conditioning, Skinner's Quadrants, Ego Defenses, Modality Quick-Map, ...) rather than Variant 1's 3-column-per-LO layout (12.2) — the right choice when the lecture's content isn't cleanly split into exactly 2–3 LOs to begin with. A `.hy-full` card (`grid-column:1/-1` on screen) holds the one dense appendix-style block — here, all 20 ego defenses as an internal 3-column bullet list — playing the same structural role as Variant 1's full-width master drug-reference table (12.2).

The button lives in the **topbar**, not the hero, styled as a filled gold pill:
```html
<button class="hy-btn" id="hyOpenBtn" title="One-page high-yield summary">⭐ HIGH YIELD</button>
```

#### 13.5.1 Print CSS — a Masonry Technique for Uneven Card Heights

Variant 1's print CSS (12.5) uses a plain `grid-template-columns: repeat(3, 1fr)`, which works well when the content really is 3 roughly-even LO columns. Variant 2's cards are *uneven* heights (a short "Practice Question Recap" card next to a long "Ego Defenses" card) — reusing a strict grid for print produced a real, verified bug: **the one-pager printed to 2 pages with a large empty gap on both**, because CSS Grid sizes every row by its tallest cell, wasting the shorter cells' unused space instead of letting later content flow up into it.

**Fix — switch the print layout from `grid` to CSS multi-column (`column-count`), and pull the one full-width card out of the column flow with `column-span: all`:**
```css
@media print{
  .hy-grid{display:block !important;column-count:3 !important;column-gap:9px !important;}
  .hy-card{display:block !important;width:100% !important;margin:0 0 7px !important;break-inside:avoid;}
  .hy-full{column-span:all !important;}
  @page{size:landscape;margin:6mm;}
}
```
This lets the small cards flow masonry-style — filling gaps top-to-bottom, column by column — instead of being locked into a rigid row grid, while the full-width card still breaks cleanly across all columns wherever it falls in the source order. **Verified by actually exporting to PDF and checking the page count dropped from 2 → 1**, not by re-reading the CSS — the same "don't just eyeball it" lesson as Variant 1's 12.6, applied to a different underlying bug.

### 13.6 Known Pitfalls Found This Build (mirrors Variant 1 Section 3's pitfall callouts)

1. **Nested `<b>` inside a component styled by a descendant selector** — see 13.4.1. Scope label-style selectors to `:first-child` whenever a component's body text might legitimately contain its own inline bold phrase.

2. **`overflow-wrap: anywhere` looks like a safe global default but silently shrinks table columns.** An earlier pass added `overflow-wrap:anywhere` to `body` (to stop one long slash-joined word from overflowing a card). The visible symptom was ordinary short words like "Dissociation" or "Displacement" fracturing mid-letter (`Dissociatio` / `n`) inside a table column that had plenty of free space beside it — because `anywhere` lets Chrome's table auto-layout compute a much smaller min-content width for that column than `break-word` would, even on wide desktop viewports where there was no actual overflow risk. **Fix:** use `overflow-wrap: break-word` as the site-wide default (still prevents genuine overflow from a long unbreakable token) and only reach for `anywhere` on one specific narrow element if `break-word` truly isn't enough there.

3. **CSS Grid track width can be forced wider than its container by a wide child's min-content — even inside a single explicit `1fr` column on mobile.** A `<table>` inside a grid item doesn't shrink to fit by default: a grid item's `min-width` is `auto`, which factors in the min-content size of its content, so a wide table can force the whole grid track — and the modal card holding it — to overflow the viewport. This shipped as a real, screenshotted-but-still-missed bug: a mobile screenshot of the HY modal *looked* fine at a glance, but the card was actually 418px wide inside a 358px-wide parent, bleeding off the right edge. **Fix:** `min-width: 0` on both the grid container and the grid items (`.hy-grid`, `.hy-card`) forces them to respect the explicit `1fr` track instead of expanding to fit their widest child. Confirmed via `getBoundingClientRect()` comparison (card width dropped from 418px to 298px, now inside its 358px parent), not just a second screenshot.

4. **Quiz tables must default to fully visible, not default to quizzed/hidden** — see 13.4.5. If a `.quiz-cell`'s hidden/blurred state isn't gated behind an explicit `.quiz-active` opt-in class on its parent table, the table is unusable as a plain reference on first load.

### 13.7 Verifying Interactive Features (same spirit as Variant 1's 12.6, applied to the whole file)

Don't just read the CSS/JS back and reason about it — actually drive the page with a headless browser and assert on the result:
- Click every `.quiz-toggle` and check `classList.contains('quiz-active')` flips both ways, and that a `.quiz-cell`'s *computed* `filter`/`opacity` (not just its class list) is actually `none`/`1` by default.
- Click every `.qbox` option and confirm the `.correct` / `.incorrect` / `.explain.show` classes land on the right elements.
- Open the lightbox, step through `ArrowRight`/`ArrowLeft`, close with `Escape`, and confirm `document.documentElement.scrollWidth` never exceeds the viewport width — check this at **320px, 390px, 768px, and desktop**, not just desktop.
- For any fixed-position modal (the HY summary, the lightbox): pull `getBoundingClientRect()` for the modal card and a representative child, and confirm the child's `right` edge is within the parent's — a visually-plausible screenshot can still be hiding an overflow that a fixed-position ancestor is silently letting bleed past the viewport edge (pitfall 3 above looked fine in a screenshot at first glance; only bounding-box numbers caught it).
- Export the HY one-pager to PDF and check the actual page count, same as Variant 1's 12.6 — re-check after *every* print-CSS edit, don't assume one tweak fixed it without re-exporting.

---

## 14. Study Tools System (Optional Active-Recall / Progress Layer)

> First built for `Eating_Disorders_Study_Notes.html` (Lee Wolfrum, DO — Eating Disorders), layered on top of Variant 1. This is an **add-on layer**, not a third variant: it assumes the base file already exists (sections with stable `id`s, a sticky TOC bar, `.exam-q` blocks, the table quiz) and injects everything else at runtime via JS — no manual per-section HTML edits needed beyond the TOC. It can be applied to either variant.

The design intent: convert a passive reading document into a retrieval-practice tool. Every feature below maps to a specific study behavior — Recall Mode = active recall, reviewed/confidence tracking = a self-sorting review queue for the second pass, collapse = header-prompted recall, the compare strip = anchoring the discrimination task, Next-Q = a pure question-pass the night before the exam.

### 14.0 Prerequisites & Conventions

- Every `.section` needs a stable `id`, listed in one JS constant: `const SECTION_IDS = ['overview','anorexia', ...];` — everything else keys off this array.
- All persistent state goes to `localStorage` under **file-unique keys** (same rule as the theme key in 5.19): e.g. `'eating-disorders-progress'`, `'eating-disorders-compare-strip'`.
- All new floating UI must be added to the print-hide rule:
```css
@media print{
  .floating-left, .progress-bar, .compare-strip, .sec-tools, .recall-note{display:none !important;}
  .section.collapsed .sec-body-outer{grid-template-rows:1fr !important;} /* print expanded even if collapsed on screen */
}
```
- Wrap ALL animations behind reduced-motion:
```css
@media (prefers-reduced-motion: reduce){
  *, *::before, *::after{animation:none !important; transition:none !important;}
  html{scroll-behavior:auto;}
}
```
- **Animation philosophy:** strictly functional only — answer fade-in on reveal, a brief flash on a just-revealed recall fact, smooth collapse, a pulse on the jumped-to question. No scroll-triggered entrance effects: they slow scanning without aiding encoding.

### 14.1 Reading Progress Bar

3px fixed gradient bar at the very top of the viewport; width = scroll percentage.

```css
.progress-bar{position:fixed; top:0; left:0; height:3px; width:0%; z-index:200;
  background:linear-gradient(90deg, var(--accent2), var(--accent)); transition:width .1s linear;}
```
```js
window.addEventListener('scroll', function(){
  const h = document.documentElement;
  const max = h.scrollHeight - h.clientHeight;
  bar.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
  backtop.classList.toggle('show', h.scrollTop > 600);
}, {passive:true});
```

### 14.2 TOC Scrollspy + Progress Chip + Collapse-All

The sticky TOC (5.2) gains three things: an active-section underline, a per-section ✓ colored by confidence, and a right-aligned tools cluster.

**HTML — each TOC link gets a hidden check, and a `.toc-tools` span goes at the end of the nav:**
```html
<a href="#anorexia">Anorexia Nervosa<span class="toc-check">✓</span></a>
...
<span class="toc-tools">
  <button class="toc-chip" id="progressChip" onclick="jumpToNextTodo()">0/6 reviewed</button>
  <button class="toc-chip" id="collapseAllBtn" onclick="toggleAllSections()">⊟ Collapse all</button>
</span>
```

**CSS (key parts):** active link underline animates via a `::after` pseudo-element (`width:0% → 100%`); `.toc-check` is `display:none` until the link has `.done`; `conf-1/2/3` classes color the check red/yellow/green. `.toc-tools{margin-left:auto;}` inside the flex nav pushes it right.

**Scrollspy JS — IntersectionObserver with an offset band so the "active" section is the one near the top of the viewport, not whatever touches the edge:**
```js
function initScrollspy(){
  if (typeof IntersectionObserver === 'undefined') return; // test-env guard
  const obs = new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if (en.isIntersecting) { /* clear all .active, set on links[en.target.id] */ }
    });
  }, {rootMargin:'-20% 0px -70% 0px'});
  SECTION_IDS.forEach(id => { const s = document.getElementById(id); if (s) obs.observe(s); });
}
```
Also add `.section{scroll-margin-top:58px;}` so anchor jumps don't hide the section title under the sticky bar.

**The progress chip doubles as a review queue.** `jumpToNextTodo()` picks, in priority order: first unreviewed section → first 🔴 shaky → first 🟡 okay, expands it if collapsed, and scrolls to it. On a second study pass, clicking the chip repeatedly walks exactly the sections that need work.

### 14.3 Per-Section Progress: Reviewed ✓ + Confidence 🔴🟡🟢

A `.sec-tools` row is **injected by JS** directly after each `.section-title` — never hand-written into the HTML (keeps the base document clean and the feature portable):

```
[✓ Reviewed]  Confidence [🔴 Shaky] [🟡 Okay] [🟢 Solid]              [▾ Collapse]
```

State shape in localStorage: `{"anorexia":{"reviewed":true,"conf":1}, ...}`. Clicking a confidence button a second time clears it (toggle-off). One `renderProgress()` function is the single source of truth — it repaints the section buttons, the TOC checks/colors, and the chip count from the stored object; every mutation just writes state and calls it.

### 14.4 Collapsible Sections (animated, no fixed heights)

Section bodies are wrapped at runtime in a two-layer grid for smooth height animation without measuring content:

```js
const outer = document.createElement('div'); outer.className = 'sec-body-outer';
const inner = document.createElement('div'); inner.className = 'sec-body-inner';
outer.appendChild(inner);
while (note.nextSibling) inner.appendChild(note.nextSibling); // move everything after the tools row
container.appendChild(outer);
```
```css
.sec-body-outer{display:grid; grid-template-rows:1fr; transition:grid-template-rows .35s ease;}
.sec-body-inner{overflow:hidden; min-height:0;}
.section.collapsed .sec-body-outer{grid-template-rows:0fr;}
```

The `1fr → 0fr` grid-row trick animates to/from auto height with zero JS measurement. The per-section button and the TOC's Collapse-all both call the same `toggleSection(sec, force)`. **Study use:** collapse all, then expand only sections you can't reconstruct from the header — the collapsed state is itself a recall prompt.

### 14.5 Recall Mode (global blur-to-reveal)

The core active-recall feature. A body class hides every `<strong>` inside section bodies behind a highlight block; each is individually click-to-reveal with a running `revealed/total` counter on the toggle button.

```css
body.recall-mode .sec-body-inner :is(p,li,td,h4) strong:not(.rc-open){
  color:transparent; background:var(--highlight2); border-radius:4px; cursor:pointer;
  box-shadow:inset 0 0 0 1px var(--border); padding:0 2px;}
body.recall-mode .exam-q strong{color:var(--gold) !important; background:none !important; box-shadow:none !important;}
strong.rc-open{animation:rcReveal .35s ease;}
```

Rules learned building it:
- **Exclude `.exam-q` and `.tq-bar` content** from blurring — questions must stay readable, and the exam-q's own click-to-reveal must not fight with recall reveals.
- The reveal click handler runs on the **capture phase** with `stopPropagation()`, so revealing a `<strong>` inside a clickable parent doesn't also trigger the parent.
- Reveals are one-way per session (click reveals; toggling Recall Mode off resets all `rc-open`).
- Turning Recall Mode ON while everything is collapsed auto-expands (`if (recallMode && allCollapsed) toggleAllSections();`) — blurred content inside collapsed sections is a dead end.
- A dashed hint banner (`.recall-note`, injected per section, `display:none` unless `body.recall-mode`) tells the reader how the mode works.
- This feature is why disciplined `<strong>` usage matters when writing content (only bold genuinely testable facts): the bolding IS the recall deck.

### 14.6 Next-Question Jumper

A button (and the `Q` shortcut) that scrolls to the next **unanswered** `.exam-q` below the current viewport position (wrapping to the first unanswered, then to the first overall), expands its section if collapsed, centers it, and pulses it:

```css
.exam-q.q-flash{outline:3px solid var(--gold); animation:qPulse 1.2s ease 1;}
@keyframes qPulse{0%{box-shadow:0 0 0 0 rgba(201,146,42,.55);} 70%{box-shadow:0 0 0 14px rgba(201,146,42,0);} 100%{box-shadow:none;}}
```

The button shows a live `answered/total` count. Restart the flash animation reliably with the reflow trick: `el.classList.remove('q-flash'); void el.offsetWidth; el.classList.add('q-flash');`. Count updates hook off delegated clicks on `.exam-q` (with a `setTimeout(0)` so the reveal class lands first).

### 14.7 Pinned Compare Strip

A fixed, dismissable panel (bottom-left, above the tools menu) holding the single hardest discrimination task in the lecture as a dense `.cs-table` — for Eating Disorders: AN vs BN vs BED across BMI, driving factor, F:M/onset, first-line tx, med contraindications. It stays open while scrolling any section; open/closed state persists in localStorage and is restored on load.

**Content rule:** the strip is not a mini-TOC — it's the one comparison the exam will test. Pick the discrimination axis the lecturer emphasized, keep it to ~5 rows, and reuse the `hy-mini-table` sizing idiom (tiny font, tight padding). Width: `min(560px, calc(100vw - 40px))`.

### 14.8 Floating Study-Tools Menu (bottom-LEFT, hover-expand)

All study-tool buttons live in a single collapsed trigger to save screen real estate — only one **🧰 Study** pill is visible at rest; hovering (desktop) or tapping (touch) expands the stack upward:

```html
<div class="floating-left" id="floatingLeft">
  <div class="tools-menu">
    <button class="tool-btn backtop" id="backtopBtn" ...>↑ Top</button>
    <button class="tool-btn" id="compareBtn" ...>⚖ Compare</button>
    <button class="tool-btn" id="nextQBtn" ...>❓ Next Q <span id="qCount"></span></button>
    <button class="tool-btn" id="recallBtn" ...>🙈 Recall Mode <span id="rcCount"></span></button>
  </div>
  <button class="tool-btn tools-trigger" id="toolsTrigger" onclick="toggleToolsMenu()">🧰 Study<span class="dot"></span></button>
</div>
```
```css
.tools-menu{opacity:0; pointer-events:none; transform:translateY(10px); transition:opacity .22s, transform .22s;}
.floating-left:hover .tools-menu, .floating-left:focus-within .tools-menu,
.floating-left.open .tools-menu{opacity:1; pointer-events:auto; transform:translateY(0);}
```

- `:hover` covers mouse users, `:focus-within` covers keyboard users, and a `.open` class toggled by tapping the trigger covers touch (with a document-level click handler closing it on outside tap).
- A small gold **activity dot** on the trigger (`.tools-trigger.busy .dot`) shows whenever Recall Mode or the compare strip is active, so a "mode is on" signal survives the menu collapsing. One `syncToolsDot()` is called from both toggles.
- Buttons that carry live counters (`Next Q 2/6`, `Recall 12/49`) keep them inside the menu — the counters are only relevant while interacting with the tools.
- The back-to-top button additionally requires `.show` (scrollY > 600) AND the menu being open/hovered.
- Bottom-left deliberately mirrors 5.19's bottom-right stack (font/theme) — display controls right, study controls left.

### 14.9 Keyboard Shortcuts

| Key | Action |
|---|---|
| `j` / `k` | Next / previous section (smooth scroll) |
| `Q` | Jump to next unanswered exam question |
| `R` | Reveal the answer of the exam-q nearest the viewport center |

Guards: ignore when a modifier key is held, when focus is in an input/textarea/select, and when the HY modal is open. Current-section detection for j/k uses `window.scrollY + window.innerHeight * 0.3` against each section's `offsetTop` — no observer needed. List the shortcuts in the footer so they're discoverable.

### 14.10 Quiz Row Shuffle (extends Section 7)

A `🔀 Shuffle rows` button in the `.tq-bar` (shown whenever the column picker is open) that Fisher-Yates-shuffles the data rows in the DOM, so answers can't be memorized positionally:

```js
let originalRowOrder = null;
shuffleBtn.addEventListener('click', function(){
  const parent = table.querySelector('tbody') || table;
  const rows = Array.from(parent.querySelectorAll('tr')).filter(r => !r.querySelector('th'));
  if (!originalRowOrder) originalRowOrder = rows.slice();   // capture once, before first shuffle
  const shuffled = rows.slice();
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  shuffled.forEach(r => parent.appendChild(r));            // re-appending moves, doesn't clone
});
```
Reset re-appends `originalRowOrder` to restore the document order. Filter on "row contains a `<th>`" rather than row index so header rows survive whether or not the table has a `<tbody>`.

### 14.11 Storage Keys Used by This Layer

| Key | Shape | Written by |
|---|---|---|
| `<file>-progress` | `{sectionId: {reviewed:bool, conf:0-3}}` | Reviewed / confidence buttons |
| `<file>-compare-strip` | `'1'` / `'0'` | Compare strip toggle |
| `<file>-theme`, `<file>-font-scale` | (pre-existing, Section 5.19) | Theme / font controls |

Recall-mode reveals, quiz state, and collapse state are deliberately **not** persisted — they're per-session study activities, and restoring them stale would be confusing.

### 14.12 Verifying This Layer (same "don't just eyeball it" rule as 12.6 / 13.7)

Drive the file headlessly (jsdom or Playwright) and assert, at minimum:
- `.sec-tools` and `.sec-body-inner` counts equal `SECTION_IDS.length` after load (the runtime injection/wrapping worked on every section).
- Clicking Reviewed / a confidence button updates the section button state, the TOC link's classes (`done`, `conf-N`), the chip text, AND the localStorage JSON — all four, from one click.
- Recall Mode: target count > 0; clicking a blurred `<strong>` increments the counter and adds `rc-open`; toggling the mode off clears every `rc-open`; strongs inside `.exam-q` are NOT in the target list.
- Revealing an `.exam-q` updates the Next-Q counter; `jumpToNextQ()` on a collapsed section expands it.
- Quiz shuffle changes row order and Reset restores the original first data row.
- jsdom gotchas: pass a real `url:` option (opaque origins throw on `localStorage`) and guard `IntersectionObserver` (`typeof … === 'undefined'`) — the guard is also cheap insurance in exotic browsers.
