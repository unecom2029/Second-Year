import json, re, sys, statistics
from images import data_uri, IMGS
SRC='/Users/jeeval/Documents/GitHub/Second-Year/OMK/Cardio/Week 14/notes/Quiz/index.html'
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
    D='/Users/jeeval/Documents/GitHub/Second-Year/OMK/Cardio/Week 14/notes/Quiz/'
    jobs={'phys':[('q_phys_v1','Cardiac Physiology Review — Quiz V1','Cardiac_Physiology_Quiz_V1.html'),
                  ('q_phys_v2','Cardiac Physiology Review — Quiz V2','Cardiac_Physiology_Quiz_V2.html')],
          'arr':[('q_arr_v0','ECG II Arrhythmias — Concept Quiz V0','ECG_II_Arrhythmias_Concept_Quiz_V0.html'),
                 ('q_arr_v1','ECG II Arrhythmias — Quiz V1','ECG_II_Arrhythmias_Quiz_V1.html'),
                 ('q_arr_v2','ECG II Arrhythmias — Image Quiz V2','ECG_II_Arrhythmias_Image_Quiz_V2.html')],
          'peds':[('q_peds_v1','Pediatric Cardiology — Quiz V1','Pediatric_Cardiology_Quiz_V1.html'),
                  ('q_peds_v2','Pediatric Cardiology — Image Quiz V2','Pediatric_Cardiology_Image_Quiz_V2.html')],
          'aa':[('q_aa_v1','Antiarrhythmic Pharmacology — Quiz V1','Antiarrhythmic_Pharmacology_Quiz_V1.html'),
                ('q_aa_v2','Antiarrhythmic Pharmacology — Quiz V2','Antiarrhythmic_Pharmacology_Quiz_V2.html')],
          'hf':[('q_hf_v1','Heart Failure Pharmacology — Quiz V1','Heart_Failure_Pharmacology_Quiz_V1.html'),
                ('q_hf_v2','Heart Failure Pharmacology — Quiz V2','Heart_Failure_Pharmacology_Quiz_V2.html')],
          'ihd':[('q_ihd_v1','Ischemic Heart Disease Pharmacology — Quiz V1','Ischemic_Heart_Disease_Pharmacology_Quiz_V1.html'),
                 ('q_ihd_v2','Ischemic Heart Disease Pharmacology — Quiz V2','Ischemic_Heart_Disease_Pharmacology_Quiz_V2.html')],
          'lp':[('q_lp_v1','Dyslipidemia Pharmacology — Quiz V1','Dyslipidemia_Pharmacology_Quiz_V1.html'),
                ('q_lp_v2','Dyslipidemia Pharmacology — Quiz V2','Dyslipidemia_Pharmacology_Quiz_V2.html')]}
    for v in sys.argv[1:]:
        if v.startswith('write'): continue
        job,_,only=v.partition(':')
        for mod,name,fn in jobs[job]:
            if only and mod!=only: continue
            Q=importlib.import_module(mod).Q; audit(mod,Q)
            print('  images:',sum(1 for q in Q if q.get('img')),'of',len(Q))
            if 'write' in sys.argv: write(Q,name,D+fn)
