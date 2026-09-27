import json, collections
F="/Users/jeeval/Board Study/figures/Text/UWorld - Complete All 26 Collections - 1241 Articles.html"
buf=open(F,encoding="utf-8",errors="ignore").read(900000)
i=buf.index('id="library-index">')+len('id="library-index">')
j=buf.index('</script>',i)
idx=json.loads(buf[i:j])
json.dump(idx,open("uworld_index.json","w"))
print("articles:",len(idx))
c=collections.Counter(a["folderPath"][0] for a in idx)
for k,v in c.most_common(): print(f"  {v:>4}  {k}")
