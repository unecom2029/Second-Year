#!/usr/bin/env python3
"""Inject finished content into OMK_2A_Cardio_Summative_Objective_Review.html.

The HTML page is the source of truth. This script only replaces marked regions,
so it is safe to re-run after editing any fragment.

  _build/sections/<section-id>.html  -> everything inside <section id="<section-id>"> ... </section>
  _build/hy/<section-id>.html        -> that section's block in the High-Yield One-Pager
  _build/checklist.html              -> the cards inside the Master High-Yield Checklist
  _build/glossary.html               -> the body of the Glossary section
  _build/pending.html                -> the body of Objectives Still Pending
  _build/status.json                 -> objective statuses + TOC label overrides

Run:  python3 _build/inject.py      (from OMK/Cardio/summative)
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGE = HERE.parent / 'OMK_2A_Cardio_Summative_Objective_Review.html'
s = PAGE.read_text(encoding='utf-8')

def die(msg):
    sys.exit('inject.py: ' + msg)

# ---------------------------------------------------------------- content CSS (_build/content.css)
A_CSS, B_CSS = '/*==CONTENT CSS==*/', '/*==/CONTENT CSS==*/'
# migrate the first-version block, which had no end marker
old = re.search(r'\n/\* ============ EMPHASIS LAYER.*?(?=/\* ============ SHELL PLACEHOLDERS)', s, re.S)
if old and A_CSS not in s:
    s = s[:old.start()] + '\n' + s[old.end():]
if A_CSS not in s:
    s = s.replace('/* ============ SHELL PLACEHOLDERS', A_CSS + B_CSS + '\n/* ============ SHELL PLACEHOLDERS', 1)
css = (HERE / 'content.css').read_text(encoding='utf-8').strip()
i, j = s.find(A_CSS), s.find(B_CSS)
s = s[:i + len(A_CSS)] + '\n' + css + '\n' + s[j:]

# ---------------------------------------------------------------- sections
for frag in sorted((HERE / 'sections').glob('*.html')):
    sid = frag.stem
    open_tag = f'<section class="section" id="{sid}">'
    i = s.find(open_tag)
    if i < 0:
        die(f'no <section id="{sid}"> in page')
    j = s.find('</section>', i)
    body = frag.read_text(encoding='utf-8').rstrip() + '\n'
    s = s[:i + len(open_tag)] + '\n' + body + s[j:]
    print('section', sid)

# ---------------------------------------------------------------- one-pager blocks
for frag in sorted((HERE / 'hy').glob('*.html')) if (HERE / 'hy').exists() else []:
    sid = frag.stem
    block = frag.read_text(encoding='utf-8').strip()
    if f'data-sec="{sid}"' not in block:
        die(f'hy/{sid}.html must carry data-sec="{sid}" on its hy-block')
    # already injected once: replace it
    pat = re.compile(r'<div class="hy-block" data-sec="%s">.*?</div><!--/hy-%s-->' % (re.escape(sid), re.escape(sid)), re.S)
    new = block + f'<!--/hy-{sid}-->'
    if pat.search(s):
        s = pat.sub(lambda m: new, s, count=1)
    else:
        # first time: replace the shell placeholder for this section (matched by its TOC label)
        m = re.search(r'<a href="#%s"><span class="toc-num">\d+</span><span>(.*?)</span>' % re.escape(sid), s)
        if not m:
            die(f'cannot find TOC label for {sid}')
        placeholder = f'<div class="hy-block"><h4>{m.group(1)}</h4><p class="shell-todo">To come</p></div>'
        if placeholder not in s:
            die(f'cannot find one-pager placeholder for {sid} (label "{m.group(1)}")')
        s = s.replace(placeholder, new, 1)
    print('one-pager', sid)

# ---------------------------------------------------------------- marked regions
def region(name, start_anchor, placeholder):
    """Replace <!--NAME-->...<!--/NAME--> with _build/<name>.html; create markers on first run."""
    f = HERE / f'{name}.html'
    if not f.exists():
        return
    global s
    body = f.read_text(encoding='utf-8').strip()
    a, b = f'<!--{name.upper()}-->', f'<!--/{name.upper()}-->'
    if a not in s:
        k = s.find(start_anchor)
        if k < 0 or s.find(placeholder, k) < 0:
            die(f'cannot place region {name}')
        p = s.find(placeholder, k)
        s = s[:p] + a + b + s[p + len(placeholder):]
    i, j = s.find(a), s.find(b)
    s = s[:i + len(a)] + '\n' + body + '\n' + s[j:]
    print('region', name)

region('checklist', 'id="checklist"', '<div class="hallmarks-grid"></div>\n  <p class="shell-todo">Cards to come</p>')
region('glossary', 'id="glossary"', '<p class="shell-todo">Glossary to come</p>')
region('pending', 'id="pending"', '<p class="shell-todo">List to come</p>')

# ---------------------------------------------------------------- statuses + counters
st_file = HERE / 'status.json'
if st_file.exists():
    st = json.loads(st_file.read_text())
    status = {str(k): v for k, v in st.get('objectives', {}).items()}
    LABEL = {'full': 'Covered', 'part': 'Partial', 'none': 'Not written yet'}

    def fix_row(m):
        n = m.group(2)
        v = status.get(n, 'none')
        row = m.group(0)
        row = re.sub(r'data-st="\w+"', f'data-st="{v}"', row, count=1)
        row = re.sub(r'<span class="cov-status \w+">[^<]*</span>', f'<span class="cov-status {v}">{LABEL[v]}</span>', row, count=1)
        return row
    s = re.sub(r'(<tr class="lo-row" data-st="\w+"><td>(\d+)</td>.*?</tr>)', fix_row, s, flags=re.S)

    rows = re.findall(r'<tr class="lo-row" data-st="(\w+)">', s)
    full, part, none = rows.count('full'), rows.count('part'), rows.count('none')
    total = len(rows)
    s = re.sub(r'<span class="n">\d+</span><span class="l">Covered in full</span>', f'<span class="n">{full}</span><span class="l">Covered in full</span>', s)
    s = re.sub(r'<span class="n">\d+</span><span class="l">Partially covered</span>', f'<span class="n">{part}</span><span class="l">Partially covered</span>', s)
    s = re.sub(r'<span class="n">\d+</span><span class="l">Not written yet</span>', f'<span class="n">{none}</span><span class="l">Not written yet</span>', s)
    s = re.sub(r'(<span class="label">Fully covered</span><span class="value">)\d+', rf'\g<1>{full}', s)
    s = re.sub(r'(<span class="label">Partly covered</span><span class="value">)\d+', rf'\g<1>{part}', s)
    s = re.sub(r'<span class="lo-badge src">\d+ objectives not written yet</span>',
               f'<span class="lo-badge src">{none} objectives not written yet</span>', s)

    # TOC label overrides (e.g. a renamed section)
    for sid, label in st.get('toc_labels', {}).items():
        s, n = re.subn(r'(<a href="#%s"><span class="toc-num">\d+</span><span>)(.*?)(</span>)' % re.escape(sid),
                       lambda m: m.group(1) + label + m.group(3), s, count=1)
        if not n:
            die(f'TOC label override failed for {sid}')
    print(f'status: {full} full · {part} partial · {none} not written · {total} total')

# exam-question counter in the hero
nq = s.count('<div class="exam-q">')
s = re.sub(r'(<span class="label">Exam questions</span><span class="value">)\d+', rf'\g<1>{nq}', s)

PAGE.write_text(s, encoding='utf-8')
print('wrote', PAGE.name, len(s), 'bytes ·', nq, 'exam questions')
