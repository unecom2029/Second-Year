import json,re,html,glob,importlib.util
S="../"
idx=json.load(open("uworld_index.json"))
heme=[a["title"] for a in idx if a["folderPath"] and a["folderPath"][0]=="Hematology & Oncology"]
rev=open(S+"OMK_2A_Heme_Summative_3_Objective_Review.html",encoding="utf-8").read()
rev=re.sub(r'data:image/[^"\')]+','',rev)
secs=[]
for m in re.finditer(r'<section class="section" id="(s[^"]+)">',rev):
    nxt=rev.find('<section class="section" id="',m.end())
    body=rev[m.start():nxt if nxt>0 else len(rev)]
    lab=re.search(r'<p class="section-label">Section (\d+)',body)
    txt=html.unescape(re.sub(r'<[^>]+>',' ',body)).lower()
    secs.append((m.group(1), "§"+lab.group(1) if lab else "?", txt))
qtext=""
for f in glob.glob(S+"quiz-toolchain/questions_batch*.py"):
    sp=importlib.util.spec_from_file_location("m",f); mod=importlib.util.module_from_spec(sp); sp.loader.exec_module(mod)
    qtext+=json.dumps(mod.Q).lower()
STOP={"an","a","of","and","the","to","in","for","on","overview","disease","disorders","syndrome","syndromes","anemia","anemias"}
rows=[]
for t in heme:
    kws=[w for w in re.findall(r'[a-zA-Z][a-zA-Z\-]{3,}',t.lower()) if w not in STOP]
    if not kws: kws=[t.lower()]
    best,score=None,0
    for sid,num,txt in secs:
        sc=sum(txt.count(k) for k in kws)
        if sc>score: best,score=(sid,num),sc
    inq=sum(1 for k in kws if k in qtext)
    rows.append((t,best[1] if best else "-",score,"yes" if inq>=max(1,len(kws)//2) else "no"))
print(f'{"UWorld Heme/Onc article":58s} {"review §":8s} {"hits":>5}  in-quiz')
for t,sec,sc,inq in rows:
    print(f'{t[:58]:58s} {sec:8s} {sc:>5}  {inq}')
print("\nNOT FOUND in review file (score 0):")
for t,sec,sc,inq in rows:
    if sc==0: print("  -",t)
