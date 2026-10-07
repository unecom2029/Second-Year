import re, html, sys, os
from PIL import Image
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
NOTES='/Users/jeeval/Documents/GitHub/Second-Year/OMK/Cardio/Week 15/notes/'
T=open('ER_template.html',encoding='utf-8').read().split('\n')
W='Watkins — CAD case module'; S='Segal — HTN case'; H='Segal/Scully — HF case'; P='Segal — PAD case'
CFG={
'1':dict(out='Application_Session_1_Chest_Pain_HTN_Study_Notes.html',title='Application Session 1 — Chest Pain & Secondary HTN — Study Notes',
  emoji='%F0%9F%A9%BA',key='cardio-w15-app-session-1',body=['s1_body.html'],tail='s1_tail.html',asset='app-session-1',prefix='A1',
  footer=('Built from Application Session 1: <em>CAD case modules</em> (Matthew W. Watkins, MD; 46 slides, no recording) and <em>HTN Case</em> (Paul Segal, DO; 34 slides). '
   'The recording (<em>Application Session transcript 2</em>) begins at the end of the HTN case; its emphasis is in the "From the recording" boxes. Figures are labeled by deck and slide. '
   'Items tagged "Board add-on" come from UWorld/AMBOSS or current guidelines. Slide errors are flagged in red boxes. No UWorld images. Personal study notes; course material remains the copyright of its authors.'),
  figs={
  'ischemia-descriptors':('as1-ischemia-descriptors.jpg','Descriptors and the probability that chest pain is ischemic: pressure, squeezing, exertional → high; sharp, fleeting, positional, pleuritic → low',W,'4 · Gulati, Circulation 2021',True),
  'chest-pain-table':('as1-chest-pain-table.jpg','Chest-pain characteristics and their likely causes: nature, onset, location, severity, precipitating and relieving factors',W,'3 · 2021 Chest Pain Guideline',True),
  'fh-signs':('as1-fh-signs.jpg','Signs of familial hypercholesterolemia: tendon xanthoma and corneal arcus < 45 (highly specific); xanthelasma (low specificity)',W,'8',True),
  'sihd-testing':('as1-sihd-testing.jpg','Choosing a non-invasive test for suspected SIHD: ability to exercise, interpretable ECG and pre-test likelihood decide ETT vs stress imaging vs CCTA',W,'18 · Katz & Gavin, Ann Intern Med 2019',False),
  'omt-survival':('as1-omt-survival.jpg','All-cause mortality 5–10 years by number of OMT drug classes (antiplatelet, statin, ACEi/ARB, β-blocker): ~20% on 0–2 vs ~13% on 3–4',W,'21 · Kawashima, JACC 2021',True),
  'nstemi-ecg':('as1-nstemi-ecg.jpg','Her return ECG: down-sloping ST depression in the inferolateral leads (I, II, III, aVF, V3–V5) with ST elevation in V1',W,'25',False),
  'acs-pyramid':('as1-acs-pyramid.jpg','The chest-pain pyramid: asymptomatic → low → intermediate → high risk → ACS, with the testing strategy for each level',W,'28 · Gulati, Circulation 2021',True),
  'mi-classification':('as1-mi-classification.jpg','Trigger-based MI classification: primary (atherothrombosis, dissection), secondary (supply–demand), procedural',W,'29 · Lindahl, Nature Medicine 2023',True),
  'type1-type2-mi':('as1-type1-type2-mi.jpg','Type 1 vs type 2 MI: plaque rupture in younger men vs supply–demand mismatch in older women with comorbidities; very different rates of angiography and revascularization',W,'30 · McCarthy, JACC 2021',True),
  'coronary-flow-reserve':('as1-coronary-flow-reserve.jpg','Coronary flow reserve: maximal flow falls from ~50% stenosis while resting flow holds until ~80–90%',W,'31 · Gould',True),
  'nste-acs-invasive':('as1-nste-acs-invasive.jpg','Timing of invasive evaluation in NSTE-ACS: very high risk < 2 h, high risk < 24 h, intermediate risk < 72 h',W,'36 · ESC 2020',True),
  'vsr-echo':('as1-vsr-echo.jpg','Echocardiogram with color Doppler: flow across the interventricular septum after MI (ventricular septal rupture)',W,'44',True),
  'mechanical-complications':('as1-mechanical-complications.jpg','Mechanical complications of acute MI: papillary muscle infarction, ventricular septal rupture, LV free-wall rupture',W,'41',True),
  'bp-positioning':('as1-bp-positioning.jpg','Positioning errors and how far they push the reading: cuff over clothing 5–50, cuff too small 2–10, crossed legs 2–8, full bladder/talking/unsupported arm 10 mm Hg',S,'7',True),
  'bp-methods':('as1-bp-methods.jpg','Clinic vs home vs ambulatory BP: description, strengths (outcome association, white-coat and masked HTN detection) and weaknesses',S,'8 · Muntner, JACC 2019',True),
  'sodium-mechanism':('as1-sodium-mechanism.jpg','High sodium → oxidative stress and endothelial Na⁺ channel activation → endothelial dysfunction (↓ NO) and large-artery stiffening → ↑ SVR and SBP',S,'11',True),
  'aldosterone-principal-cell':('as1-aldosterone-principal-cell.jpg','Collecting-duct principal cell: aldosterone (and cortisol, unless inactivated by 11β-HSD2) activates the MR → ENaC, ROMK and Na⁺/K⁺-ATPase; spironolactone blocks the MR',S,'21 · Geetha, CCJM 2022',True),
  'aldosterone-tissues':('as1-aldosterone-tissues.jpg','Aldosterone acts on kidney, vessels, liver and fat via MR and GPER → hypertension and cardiometabolic syndrome',S,'22',True),
  'low-renin-algorithm':('as1-low-renin-algorithm.jpg','Low-renin hypertension: exclude interfering factors → aldosterone → elevated ARR = PA; normal ARR → Liddle, AME, CAH, Gordon, DOC-secreting tumor',S,'24 · Shah, Hypertension 2024',True),
  'pa-prevalence':('as1-pa-prevalence.jpg','Renin-independent aldosterone production rises on a continuum with BP severity, from normotension to resistant HTN; PA prevalence is high',S,'25 · Brown, Ann Intern Med 2020',True),
  'pa-management':('as1-pa-management.jpg','PA management: low renin + high aldosterone → surgical candidate? → adrenal CT + AVS → lateralized → adrenalectomy; otherwise MRA (spironolactone), then ENaC inhibitor',S,'28, 31',False),
  'aldosterone-escape':('as1-aldosterone-escape.jpg','Aldosterone escape: Na⁺ retention → plasma volume expansion → ↑ renal flow and peritubular pressure + atrial stretch (ANP) → natriuresis, so no edema',S,'29 · MyEndoConsult',True),
  'renin-independent-aldo':('as1-renin-independent-aldo.jpg','Renin-independent aldosteronism: ↑ distal Na⁺ delivery and reabsorption, volume expansion and BP; ↑ K⁺ and H⁺ excretion; cardiovascular and kidney disease',S,'31 · Endocrine Society',False)}),
'2':dict(out='Application_Session_2_Heart_Failure_PAD_Study_Notes.html',title='Application Session 2 — Heart Failure & PAD — Study Notes',
  emoji='%F0%9F%AB%81',key='cardio-w15-app-session-2',body=['s2_body.html'],tail='s2_tail.html',asset='app-session-2',prefix='A2',
  footer=('Built from Application Session 2: <em>Application Session – Heart Failure</em> (P. Segal, DO + K. Scully, PhD, with A. Qazi, DO; 40 slides) and <em>A Case of Atherosclerosis</em> (PAD; P. Segal, DO; 36 slides), '
   'with the full recording (<em>Application Session transcript 2</em>). Spoken emphasis is in the "From the recording" boxes. Figures are labeled by deck and slide. Items tagged "Board add-on" come from UWorld/AMBOSS or current guidelines. '
   'Slide or recording errors are flagged in red boxes. No UWorld images. Personal study notes; course material remains the copyright of its authors.'),
  figs={})}
def build(n,figs_extra=None):
    c=CFG[n]; figs=dict(c['figs']); figs.update(figs_extra or {})
    head='\n'.join(T[0:813]); toolcss='\n'.join(T[854:885]); tail='\n'.join(T[1473:])
    head=head.replace('<title>Exercise Rehabilitation & Lifestyle Prevention — Study Notes</title>','<title>'+html.escape(c['title'],quote=False)+'</title>').replace('%F0%9F%8F%83',c['emoji'])
    num=[0]; index=[]
    def fig(k):
        f,t,src,sl,sm=figs[k]; num[0]+=1
        w,h=Image.open(NOTES+'assets/'+c['asset']+'/'+f).size; index.append((num[0],f,t,src,sl))
        return ('<figure class="fig-card%s" id="fig-%s"><div class="fig-frame"><img class="slide-img" src="assets/%s/%s" alt="%s" width="%d" height="%d" loading="lazy" decoding="async"></div>'
          '<figcaption><span class="fig-num">Fig %s.%d</span><span class="fig-title">%s</span><span class="fig-src"><b>%s</b> · slide %s</span></figcaption></figure>')%(' sm' if sm else '',k,c['asset'],f,html.escape(t),w,h,c['prefix'],num[0],t,src,sl)
    body=''.join(open(p,encoding='utf-8').read() for p in c['body'])
    body=re.sub(r'\{\{F:([\w-]+)\}\}',lambda m:fig(m.group(1)),body)
    assert '{{' not in body, re.findall(r'\{\{[^}]*\}\}',body)[:3]
    tl=open(c['tail'],encoding='utf-8').read()
    nq=(body+tl).count('class="exam-q"')
    body=body.replace('@@NQ@@',str(nq)).replace('@@NF@@',str(num[0])).replace('@@TOOLCSS@@',toolcss)
    ids=re.findall(r'<div class="section" id="([^"]+)"',body+tl)
    t2=tail.replace('cardio-w15-exercise-rehab-',c['key']+'-')
    t2=re.sub(r"var SECTION_IDS=\[[^\]]*\];","var SECTION_IDS="+str(ids)+";",t2)
    old=re.search(r'<footer>\s*<div class="container">\s*<div>(.*?)</div>',t2,re.S).group(1)
    t2=t2.replace(old,c['footer'])
    assert 'Exercise' not in t2
    out=head+'\n'+body+'\n'+tl+'\n'+t2
    from strip_slides import strip_slides
    out=strip_slides(out)
    open(NOTES+c['out'],'w',encoding='utf-8').write(out)
    print('ok',c['out'],len(out),'exam-q',nq,'figs',num[0],'sections',len(ids))
    return index
if __name__=='__main__':
    for n in sys.argv[1:]:
        if n=='2':
            import s2figs; build(n,s2figs.FIGS)
        else: build(n)
