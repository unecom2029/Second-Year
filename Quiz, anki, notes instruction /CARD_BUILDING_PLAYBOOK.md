# Playbook: Building AnKing-Style `.apkg` Decks from `week1_DIs.html`

**Purpose of this doc:** so a future Claude session (or Jeevs himself) can pick this
project back up — for a new week's Disease Index HTML file, or to extend/fix this
one — without re-deriving the workflow from scratch. Read this whole thing before
touching the source file.

---

## 1. What this project actually is

Jeevs (OMS-1, UNE COM) builds one big self-contained HTML "Disease Index" (DI) file
per week — a sidebar of categories, each containing a category-level "Overview"
panel plus one panel per condition (Natural History, Etiology, Pathophysiology,
Clinical Presentation, sometimes Diagnostic Workup/Treatment/Monitoring, images
embedded as base64, a quiz section, sources).

The task: convert each condition's panel into a **real Anki `.apkg` deck**
(genanki-built, not just an HTML flashcard mockup) — AnKing-style front/back cards,
images pulled out of the base64 and attached to the relevant card, tagged and
nested into a deck hierarchy that mirrors the DI's own category structure.

This is **not** a one-shot script. It's panel-by-panel, category-by-category,
because judgment is needed at every step (how to group facts into cards, which
image belongs on which card, how much a given DI actually contains).

---

## 2. Source file structure — how to navigate it

The DI is one giant HTML file (`week1_DIs.html` was ~4,350 lines / ~10MB, almost
entirely due to embedded base64 images). Do **not** `cat` or `view` the whole
thing — the base64 blobs will blow out the context window instantly.

### 2.1 Find panel boundaries first, always via `grep -n`

Every condition panel starts with an HTML comment and a `<div id="panel-XXX">`:

```bash
grep -n '<!-- DUCHENNE\|panel-duchenne\|<!-- BECKER\|panel-becker' week1_DIs.html
```

The sidebar itself (near the top of the file) lists every category and every
condition inside it, each with a `data-panel="xxx"` id and an `lo-badge` showing
its LO (learning objective) scope, e.g.:

```html
<button class="sidebar-link" data-panel="duchenne" onclick="showPanel('duchenne')">
  <span>Duchenne MD</span><span class="lo-badge">1–5</span>
</button>
```

**Always read the sidebar block for the whole file first** (`sed -n` a
few hundred lines around the `<aside>`). It tells you:
- every category and how many conditions it has (`cat-count`)
- whether a category has its own `📖 Overview` panel (`data-panel="xxx-overview"`)
  — **check this explicitly for every category**, don't assume. In this file,
  Muscular Dystrophies and Metabolic Myopathies each had one; Inflammatory
  Myopathies had one; NMJ Disorders and Neoplastic Disorders did **not**.
  I missed the first two overviews initially and had to circle back — don't
  repeat that. Grep for `panel-<catid>-overview` before declaring a category done.
- the LO-badge range per condition, which predicts how much content (and
  therefore how many cards) that condition will have — see §4.2.

### 2.2 Extract one panel at a time, with images truncated for readability

Once you have the start/end line numbers for a panel:

```bash
awk 'NR>=1885 && NR<=2018 && /data:image/{print NR": "length($0)" chars"}' week1_DIs.html
sed -n '1885,2018p' week1_DIs.html \
  | sed -E 's/(src="data:image\/[a-z]+;base64,)[^"]*"/\1[TRUNCATED]"/g' \
  > ibm_panel_clean.html
```

The `awk` line tells you exactly which line numbers contain base64 images (by
their absurd character length — normal HTML lines are <500 chars, image lines
are 30,000–600,000+ chars) so you know which lines to target for extraction in
the next step. Then `view` the `_clean.html` file normally — it's now safe to
read, with images replaced by a placeholder.

### 2.3 Extract the actual images

For each image line number you noted, decode it out to a real file:

```python
import re, base64

lines_needed = {
    1968: "ibm_gomori_vacuole",
    1972: "ibm_he_vacuole",
}

with open('week1_DIs.html', 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f, start=1):
        if i in lines_needed:
            name = lines_needed[i]
            m = re.search(r'data:image/(\w+);base64,([A-Za-z0-9+/=]+)"', line)
            ext, data = m.group(1), m.group(2)
            with open(f'/home/claude/infl_images/{name}.{ext}', 'wb') as out:
                out.write(base64.b64decode(data))
```

Name files descriptively (`gowers_photo.png`, `dapc_diagram.png`,
`biopsy_vacuoles.png`) — the name becomes the `<img src="...">` filename inside
the card, and a good name is self-documenting when you re-read the build script
later.

**Always `view` every extracted image** before using it — confirms the decode
worked (no corruption) and lets you sanity-check content (e.g. is it the
diagram you expected, is a clinical photo tightly cropped/de-identified the way
the source already intended). These DIs source their clinical photos from
published course material (Osmosis, AMBOSS, AnKing illustrations, case report
figures) that's already been vetted for teaching use — tightly-cropped
dermatology/exam photos (eyelid, knuckles, periorbital region) are treated as
appropriate, consistent with how the source document itself already used them
(e.g. the Gowers maneuver photo already had eyes blacked out in the original).
Don't re-litigate that per image; just confirm the decode succeeded and the
image matches its alt text/caption.

---

## 3. Deck/model architecture (genanki)

### 3.1 The note model — USE THIS EXACT VERSION

Early decks (Duchenne, Becker, Myotonic, LGMD — see §6 "known issues") used a
template that referenced `{{Front tag}}` as if it were a field. **It isn't** —
there's no field by that name, and Anki correctly complained the front was
empty for those note types. Jeevs fixed it manually in Anki by changing the
card/note type, but the underlying `.apkg` files still reflect the broken
template.

**The corrected model (used from the Metabolic Myopathies batch onward) is the
one to keep using:**

```python
import genanki
import random

def sid(name):
    random.seed(name)
    return random.randrange(1 << 30, 1 << 31)

MODEL_ID = sid("jeevs_anking_basic_model_v2")   # stable across all decks/sessions

CSS = """
.card {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 19px;
    text-align: left;
    color: #1a1a1a;
    background-color: #fafafa;
    line-height: 1.5;
    padding: 14px 18px;
}
.front-tag {
    display: inline-block;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: .04em;
    text-transform: uppercase;
    color: #ffffff;
    background: #2f6f4f;
    padding: 2px 8px;
    border-radius: 4px;
    margin-bottom: 8px;
}
hr#answer { border: none; border-top: 2px solid #2f6f4f; margin: 14px 0; }
img { max-width: 100%; border-radius: 6px; margin-top: 8px; display: block; }
ul { margin-top: 4px; margin-bottom: 4px; padding-left: 22px; }
li { margin-bottom: 4px; }
table { border-collapse: collapse; margin-top: 6px; }
table td, table th { border: 1px solid #ccc; padding: 4px 8px; }
.extra { margin-top: 10px; font-size: 15px; color: #444; }
"""

model = genanki.Model(
    MODEL_ID,
    'Jeevs AnKing-style Basic v2',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
        {'name': 'Category'},   # real field — this is what fixed the bug
        {'name': 'Extra'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{#Category}}<div class="front-tag">{{Category}}</div>{{/Category}}{{Front}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Back}}{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}',
        },
    ],
    css=CSS,
)
```

**If you ever need to change the fields again**, bump the seed string
(`jeevs_anking_basic_model_v3`, etc.) rather than editing v2 in place — genanki
model IDs must stay stable for Anki to treat re-imports as updates rather than
new/duplicate note types, and changing field structure under an existing model
ID that's already been imported into Jeevs's collection can cause conflicts.

### 3.2 Deck IDs, deck names, helper functions

```python
def sid(name):
    random.seed(name)
    return random.randrange(1 << 30, 1 << 31)

def make_deck(deck_name):
    did = sid("jeevs_deck_" + deck_name)     # stable ID derived from the name
    return genanki.Deck(did, deck_name)

ALL_MEDIA = set()

def img_tag(image_dir, filename):
    ALL_MEDIA.add(f'{image_dir}/{filename}')
    return f'<img src="{filename}">'

def add_card(deck, front, back, category):
    note = genanki.Note(
        model=model,
        fields=[front, back, category, ""],   # Front, Back, Category, Extra
        tags=[category.replace(" ", "_")],    # Anki tags can't contain spaces
    )
    deck.add_note(note)
```

**Deck naming convention** (Anki uses `::` for nesting):

```
UNE Neuro::Week 1 DIs::<Category Name>::<Condition Name>
```

e.g. `UNE Neuro::Week 1 DIs::Metabolic Myopathies::Myophosphorylase Deficiency (McArdle's Disease)`

Category-level overview decks go at `...::<Category Name>::Overview`.

### 3.3 Packaging — bundle a whole category into one `.apkg`

A single `genanki.Package` can hold multiple `Deck` objects, which is the
natural unit for "one category = one apkg file, one sub-deck per condition":

```python
package = genanki.Package([deck1, deck2, deck3])
package.media_files = sorted(ALL_MEDIA)
package.write_to_file('/home/claude/Metabolic_Myopathies_AnKing_style.apkg')
```

Then always: copy to `/mnt/user-data/outputs/`, call `present_files` on it.

---

## 4. Card design philosophy

### 4.1 The core correction (learned from user feedback mid-project)

First attempt at Duchenne produced **31 cards** — one atomic fact per card
(AnKing "true" style: one Gowers-sign card, one Trendelenburg card, one calf-
pseudohypertrophy card, etc.). Jeevs's feedback: *"try to not make too many
cards for each... the amount of info is excellent but should be combined."*

**The corrected approach, used for everything since:**
- Group tightly-related facts under one broader question, answer with a
  **bulleted list** in the `Back` field rather than a single sentence.
- Target **≤10 cards per condition**, but **don't pad** — a thin LO 1–2 DI with
  only Natural History + Clinical Presentation genuinely supports fewer cards
  (4–8) than a full LO 1–4 DI with Diagnostic Workup and Treatment sections
  (8–10). Let the source content set the number; never invent filler cards to
  hit a round number, and never cut real content to force a lower count either.
  Consolidate, don't delete.
- A card's `Front` is a **complete, specific question** ("What are the
  epidemiologic features of DMD (incidence, age of diagnosis/ambulation loss,
  life expectancy)?"), not a bare keyword — so the user knows exactly how much
  is being asked for before flipping.
- Tables in the source (GSD family comparison, Duchenne-vs-Becker quick
  compare, RMS four-subtypes table) become a real HTML `<table>` in the `Back`
  field verbatim — a table is often the single highest-yield artifact in a DI
  and shouldn't be atomized into separate cards.
- **Images go on the card whose content they illustrate**, inline in the
  `Back` field via `img_tag()` — never a standalone "here's a picture" card.
  Pathophys diagram → pathophys card. Biopsy photo → diagnostic workup (or
  pathophys, if the DI frames histology as "natural history" rather than a
  diagnostic test — LGMD/IBM do this explicitly). Exam-finding photo → the
  clinical-presentation or key-exam-terms card describing that exact finding.
- Category-level "quick compare" images/tables (Duchenne vs Becker, DM1 vs
  DM2, MG vs LEMS) belong on the **first** condition's definition card if the
  image physically appears there first in the source, since it's the
  orienting figure for the pair — don't force a duplicate second copy on the
  companion condition unless the source repeats the image there too (it
  sometimes does, e.g. the Duchenne-vs-Becker table appears on both panels in
  the source, so both decks got it).

### 4.2 How LO scope predicts card count

Every condition panel has an `lo-badge` (e.g. `1–2`, `1–4`, `1–5`) and often an
explicit "📌 Scope note" callout spelling out what's included:

> Stratified **LO 1–2** — Natural History and Clinical Presentation only.
> [Source] covers diagnostic workup and treatment in real depth, but that's
> intentionally left out here per the Disease Index rule.

**LO 1–2** → Natural History + Clinical Presentation only → typically
4–8 cards (Definition, Epi/Etiology, Pathophysiology, Clinical Presentation —
sometimes split into 2 if there's a lot, e.g. "core pattern" + "associated
findings"). LGMD, all four Metabolic Myopathies conditions, IBM, LEMS, and all
three Neoplastic conditions were LO 1–2 and landed in the 4–8 range. This is
correct and expected — don't try to inflate these to 10.

**LO 1–4 / 1–5** → full DI including Diagnostic Workup, Treatment, sometimes
Monitoring & Complications → typically 9–10 cards. Duchenne, Becker, Myotonic,
Myasthenia Gravis were all full-scope and landed at 10.

### 4.3 Standard card skeleton per condition (adapt as content demands)

For a full-scope (LO 1–4/5) condition, this is the natural card breakdown:
1. Definition (what it is, what causes it at the top level)
2. Epidemiology (+ prognosis if the source has one)
3. Etiology (inheritance pattern, gene, molecular basis)
4. Pathophysiology — mechanism (often splits into 2 cards if there's both a
   "how the protein/mechanism normally works" card and a "what breaks and the
   injury cascade" card)
5. Clinical presentation — core pattern / by-system-or-muscle-group
6. Clinical presentation — second card if there's a lot (e.g. "key exam
   terms/maneuvers" or "associated/systemic findings")
7. Diagnostic workup (+ differential diagnosis folded in)
8. Treatment (+ monitoring folded in, or as its own card if there's enough)

For an LO 1–2 condition, just keep Definition → Epi/Etiology → Pathophysiology
→ Clinical Presentation, splitting only where the source itself clearly splits
(e.g. "during episodes vs. between episodes," "motor vs. autonomic findings").

### 4.4 Comparison cards are gold — always keep them

Whenever the source explicitly frames two conditions against each other (a
"quick compare" table, a "🔑 fastest way to tell them apart" callout, a
mnemonic contrasting triggers/mechanisms), that becomes its own dedicated card,
verbatim structure preserved. Examples already built: Duchenne vs. Becker,
DM1 vs. DM2, CPT II vs. McArdle's (same symptom, different trigger), LEMS vs.
MG (two fastest differentiators), and the three-way inflammatory myositis
table (DM vs. IBM vs. PM). These tend to be the single highest-yield cards in
the whole set — never skip or bury them inside another card.

---

## 5. Build script template (copy this structure per category)

```python
import genanki, random

def sid(name):
    random.seed(name)
    return random.randrange(1 << 30, 1 << 31)

MODEL_ID = sid("jeevs_anking_basic_model_v2")   # reuse — don't recreate
CSS = """..."""                                  # reuse verbatim from §3.1
model = genanki.Model(MODEL_ID, 'Jeevs AnKing-style Basic v2',
                       fields=[...], templates=[...], css=CSS)  # from §3.1

ALL_MEDIA = set()
def make_deck(name): ...     # from §3.2
def img_tag(dir_, fn): ...   # from §3.2
def add_card(deck, front, back, category): ...  # from §3.2

IMG = '/home/claude/<category>_images'

# --- Condition 1 ---
deck1 = make_deck('UNE Neuro::Week 1 DIs::<Category>::<Condition 1>')
add_card(deck1, "Front question?", "Back content" + img_tag(IMG, "x.png"), "Definition")
# ... more cards ...

# --- Condition 2 ---
deck2 = make_deck('UNE Neuro::Week 1 DIs::<Category>::<Condition 2>')
# ... cards ...

package = genanki.Package([deck1, deck2])
package.media_files = sorted(ALL_MEDIA)
package.write_to_file('/home/claude/<Category>_AnKing_style.apkg')
print("Condition 1 cards:", len(deck1.notes))
print("Condition 2 cards:", len(deck2.notes))
print("Total media files:", len(ALL_MEDIA))
```

After running: verify the zip structure sanity-checks
(`zipfile.ZipFile(path).namelist()` should show `collection.anki2`, `media`,
and one numbered file per media entry), copy to `/mnt/user-data/outputs/`,
`present_files`.

---

## 6. Known issues / technical debt

**The first four decks predate the model fix and the correct deck path.**
Built early in the project, before Jeevs corrected the deck hierarchy and
before the `{{Front tag}}` bug was caught:

| Condition | apkg file | Deck path used (WRONG) | Model used |
|---|---|---|---|
| Duchenne MD | `DMD_AnKing_style.apkg` | `Block 5::Neuromuscular::Disease Index::Duchenne Muscular Dystrophy` | v1 (broken `{{Front tag}}`) |
| Becker MD | `BeckerMD_AnKing_style.apkg` | `Block 5::Neuromuscular::Disease Index::Becker Muscular Dystrophy` | v1 |
| Myotonic Dystrophy | `MyotonicDystrophy_AnKing_style.apkg` | `Block 5::Neuromuscular::Disease Index::Myotonic Dystrophy` | v1 |
| Limb-Girdle MD | `LGMD_AnKing_style.apkg` | `Block 5::Neuromuscular::Disease Index::Limb-Girdle Muscular Dystrophy` | v1 |

They *should* live at `UNE Neuro::Week 1 DIs::Muscular Dystrophies::<condition>`
using the v2 model, matching everything built afterward. Jeevs manually patched
the "empty front" symptom in Anki itself by changing the note/card type, so
these are usable in his live collection right now — but the source `.apkg`
files in `/mnt/user-data/outputs/` still reflect the old broken template and
wrong deck path. **If asked to revisit these four**, the clean fix is to
regenerate them with the current v2 model/script pattern and the corrected
deck path, and give Jeevs the option to delete the old note type/cards in Anki
before reimporting (to avoid duplicates) — don't just silently reissue new
files without flagging that the deck path will change.

**Always check for a category overview panel.** Missed on the first pass for
Muscular Dystrophies (`panel-md-overview`) and Metabolic Myopathies
(`panel-met-overview`) — both were built later, retroactively, once Jeevs
noticed and asked. Confirmed **no** overview panel exists for NMJ Disorders or
Neoplastic Disorders (grepped explicitly, cat-count matched exactly the
conditions listed, no `overview` data-panel present). Do this grep check for
every category, every time, before considering it done:
```bash
grep -n 'panel-<catid>-overview' week1_DIs.html
```

---

## 7. Full inventory as of end of Week 1 DI

| Category | Sub-deck | LO scope | Cards | Images | apkg file |
|---|---|---|---|---|---|
| Muscular Dystrophies | Overview | — | 5 | 1 | `Category_Overviews_AnKing_style.apkg` |
| Muscular Dystrophies | Duchenne MD *(legacy path/model — see §6)* | 1–5 | 10 | 5 | `DMD_AnKing_style.apkg` |
| Muscular Dystrophies | Becker MD *(legacy)* | 1–5 | 10 | 1 | `BeckerMD_AnKing_style.apkg` |
| Muscular Dystrophies | Myotonic Dystrophy *(legacy)* | 1–4 | 10 | 4 | `MyotonicDystrophy_AnKing_style.apkg` |
| Muscular Dystrophies | Limb-Girdle MD *(legacy)* | 1–2 | 5 | 3 | `LGMD_AnKing_style.apkg` |
| Metabolic Myopathies | Overview | — | 4 | 0 | `Category_Overviews_AnKing_style.apkg` |
| Metabolic Myopathies | Acid Maltase Deficiency (Pompe) | 1–2 | 7 | 1 | `Metabolic_Myopathies_AnKing_style.apkg` |
| Metabolic Myopathies | Myophosphorylase Deficiency (McArdle's) | 1–2 | 7 | 2 | same |
| Metabolic Myopathies | CPT II Deficiency | 1–2 | 6 | 0 | same |
| Metabolic Myopathies | Mitochondrial Myopathy | 1–2 | 8 | 0 | same |
| Inflammatory Myopathies | Overview (DM & PM context) | — | 5 | 4 | `Inflammatory_Myopathies_AnKing_style.apkg` |
| Inflammatory Myopathies | Inclusion Body Myositis | 1–2 | 7 | 2 | same |
| NMJ Disorders | Myasthenia Gravis | 1–4 | 10 | 3 | `NMJ_Disorders_AnKing_style.apkg` |
| NMJ Disorders | LEMS | 1–2 | 5 | 4 | same |
| Neoplastic Disorders | Leiomyoma | 1–2 | 5 | 3 | `Neoplastic_Disorders_AnKing_style.apkg` |
| Neoplastic Disorders | Leiomyosarcoma | 1–2 | 4 | 1 | same |
| Neoplastic Disorders | Rhabdomyosarcoma | 1–2 | 5 | 2 | same |

**Totals: 18 sub-decks, 113 cards, 35 unique images, 9 `.apkg` files, across all
8 categories in `week1_DIs.html`. The entire file is covered.**

---

## 8. Quick-start checklist for a new DI file (e.g. `week2_DIs.html`)

1. Read the sidebar block fully. List every category, every condition, every
   `lo-badge`, and whether each category has an `-overview` panel.
2. For each category, in order:
   a. If there's an overview panel, extract and build it first (it often
      contains the genotype-phenotype/mechanism table that individual
      condition cards will reference or that orients the whole category).
   b. For each condition: grep boundaries → extract clean text → note image
      line numbers → extract images → view every image → design the card
      list (Definition → Epi/Etiology → Pathophys → Clinical → [Workup] →
      [Treatment], split/combine per §4.3/§4.2) → write the build script →
      run it → verify zip contents → copy to outputs → present.
3. Use the **v2 model verbatim** (§3.1). Don't reintroduce the `{{Front tag}}`
   bug or any other unbound field reference in a template.
4. Deck path: `UNE Neuro::Week <N> DIs::<Category>::<Condition>`.
5. Package one whole category (all its conditions + its overview) into a
   single `.apkg` per build script, unless the category is large enough that
   Jeevs asks for it split up for easier review.
6. After finishing a category, briefly summarize card counts/images per
   condition back to Jeevs before moving to the next category — he's been
   reviewing each batch before giving the go-ahead to continue.
