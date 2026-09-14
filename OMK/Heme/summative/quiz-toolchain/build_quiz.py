import re,json,base64,importlib.util,os
def load(n,p):
    sp=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
import sys
QUESTIONS_PY = sys.argv[1] if len(sys.argv)>1 else "questions_batch01_hematopoiesis_marrow.py"
TAGS_PY      = sys.argv[2] if len(sys.argv)>2 else "lo_tags_batch01.py"
QUIZ_TITLE   = sys.argv[3] if len(sys.argv)>3 else "Jeevs Edition — Hematopoiesis & Marrow"
OUT_NAME     = sys.argv[4] if len(sys.argv)>4 else "Jeevs Edition - Hematopoiesis and Marrow Quiz.html"
Q=load("m",QUESTIONS_PY).Q
TAGS=load("t",TAGS_PY).LO_TAGS
SUMM="/Users/jeeval/Documents/GitHub/Second-Year/OMK/Heme/summative/"
LOMAP=json.load(open(SUMM+"heme_summative3_lo_question_map.json"))["objectives"]
for i,q in enumerate(Q,1):
    q["los"]=[{"n":lo,"t":LOMAP[str(lo)]["objective"],
               "a":LOMAP[str(lo)]["anchors"][0] if LOMAP[str(lo)]["anchors"] else "",
               "s":LOMAP[str(lo)]["sections"][0] if LOMAP[str(lo)]["sections"] else ""} for lo in TAGS[i]]

# ---- lab panels: inline "Laboratory studies show:" block -> structured q["labs"] ----
LAB_LINE=re.compile(r'^(.*?)\s((?:[<>]?\d).*?)(?:\s*\((N=[^)]*)\))?$')
LAB_BLOCK=re.compile(r'(Laboratory studies[^\n:]*:)\n((?:.+\n?)+?)(?=\n|$)')
def _rows(block):
    out=[]
    for ln in block.strip().split("\n"):
        ln=ln.strip()
        if not ln: continue
        mm=LAB_LINE.match(ln)
        if not mm: raise ValueError("unparseable lab line: "+ln)
        ref=(mm.group(3) or "")
        out.append({"t":mm.group(1).strip(),"r":mm.group(2).strip(),
                    "n":ref[2:].strip() if ref.startswith("N=") else ref.strip()})
    return out
for i,q in enumerate(Q,1):
    mo=LAB_BLOCK.search(q["stem"])
    if not mo: continue
    q["labs"]={"title":mo.group(1),"rows":_rows(mo.group(2))}
    q["stem"]=q["stem"][:mo.start()]+"[[LABS]]"+q["stem"][mo.end():]

TPL="/Users/jeeval/Documents/GitHub/Second-Year/OMK/Heme/week 11/quiz/UWorld Edition/Hematopoiesis and Neoplastic Disorders Quiz.html"
OUT=SUMM+OUT_NAME
s=open(TPL,encoding="utf-8").read()
used={q[k] for q in Q for k in ("image","explanationImage") if q.get(k)}
FIGDIR=os.environ.get("FIGDIR","figs")
figs={k:"data:image/jpeg;base64,"+base64.b64encode(open(os.path.join(FIGDIR,k+".jpg"),"rb").read()).decode() for k in sorted(used)}
def rep(a,b):
    global s
    assert s.count(a)>=1,("MISSING",a[:90]); s=s.replace(a,b,1)
s=s.replace("<title>Hematopoiesis and Neoplastic Disorders — UWorld Edition Quiz</title>","<title>"+QUIZ_TITLE.replace("&","&amp;")+" Quiz</title>",1)
s=re.sub(r'PRELOADED_QUIZ_NAME="[^"]*";',lambda _:'PRELOADED_QUIZ_NAME='+json.dumps(QUIZ_TITLE,ensure_ascii=False)+';',s,count=1)
s=re.sub(r'var PRELOADED_QUESTIONS_JSON="[^\r\n]*";',lambda _:'var PRELOADED_QUESTIONS_JSON='+json.dumps(json.dumps(Q,ensure_ascii=False),ensure_ascii=False)+';',s,count=1)
s=re.sub(r'var QUIZ_FIGURES=\{.*?\};\n',lambda _:'var QUIZ_FIGURES='+json.dumps(figs)+';\n',s,count=1,flags=re.S)
rep(".qstem{font-family:var(--font-ui);font-size:var(--stem-size);line-height:1.45;margin-bottom:22px;font-weight:400;color:var(--ink);letter-spacing:0}",
    ".qstem{font-family:var(--font-ui);font-size:var(--stem-size);line-height:1.45;margin-bottom:22px;font-weight:400;color:var(--ink);letter-spacing:0;white-space:pre-line}")
rep(".nb-question-stem{font-size:calc(var(--stem-size) * .72);line-height:1.58;user-select:text}",
    ".nb-question-stem{font-size:calc(var(--stem-size) * .72);line-height:1.58;user-select:text;white-space:pre-line}")
rep("    explanationImageCaption:q.explanationImageCaption?String(q.explanationImageCaption):''\n  };",
    "    explanationImageCaption:q.explanationImageCaption?String(q.explanationImageCaption):'',\n    los:Array.isArray(q.los)?q.los.slice():[],\n    labs:q.labs&&q.labs.rows?q.labs:null\n  };")
rep("explanationImage:source.explanationImage,explanationImageCaption:source.explanationImageCaption};",
    "explanationImage:source.explanationImage,explanationImageCaption:source.explanationImageCaption,los:Array.isArray(source.los)?source.los.slice():[],labs:source.labs||null};")
rep("explanationImage:q.explanationImage?String(q.explanationImage):'',explanationImageCaption:q.explanationImageCaption?String(q.explanationImageCaption):''};",
    "explanationImage:q.explanationImage?String(q.explanationImage):'',explanationImageCaption:q.explanationImageCaption?String(q.explanationImageCaption):'',los:Array.isArray(q.los)?q.los.slice():[],labs:q.labs&&q.labs.rows?q.labs:null};")
rep("""function getStemHTML(index){
  return stemMarkup[index]!=null?stemMarkup[index]:questions[index].stem;
}""",
"""function getStemHTML(index){
  var base=stemMarkup[index]!=null?stemMarkup[index]:questions[index].stem;
  if(base.indexOf('[[LABS]]')>-1)base=base.replace('[[LABS]]',labTableHTML(questions[index]));
  return base;
}""")
rep("function buildFigureHTML(index){",
"""var LO_REVIEW_FILE='OMK_2A_Heme_Summative_3_Objective_Review.html';
function labTableHTML(q){
  var L=q&&q.labs;
  if(!L||!L.rows||!L.rows.length)return '';
  var cap=L.title?'<div class="labt-cap">'+escapeStudyText(L.title)+'</div>':'';
  var head='<div class="labt-row labt-head"><span>Test</span><span>Result</span><span>Reference range</span></div>';
  var body=L.rows.map(function(r){
    return '<div class="labt-row"><span class="labt-t">'+escapeStudyText(r.t)+'</span>'+
           '<span class="labt-v">'+escapeStudyText(r.r)+'</span>'+
           '<span class="labt-n">'+escapeStudyText(r.n||'\\u2014')+'</span></div>';
  }).join('');
  var foot='<div class="labt-foot">Typical educational ranges are shown. Actual reference intervals vary by laboratory, age, sex, and clinical context.</div>';
  return cap+'<div class="labt">'+head+body+foot+'</div>';
}
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
    <div class="exs exc"><div class="exl">✓ Why ${correctLetter} is Correct</div><div class="ext">${q.explanation}</div></div>
    ${myWrong}${others}${eli5}${figBlock}
  </div>`;""",
"""return `<div class="exb vis">
    ${loBlockHTML(q)}
    <div class="exs exc"><div class="exl">✓ Why ${correctLetter} is Correct</div><div class="ext">${q.explanation}</div></div>
    ${myWrong}${others}${eli5}${figBlock}
  </div>`;""")
rep(".qfig{margin:18px 0 4px;padding:10px;border:1px solid rgba(18,32,60,.14);border-radius:14px;background:#fff;overflow-x:auto}",
""".labt-cap{margin:18px 0 8px;white-space:normal}
.labt{white-space:normal;border:1px solid rgba(18,32,60,.13);border-radius:14px;overflow:hidden;background:#fff;margin:0 0 20px;font-size:.94em}
.labt-row{display:grid;grid-template-columns:minmax(0,1.45fr) minmax(0,.95fr) minmax(0,1.15fr);gap:14px;padding:11px 18px;align-items:baseline}
.labt-row+.labt-row{border-top:1px solid rgba(18,32,60,.07)}
.labt-row:nth-child(even){background:rgba(18,32,60,.028)}
.labt-head{background:rgba(18,32,60,.055);font-family:'IBM Plex Mono',Consolas,monospace;font-size:.76em;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--slate,#6B7689)}
.labt-head span:nth-child(2),.labt-head span:nth-child(3){text-align:right}
.labt-t{font-weight:700;color:var(--ink,#1E1E20)}
.labt-v{text-align:right;font-variant-numeric:tabular-nums;color:var(--ink,#1E1E20)}
.labt-n{text-align:right;font-variant-numeric:tabular-nums;color:var(--slate,#6B7689)}
.labt-foot{padding:10px 18px 12px;border-top:1px solid rgba(18,32,60,.07);font-size:.8em;line-height:1.45;color:var(--mist,#A0AAB8)}
@media(max-width:620px){
  .labt-row{grid-template-columns:1fr auto;gap:4px 12px;padding:10px 14px}
  .labt-head{display:none}
  .labt-v{grid-column:2}
  .labt-n{grid-column:1/-1;text-align:left;font-size:.86em}
}
.exs.exlo{background:var(--gold-bg,#FDF6E3);border-left:5px solid var(--coral,#E07A5F)}
.exs.exlo .exl{color:var(--coral,#E07A5F)}
.lo-row{display:flex;gap:10px;align-items:flex-start}
.lo-row+.lo-row{margin-top:9px;padding-top:9px;border-top:1px solid rgba(224,122,95,.18)}
.lo-chip{flex:0 0 auto;display:inline-block;font-family:'IBM Plex Mono',Consolas,monospace;font-size:11px;font-weight:700;letter-spacing:.6px;padding:3px 9px;border-radius:999px;background:var(--coral,#E07A5F);color:#fff;text-decoration:none;white-space:nowrap}
.lo-chip:hover{filter:brightness(1.12)}
.lo-text{font-size:.9em;line-height:1.55;color:var(--ink2,#3E4555);white-space:normal}
.lo-sec{display:inline-block;margin-left:7px;font-family:'IBM Plex Mono',Consolas,monospace;font-size:10.5px;color:var(--slate,#6B7689)}
.qfig{margin:18px 0 4px;padding:10px;border:1px solid rgba(18,32,60,.14);border-radius:14px;background:#fff;overflow-x:auto}""")
open(OUT,"w",encoding="utf-8").write(s)
print("rebuilt %.2f MB"%(len(s)/1e6))
