"""Build a Jeevs Edition quiz from a questions module + an LO-tags module.

usage: FIGDIR=figs python3 build_quiz.py QUESTIONS_PY TAGS_PY "Quiz Title" "Output File.html"
"""
import re, json, base64, importlib.util, os, sys
sys.dont_write_bytecode = True  # keep __pycache__ out of the repo

HERE = os.path.dirname(os.path.abspath(__file__))
SUMM = os.path.dirname(HERE) + os.sep
TPL = os.path.join(os.path.dirname(os.path.dirname(HERE)),
                   "week 11", "quiz", "UWorld Edition", "Hematopoiesis and Neoplastic Disorders Quiz.html")
REVIEW = SUMM + "OMK_2A_Heme_Summative_3_Objective_Review.html"
LOMAP_PATH = SUMM + "heme_summative3_lo_question_map.json"

QUESTIONS_PY = sys.argv[1] if len(sys.argv) > 1 else "questions_batch01_hematopoiesis_marrow.py"
TAGS_PY      = sys.argv[2] if len(sys.argv) > 2 else "lo_tags_batch01.py"
QUIZ_TITLE   = sys.argv[3] if len(sys.argv) > 3 else "Jeevs Edition — Hematopoiesis & Marrow"
OUT_NAME     = sys.argv[4] if len(sys.argv) > 4 else "Jeevs Edition - Hematopoiesis and Marrow Quiz.html"
FIGDIR       = os.environ.get("FIGDIR", os.path.join(HERE, "figs"))


def load(name, path):
    sp = importlib.util.spec_from_file_location(name, os.path.join(HERE, path))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m


Q = load("questions", QUESTIONS_PY).Q
TAGS = load("tags", TAGS_PY).LO_TAGS
LOMAP = json.load(open(LOMAP_PATH))["objectives"]
assert len(TAGS) == len(Q), f"{len(Q)} questions but {len(TAGS)} LO tag entries"

# ── 1. LO tags → q["los"] ─────────────────────────────────────────────────────
# A tag is an LO number, or (LO number, "section-anchor") to deep-link a specific section.
REV = open(REVIEW, encoding="utf-8").read()
SECNUM = {}
for m in re.finditer(r'<section class="section" id="([^"]+)">', REV):
    lab = re.search(r'<p class="section-label">Section (\d+)', REV[m.end():m.end() + 1500])
    if lab: SECNUM[m.group(1)] = "§" + lab.group(1)

for i, q in enumerate(Q, 1):
    q["los"] = []
    for tag in TAGS[i]:
        lo, anc = tag if isinstance(tag, (tuple, list)) else (tag, None)
        e = LOMAP[str(lo)]
        a = anc or (e["anchors"][0] if e["anchors"] else "")
        assert a in SECNUM, f"Q{i}: anchor {a!r} not found in review file"
        q["los"].append({"n": lo, "t": e["objective"], "a": a, "s": SECNUM[a]})

# ── 2. Lab blocks → the template's native lab-panel format ─────────────────────
# Authors write:            Hemoglobin 8.6 g/dL (N=13.5–17.5 g/dL)
# Template renders rows of: "  Hemoglobin  8.6 g/dL (N=13.5–17.5 g/dL)"
# (2-space indent, name, 2+ spaces, value). An explicit (N=…) overrides the template's
# built-in TYPICAL_LAB_RANGES, so ranges stay consistent with index.html LAB_SECTIONS.
LAB_LINE = re.compile(r'^(.*?)\s((?:[<>]?\d).*)$')
LAB_BLOCK = re.compile(r'(Laboratory studies[^\n:]*:)\n((?:[^\n]+\n?)+?)(?=\n|$)')


def _native(block, qn):
    rows = []
    for ln in block.strip().split("\n"):
        ln = ln.strip()
        if not ln: continue
        mm = LAB_LINE.match(ln)
        if not mm: raise ValueError(f"Q{qn}: unparseable lab line: {ln!r}")
        if "(N=" not in mm.group(2): raise ValueError(f"Q{qn}: lab line has no (N=…) range: {ln!r}")
        rows.append(f"  {mm.group(1).strip()}  {mm.group(2).strip()}")
    if len(rows) < 2: raise ValueError(f"Q{qn}: native lab panel needs ≥2 rows")
    return "\n".join(rows)


for i, q in enumerate(Q, 1):
    q["stem"] = LAB_BLOCK.sub(lambda mo: mo.group(1) + "\n" + _native(mo.group(2), i), q["stem"])

# ── 3. Clone template ─────────────────────────────────────────────────────────
s = open(TPL, encoding="utf-8").read()


def rep(a, b):
    """Required patch — fail loudly if the template has drifted."""
    global s
    assert s.count(a) == 1, f"template drift — patch target not found exactly once: {a[:90]!r}"
    s = s.replace(a, b, 1)


used = sorted({q[k] for q in Q for k in ("image", "explanationImage") if q.get(k)})
figs = {k: "data:image/jpeg;base64," + base64.b64encode(open(os.path.join(FIGDIR, k + ".jpg"), "rb").read()).decode()
        for k in used}

s = re.sub(r'<title>[^<]*</title>', lambda _: "<title>" + QUIZ_TITLE.replace("&", "&amp;") + " Quiz</title>", s, count=1)
s = re.sub(r'PRELOADED_QUIZ_NAME="[^"]*";', lambda _: 'PRELOADED_QUIZ_NAME=' + json.dumps(QUIZ_TITLE, ensure_ascii=False) + ';', s, count=1)
s = re.sub(r'var PRELOADED_QUESTIONS_JSON="[^\r\n]*";',
           lambda _: 'var PRELOADED_QUESTIONS_JSON=' + json.dumps(json.dumps(Q, ensure_ascii=False), ensure_ascii=False) + ';', s, count=1)
s = re.sub(r'var QUIZ_FIGURES=\{.*?\};\n', lambda _: 'var QUIZ_FIGURES=' + json.dumps(figs) + ';\n', s, count=1, flags=re.S)

# The template must already render newlines and lab panels natively.
assert "function formatStemText" in s and "white-space:pre-wrap" in s, \
    "template lacks native stem formatting — see QUIZ_BUILD_METHOD.md §6"

# ── 4. Thread `los` through the three question normalizers ─────────────────────
rep("    explanationImageCaption:q.explanationImageCaption?String(q.explanationImageCaption):''\n  };",
    "    explanationImageCaption:q.explanationImageCaption?String(q.explanationImageCaption):'',\n    los:Array.isArray(q.los)?q.los.slice():[]\n  };")
rep("explanationImage:source.explanationImage,explanationImageCaption:source.explanationImageCaption};",
    "explanationImage:source.explanationImage,explanationImageCaption:source.explanationImageCaption,los:Array.isArray(source.los)?source.los.slice():[]};")
rep("explanationImage:q.explanationImage?String(q.explanationImage):'',explanationImageCaption:q.explanationImageCaption?String(q.explanationImageCaption):''};",
    "explanationImage:q.explanationImage?String(q.explanationImage):'',explanationImageCaption:q.explanationImageCaption?String(q.explanationImageCaption):'',los:Array.isArray(q.los)?q.los.slice():[]};")

# ── 5. LO block at the top of every explanation ───────────────────────────────
rep("function buildFigureHTML(index){",
"""var LO_REVIEW_FILE='OMK_2A_Heme_Summative_3_Objective_Review.html';
function loBlockHTML(q){
  var los=(q&&Array.isArray(q.los))?q.los:[];
  if(!los.length)return '';
  var rows=los.map(function(lo){
    var href=LO_REVIEW_FILE+(lo.a?('#'+lo.a):'');
    var sec=lo.s?'<span class="lo-sec">'+escapeStudyText(lo.s)+'</span>':'';
    return '<div class="lo-row"><a class="lo-chip" href="'+href+'" target="_blank" rel="noopener">LO '+escapeStudyText(lo.n)+'</a>'+
           '<span class="lo-text">'+escapeStudyText(lo.t)+sec+'</span></div>';
  }).join('');
  return '<div class="exs exlo"><div class="exl">\\uD83C\\uDFAF Learning Objective'+(los.length>1?'s':'')+' tested</div><div class="ext">'+rows+'</div></div>';
}
function buildFigureHTML(index){""")
rep("""return `<div class="exb vis">
    <div class="exs exc">""",
"""return `<div class="exb vis">
    ${loBlockHTML(q)}
    <div class="exs exc">""")

rep(".qfig{margin:18px 0 4px;padding:10px;border:1px solid rgba(18,32,60,.14);border-radius:14px;background:#fff;overflow-x:auto}",
""".exs.exlo{background:var(--gold-bg,#FDF6E3);border-left:5px solid var(--coral,#E07A5F)}
.exs.exlo .exl{color:var(--coral,#E07A5F)}
.exb .exs .ext{white-space:pre-line}
.exs.exlo .ext{white-space:normal}
.lo-row{display:flex;gap:10px;align-items:flex-start}
.lo-row+.lo-row{margin-top:9px;padding-top:9px;border-top:1px solid rgba(224,122,95,.18)}
.lo-chip{flex:0 0 auto;display:inline-block;font-family:'IBM Plex Mono',Consolas,monospace;font-size:11px;font-weight:700;letter-spacing:.6px;padding:3px 9px;border-radius:999px;background:var(--coral,#E07A5F);color:#fff;text-decoration:none;white-space:nowrap}
.lo-chip:hover{filter:brightness(1.12)}
.lo-text{font-size:.9em;line-height:1.55;color:var(--ink2,#3E4555)}
.lo-sec{display:inline-block;margin-left:7px;font-family:'IBM Plex Mono',Consolas,monospace;font-size:10.5px;color:var(--slate,#6B7689)}
.qfig{margin:18px 0 4px;padding:10px;border:1px solid rgba(18,32,60,.14);border-radius:14px;background:#fff;overflow-x:auto}""")

open(SUMM + OUT_NAME, "w", encoding="utf-8").write(s)
print(f"built {OUT_NAME}  ({len(Q)} questions, {len(figs)} figures, {len(s)/1e6:.2f} MB)")
