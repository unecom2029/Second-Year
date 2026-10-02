import json, re, sys, statistics
from images import data_uri, IMGS
import q_cardiac, q_endo
SRC='/Users/jeeval/Documents/GitHub/Second-Year/OMK/Cardio/Week 13/Notes/Quiz/index.html'
LET='ABCDEFGH'
def fig(key,cap):
    credit=IMGS[key][2]
    return ('<figure class="qfig" style="margin:16px 0;text-align:center">'
            f'<img src="{data_uri(key)}" alt="Figure 1" style="display:block;margin:0 auto;max-width:100%;max-height:460px;height:auto;border-radius:8px;border:1px solid rgba(0,0,0,.14);cursor:zoom-in" onclick="window.open(this.src)">'
            f'<figcaption class="qfig-cap" style="font-size:12.5px;margin-top:6px;opacity:.8">Figure 1 · {cap} · <i>{credit}</i></figcaption></figure>')
def to_json(Q):
    out=[]
    for q in Q:
        stem=q['stem'].replace('{FIG}',fig(q['img'],q['cap']) if q.get('img') else '<br><br>')
        assert set(q['wrong'])==set(range(len(q['choices'])))-{q['key']}, q['stem'][:40]
        order=list(range(len(q['choices'])))
        if not all(c[:1].isdigit() for c in q['choices']):
            order=sorted(order,key=lambda i:q['choices'][i].lower())
        ch=[f'{LET[n]}. {q["choices"][i]}' for n,i in enumerate(order)]
        key=order.index(q['key'])
        wrong={str(order.index(i)):v for i,v in q['wrong'].items()}
        out.append(dict(stem=stem,choices=ch,correct=key,explanation=q['exp'],
            wrongExplanations=wrong,eli5=q['eli5']))
    return out
def audit(name,Q):
    longest=shortest=0; ranks=[]; n=0
    for q in Q:
        L=[len(c) for c in q['choices']]
        if all(len(c.split())<=4 for c in q['choices']): continue  # single-term lists
        n+=1; k=q['key']
        if L[k]==max(L): longest+=1
        if L[k]==min(L): shortest+=1
        ranks.append(sorted(L,reverse=True).index(L[k])+1)
    keys=''.join(LET[q['key']] for q in Q)
    print(f'{name}: phrase-style items={n}; key longest={longest}, shortest={shortest}; chance≈{n/5:.1f} each; key rank (1=longest) {ranks}; keys {keys}')
def write(Q,name,out):
    qs=to_json(Q)
    html=open(SRC,encoding='utf-8').read()
    enc=lambda v: json.dumps(v,ensure_ascii=False).replace('</script','<\\/script').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
    html=re.sub(r'(<div class="view) active(" id="viewSetup">)',r'\1\2',html,count=1)
    html=re.sub(r'<title>[^<]*</title>',lambda m:f'<title>QUIZ: {name}</title>',html,count=1)
    html=re.sub(r'^var PRELOADED_QUIZ_NAME=[^\r\n]*;',lambda m:'var PRELOADED_QUIZ_NAME='+enc(name)+';',html,count=1,flags=re.M)
    html=re.sub(r'^var PRELOADED_QUESTIONS_JSON=[^\r\n]*;',lambda m:'var PRELOADED_QUESTIONS_JSON='+enc(json.dumps(qs,ensure_ascii=False))+';',html,count=1,flags=re.M)
    html=re.sub(r'^var PRELOADED_UI_MODE=[^\r\n]*;',lambda m:'var PRELOADED_UI_MODE='+enc('nbme')+';',html,count=1,flags=re.M)
    open(out,'w',encoding='utf-8').write(html)
    print('wrote',out,round(len(html)/1e6,2),'MB')
if __name__=='__main__':
    import importlib
    D='/Users/jeeval/Documents/GitHub/Second-Year/OMK/Cardio/Week 13/Notes/Quiz/'
    jobs={'v2':[('q_cardiac','Cardiac Pathology — Image Quiz V2','Cardiac_Pathology_Image_Quiz_V2.html'),
                ('q_endo','Endocarditis, Myocarditis & Pericarditis — Image Quiz V2','Endocarditis_Myocarditis_Pericarditis_Image_Quiz_V2.html')],
          'v1':[('q1_cardiac','Cardiac Pathology — Quiz V1','Cardiac_Pathology_Quiz_V1.html'),
                ('q1_endo','Endocarditis, Myocarditis & Pericarditis — Quiz V1','Endocarditis_Myocarditis_Pericarditis_Quiz_V1.html')],
          'ecg':[('q_ecg_v1','ECG Basics — Quiz V1','ECG_Basics_Quiz_V1.html'),
                 ('q_ecg_v2','ECG Basics — Image Quiz V2','ECG_Basics_Image_Quiz_V2.html')],
          'pharm':[('q_htn_v1','Hypertension Pharmacology — Quiz V1','Hypertension_Pharmacology_Quiz_V1.html'),
                   ('q_htn_v2','Hypertension Pharmacology — Quiz V2','Hypertension_Pharmacology_Quiz_V2.html'),
                   ('q_bsr_v1','CV Pharm Basic Sciences Review — Quiz V1','CV_Pharm_Basic_Sciences_Quiz_V1.html'),
                   ('q_bsr_v2','CV Pharm Basic Sciences Review — Quiz V2','CV_Pharm_Basic_Sciences_Quiz_V2.html')],
          'ecg0':[('q_ecg_v0','ECG Basics — Concept Quiz V0','ECG_Basics_Concept_Quiz_V0.html')]}
    for v in sys.argv[1:]:
        if v.startswith('write'): continue
        for mod,name,fn in jobs[v]:
            Q=importlib.import_module(mod).Q; audit(mod,Q)
            print('  images:',sum(1 for q in Q if q.get('img')),'of',len(Q))
            if 'write' in sys.argv: write(Q,name,D+fn)
