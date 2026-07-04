# Case Note Build Spec — "Highlight → Explain" Interactive HTML Notes

**What this is:** the reusable spec for the single-file HTML case-note format built for Case 2-1 (CMT1A, Block 5 Medical Neuroanatomy, Dr. Willard's small group). Upload this file alongside a case document (and a small-group transcript, if you have one) and this is the whole build plan — no re-deriving design decisions from scratch.

---

## 1. What to build

A single self-contained `.html` file with three stacked parts:

1. **The case, word-for-word.** The full case document text, reproduced exactly (not summarized/paraphrased), split into its own natural sections (Chief Complaint, HPI/HCC, Family Hx, Medical Hx, ROS, PE, Neuro exam, Follow-up, etc. — whatever sections the source document actually uses).
2. **Annotations woven into the highlights.** Key phrases in the case get a colored highlight. Interacting with a highlight explains it — see §4 for the interaction model.
3. **Below the case:** a condensed **Clinical Reasoning Walkthrough** (localization → distribution → time course → differential → workup → prognosis → management) and a set of **Concept Deep-Dive** cards (custom diagrams for the underlying neuroanatomy/pathophys the case is testing).

---

## 2. Inputs I need from you

- **Required:** the case document (verbatim text — chief complaint, HPI, exam findings, etc.)
- **Optional, use if present:**
  - The small-group transcript (or partial transcript) — mine this for the actual reasoning your group walked through; it's the best source for *why* something matters, in your professor's own framing, not a generic textbook explanation.
  - A differential/reasoning breakdown doc (e.g. an OpenEvidence export, or similar) — use this to build the Clinical Reasoning Walkthrough section.
  - Lecture slide PDFs — if provided, extract real slide images (pdftoppm → crop → base64) for the Concept Deep-Dive section instead of building custom SVGs.
- If images/PDF are **not** provided, default to hand-built SVG/CSS diagrams for the deep-dive section (see §6) rather than pulling images from the web — keeps it copyright-clean and visually consistent.

---

## 3. Design system (tokens — reuse exactly)

**Fonts** (Google Fonts CDN, works fine once the file is opened locally — no need to self-host):
- Display / case text: `Crimson Pro` (serif) — weights 400,500,600,700, italic 400,500
- UI / labels / body chrome: `Nunito` (sans) — weights 400,600,700,800
- Mono / eyebrows / data: `IBM Plex Mono` — weights 400,500,600

```html
<link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Nunito:wght@400;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

**Color tokens:**
```css
:root{
  --cream:#F6F1E6;      /* page background */
  --paper:#FCFAF3;      /* card/panel background */
  --ink:#2A241C;        /* primary text */
  --ink-soft:#6B6152;   /* body/secondary text */
  --ink-faint:#9A8F7B;  /* eyebrows, meta labels */
  --line:#DED2B6;       /* borders */
  --line-soft:#EAE0C9;  /* faint dividers */

  --coral:#C85A3E;   --coral-bg:#F7E4DB;   /* category: exam finding */
  --teal:#256B63;    --teal-bg:#DFEDE8;    /* category: localization */
  --gold:#A47A1F;    --gold-bg:#F3E7C6;    /* category: terminology */
  --violet:#6B5390;  --violet-bg:#E9E2F1;  /* category: pattern recognition */
  --sky:#2F6485;     --sky-bg:#DEE9EF;     /* category: genetics/workup/trajectory */

  --radius:10px;
  --shadow:0 1px 2px rgba(42,36,28,.06), 0 8px 24px -12px rgba(42,36,28,.18);
}
```

Five annotation categories, always this set (relabel per case if a category genuinely doesn't apply, but keep the five-way split — it's what lets a reader pattern-match at a glance):

| Category | Color | Use for |
|---|---|---|
| `localization` | teal | Where the lesion/process is; UMN vs LMN reasoning; anatomic pathway logic |
| `finding` | coral | What an exam/history finding means clinically |
| `term` | gold | Definitions of clinical vocabulary (e.g. "insidious," "hyporeflexia") |
| `pattern` | violet | Pattern-recognition / differential-defining clues |
| `genetics` | sky | Inheritance, genetics, workup, trajectory/prognosis facts |

---

## 4. Annotation interaction model (important — read before building)

**Use this exact model. Do not build a persistent right-rail with SVG connector lines to every annotation simultaneously — that was tried and it breaks.** With ~20 annotations, sections with several clustered close together (e.g. a dense HPI paragraph) force a "don't-overlap" stacking algorithm to push later cards far down the page, so their connector lines end up traveling long diagonal distances and crossing through unrelated text and each other. It looks broken because it *is* broken past a certain annotation density, and case notes always have that density. Don't re-derive this — go straight to the model below.

**The model that works, and holds up on desktop, iPad, and phone:**

- **Hover a highlight** (any device with a real pointer — mouse, trackpad, Apple Pencil-equipped iPad): a small tooltip pops up immediately next to that highlight (title + short teaser). No line, because it isn't traveling anywhere — it's already adjacent.
- **Tap/click a highlight** (works on every device, including touch-only): opens the full annotation in a **docked panel** — fixed to the right edge of the viewport on wider screens (≥1000px), a bottom sheet on narrower ones. No page scroll, ever.
- Detect hover capability with `matchMedia("(hover: hover) and (pointer: fine)")` and only attach hover listeners when it's true, so touch devices skip straight to tap → panel (no dead first-tap, no stuck tooltips).
- Case column is a single centered reading column (`max-width: ~800px`) — no grid, no permanent second column. Simpler and it can't break under content density.

**Implementation shape:**
- Each highlighted phrase is a `<mark class="hl" data-cat="…" id="hlN">` wrapping the *exact, unmodified* case text (never alter wording to fit a highlight — only wrap it).
- One JS array of annotation objects: `{target:"hlN", cat, eyebrow, title, body}`, keyed by mark id.
- One small hover-tooltip element (`position:fixed`, positioned relative to the hovered mark's `getBoundingClientRect()`, flips above if it would overflow the bottom of the viewport).
- One docked spotlight panel (`position:fixed`, right-docked ≥1000px / bottom sheet <1000px), populated on click, closable via ×, `Escape`, or click-outside.
- Small superscript number badge after each highlight (numbered in reading/DOM order) — cosmetic continuity with the eyebrow number in the panel, not load-bearing.

---

## 5. Clinical Reasoning Walkthrough (section, below the case)

Condense — don't paste verbatim — into this fixed shape, sourced from the transcript + any reasoning-breakdown doc provided:

1. **Localization** — segmental vs suprasegmental / where in the nervous system, one paragraph.
2. **Distribution** — focal / multifocal / diffuse, length-dependent or not.
3. **Time course** — acute / subacute / chronic-progressive, with the specific evidence for it.
4. **Differential diagnosis** — table: Diagnosis | Fits | Argues against. Lead diagnosis gets a highlighted row + "most likely" tag.
5. **Diagnostic workup** — numbered flow (1→2→3…), each step bolded lead-in + a lighter sub-line with the specific test values/branch logic.
6. **Prognosis** — condensed paragraph.
7. **Management** — bullet checklist, ordered roughly by what a boards question would ask first (orthotics/PT-type supportive care before pharmacologic/surgical).

Layout: CSS grid of cards, 3-wide desktop / 2-wide tablet / 1-wide mobile, differential + workup cards spanning full width (they're tables/flows, need the room).

---

## 6. Concept Deep-Dive cards (section, below reasoning)

5–6 cards, one concept each, pulled from whatever the transcript spent real time on (not just anything textbook-adjacent — if the small group didn't discuss it, it's lower priority than something they did). Each card: category tag, title, a visual (inline SVG built from scratch, or a table styled to match tokens), then a 2–3 sentence takeaway tying it back to *this specific patient's* findings.

If lecture slide images exist, prefer real extracted images over hand-drawn SVG for anything that's genuinely a photographed/illustrated structure (histology, imaging, gross anatomy). Hand-drawn SVG is for schematic/conceptual diagrams (pathways, comparison tables, spectrums) — that's what it's good at, and it's copyright-clean.

---

## 7. Technical notes

- Single HTML file, inline `<style>` and `<script>`, no external JS deps.
- Validate the script block with `node --check` before delivering (extract the `<script>…</script>` contents to a temp `.js` file and check it).
- Sanity-check tag balance (div/section/table/etc. open vs. close counts) before delivering — cheap insurance against a broken layout from a missed closing tag.
- Responsive breakpoint at `1000px` (this is also the hover/panel-position breakpoint — keep them the same value).
- No `localStorage`/`sessionStorage` — not needed here (nothing persists between visits for a single case note), and it wouldn't work in the claude.ai artifact sandbox anyway if this ever gets previewed there.
- Output as a real file to `/mnt/user-data/outputs/`, present it — don't just paste HTML into the chat.

---

## 8. File naming

`case_[X-X]_[working-dx-or-topic]_annotated.html` — e.g. `case_2-1_CMT1A_annotated.html`. Keep cases from the same small-group session visually/structurally identical (same tokens, same section shape) so flipping between them feels like the same tool, not a new build each time.

---

## 9. My build workflow, step by step

1. Read the case document; identify its natural section breaks — preserve them exactly, don't invent new ones.
2. Read the transcript (if provided); pull out the actual reasoning moments — the "why does X matter" explanations your small group discussed — these become the annotation content, in preference to generic textbook explanations.
3. Pick ~15–25 phrases in the case worth annotating: favor findings that (a) change the differential, (b) a professor would ask about directly, or (c) came up explicitly in discussion. Tag each with one of the five categories.
4. Write annotation bodies short (2–3 sentences), concrete, tied to *this patient's numbers/findings*, not generic definitions where a specific one is possible.
5. Build the Clinical Reasoning Walkthrough from the reasoning-breakdown doc (if provided) or synthesized from the transcript + case findings if not.
6. Build 5–6 Concept Deep-Dive cards from whatever the transcript emphasized.
7. Assemble the HTML using the tokens/interaction model above — no rail-with-lines, ever.
8. Validate JS syntax + tag balance.
9. Save to `/mnt/user-data/outputs/`, present the file.
