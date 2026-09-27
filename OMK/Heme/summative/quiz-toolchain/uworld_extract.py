import json,re,sys,base64,html
F="/Users/jeeval/Board Study/figures/Text/UWorld - Complete All 26 Collections - 1241 Articles.html"
IDX="uworld_index.json"
idx=json.load(open(IDX))
want=[t.lower() for t in sys.argv[1:]]
targets={i for i,a in enumerate(idx) if any(w in a["title"].lower() for w in want)}
print("matched:",[idx[i]["title"] for i in sorted(targets)],file=sys.stderr)
out={}
with open(F,encoding="utf-8",errors="ignore") as f:
    buf=""; total=0
    while targets:
        chunk=f.read(8_000_000)
        if not chunk: break
        buf+=chunk; total+=len(chunk)
        for m in re.finditer(r'<script[^>]{0,120}id="article-(\d+)"[^>]*>',buf):
            n=int(m.group(1))
            if n in targets:
                end=buf.find("</script>",m.end())
                if end==-1: continue
                out[n]=buf[m.end():end].strip(); targets.discard(n)
        buf=buf[-2_000_000:]
        if total>90_000_000: break
def decode(raw):
    raw=raw.strip()
    if raw.startswith('"') or raw.startswith('{'):
        try:
            d=json.loads(raw)
            raw=d if isinstance(d,str) else (d.get("html") or d.get("content") or "")
        except Exception: pass
    try: return base64.b64decode(raw).decode("utf-8","ignore")
    except Exception: return raw
for n,raw in sorted(out.items()):
    h=decode(raw)
    h=re.sub(r'data:image/[^"\')]+','',h)
    h=re.sub(r'<(h2|h3|h4)[^>]*>',r'\n## ',h)
    h=re.sub(r'</(p|li|tr|h2|h3|h4)>','\n',h)
    h=re.sub(r'<li[^>]*>','• ',h)
    h=re.sub(r'<t[dh][^>]*>',' | ',h)
    t=html.unescape(re.sub(r'<[^>]+>','',h))
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    print("="*25,idx[n]["title"],"="*25)
    print(t.strip())
    print()
