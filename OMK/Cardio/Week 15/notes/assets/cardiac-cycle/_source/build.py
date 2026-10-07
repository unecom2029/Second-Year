import re, html
from PIL import Image
NOTES='/Users/jeeval/Documents/GitHub/Second-Year/OMK/Cardio/Week 15/notes/'
import os
HERE=os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
T=open('ER_template.html',encoding='utf-8').read().split('\n')
head='\n'.join(T[0:813])
toolcss='\n'.join(T[854:885])
tail='\n'.join(T[1473:])
assert T[812].strip()=='' and 'progress-bar' in T[811], T[811]
assert T[854].startswith('<style>') and T[884].startswith('</style>')
assert 'lightbox' in T[1473]
head=head.replace('<title>Exercise Rehabilitation & Lifestyle Prevention — Study Notes</title>','<title>Cardiac Cycle & Valve Hemodynamics — Study Notes</title>')
head=head.replace('%F0%9F%8F%83','%F0%9F%AB%80')  # running person -> anatomical heart
assert 'Cardiac Cycle' in head and '%F0%9F%AB%80' in head
FIG={
 'wiggers':('cc-wiggers.jpg','Normal Wiggers diagram: aortic, atrial and ventricular pressure, ventricular volume, ECG and phonocardiogram, with the phases named across the top','11','Line graph of cardiac pressures, ventricular volume, ECG and heart sounds over two beats',False),
 'ms-schematic':('cc-ms-schematic.jpg','Normal vs mitral stenosis: LA 10 → 25 mm Hg, LV 120/10 → 115/6, turbulent flow through the narrowed valve','20','Two heart outlines comparing a normal mitral valve with a narrowed one, with chamber pressures',True),
 'ms-tracing':('cc-ms-tracing.jpg','Mitral stenosis: LA pressure stays above LV pressure through diastole (shaded diastolic gradient)','20','Pressure tracing with the LA curve above the LV curve during diastole',True),
 'as-schematic':('cc-as-schematic.jpg','Normal vs aortic stenosis: LV 120/10 → 200/25 with a thick wall, aorta 110/70, LA 25','22','Two heart outlines comparing a normal aortic valve with a narrowed one, with chamber pressures',True),
 'as-tracing':('cc-as-tracing.jpg','Aortic stenosis: LV systolic pressure far above aortic pressure (shaded systolic gradient)','22','Pressure tracing with the LV peak near 200 and the aortic peak near 115',True),
 'mr-schematic':('cc-mr-schematic.jpg','Normal vs mitral regurgitation: systolic jet back into the LA, LA 25, LV 110/25','24','Two heart outlines comparing normal mitral closure with a leaking valve',True),
 'mr-tracing':('cc-mr-tracing.jpg','Mitral regurgitation: a tall v wave on the LA curve, rising toward LV pressure late in systole','24','Pressure tracing with a labelled tall v wave on the LA curve',True),
 'ar-schematic':('cc-ar-schematic.jpg','Normal vs aortic regurgitation: diastolic jet into the LV, aorta 160/60, LV 160/20, LA 20','26','Two heart outlines comparing a normal aortic valve with a leaking one',True),
 'ar-tracing':('cc-ar-tracing.jpg','Aortic regurgitation: ↑ systolic and ↓ diastolic aortic pressure (wide pulse pressure), LV and aortic peaks superimposed','26','Pressure tracing labelled with raised systolic and lowered diastolic aortic pressure',True)}
n=[0]; index=[]
def fig(k):
    f,t,s,alt,sm=FIG[k]; n[0]+=1
    w,h=Image.open(NOTES+'assets/cardiac-cycle/'+f).size
    index.append((n[0],f,t,s,w,h))
    return ('<figure class="fig-card%s" id="fig-cc-%s"><div class="fig-frame"><img class="slide-img" src="assets/cardiac-cycle/%s" alt="%s" width="%d" height="%d" loading="lazy" decoding="async"></div>'
     '<figcaption><span class="fig-num">Fig C%d</span><span class="fig-title">%s</span><span class="fig-src"><b>Qazi — Cardiac Cycle lecture</b> · slide %s</span></figcaption></figure>')%(' sm' if sm else '',k,f,html.escape(alt),w,h,n[0],t,s)
def thumb(k):
    f,t,s,alt,sm=FIG[k]
    return '<img class="slide-img thumb" src="assets/cardiac-cycle/%s" alt="%s" loading="lazy" decoding="async">'%(f,html.escape(alt))
body=''.join(open(p,encoding='utf-8').read() for p in ['body1.html','body2.html','body3.html','body4.html'])
body=re.sub(r'\{\{F:([\w-]+)\}\}',lambda m:fig(m.group(1)),body)
body=re.sub(r'\{\{ROW:([\w-]+),([\w-]+)\}\}',lambda m:'<div class="fig-row">'+fig(m.group(1))+fig(m.group(2))+'</div>',body)
body=re.sub(r'\{\{THUMB:([\w-]+)\}\}',lambda m:thumb(m.group(1)),body)
assert '{{' not in body
nq=body.count('class="exam-q"')
body=body.replace('@@NQ@@',str(nq))
# insert tool css right after hero (as template does)
i=body.index('<!-- ==================== ORIENTATION')
body=body[:i]+toolcss+'\n\n'+body[i:]
ids=re.findall(r'<div class="section" id="([^"]+)"',body)
tail=tail.replace("cardio-w15-exercise-rehab-","cardio-w15-cardiac-cycle-")
tail=re.sub(r"var SECTION_IDS=\[[^\]]*\];","var SECTION_IDS="+str(ids).replace("'","'")+";",tail)
foot_old=re.search(r'<footer>\s*<div class="container">\s*<div>(.*?)</div>',tail,re.S).group(1)
foot_new=('Built from <em>The Wigger’s Diagram and the Cardiac Cycle</em> (Amina Qazi, DO, FACC, UNE COM; 27 slides) and the two-part lecture recording '
 '(cardiac cycle → mitral and aortic stenosis; mitral and aortic regurgitation → cardiac rehab). Figures are from the lecture deck and labeled by slide. '
 'Items tagged "Board add-on" come from the UWorld and AMBOSS library articles (Valve disorders; Cardiovascular hemodynamics; Cardiac physiology; Cardiovascular examination). '
 'Recording-vs-textbook discrepancies are flagged in red boxes. No UWorld images. Personal study notes; course material remains the copyright of its authors.')
tail=tail.replace(foot_old,foot_new)
assert 'exercise-rehab' not in tail and 'Exercise' not in tail, [l for l in tail.split('\n') if 'xercise' in l][:3]
out=head+'\n'+body+'\n'+open('body5.html',encoding='utf-8').read()+'\n'+open('hy.html',encoding='utf-8').read()+'\n'+tail
from strip_slides import strip_slides
out=strip_slides(out)
open(NOTES+'Cardiac_Cycle_Valve_Hemodynamics_Study_Notes.html','w',encoding='utf-8').write(out)
print('ok',len(out),'exam-q',nq,'sections',ids)
for r in index: print(r)
