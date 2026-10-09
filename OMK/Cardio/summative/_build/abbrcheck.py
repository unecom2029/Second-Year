import re, html, glob, sys
D = {
'QRS':'the ventricular depolarisation complex on the ECG','PR':'PR interval (atrial depolarisation to ventricular depolarisation)','ST':'ST segment (between the QRS and the T wave)','QT':'QT interval (ventricular depolarisation plus repolarisation)',
'SERCA':'sarcoplasmic reticulum calcium ATPase (the pump that refills the store)','RyR2':'ryanodine receptor 2 (the calcium-release channel)','METs':'metabolic equivalents',
'CV':'cardiovascular','DAG':'diacylglycerol','IP3':'inositol trisphosphate','RS':'RS complex (an R wave followed by an S wave)',
'AMP':'adenosine monophosphate','ATPase':'adenosine triphosphatase','ACE':'angiotensin-converting enzyme','INOCA':'ischemia with no obstructive coronary arteries',
'P2Y12':'the platelet ADP receptor blocked by clopidogrel, prasugrel and ticagrelor','V4R':'right-sided chest lead V4','ADP':'adenosine diphosphate','CNS':'central nervous system',
'COPD':'chronic obstructive pulmonary disease','COX':'cyclooxygenase','BMI':'body mass index','ED':'emergency department','GLP':'GLP-1, glucagon-like peptide-1',
'LVH':'left ventricular hypertrophy','SGLT2':'sodium–glucose cotransporter 2','BNP':'B-type natriuretic peptide','NT':'NT-proBNP, N-terminal pro-B-type natriuretic peptide',
'DASH':'Dietary Approaches to Stop Hypertension','PV':'pressure–volume','SR':'sarcoplasmic reticulum','AED':'automated external defibrillator','LVAD':'left ventricular assist device',
'HFrEF':'heart failure with reduced ejection fraction','GI':'gastrointestinal','GU':'genitourinary','ICD':'implantable cardioverter-defibrillator','ID':'infectious disease',
'IgG':'immunoglobulin G','CYP450':'cytochrome P450','CYP':'cytochrome P450 liver enzymes','CBC':'complete blood count','COVID':'COVID-19, coronavirus disease 2019',
'SARS':'SARS-CoV-2, the virus that causes COVID-19','IDU':'injection drug use','JVP':'jugular venous pressure','NSAID':'non-steroidal anti-inflammatory drug',
'PCR':'polymerase chain reaction','VSD':'ventricular septal defect','AVR':'aortic valve replacement','DOAC':'direct oral anticoagulant','PCI':'percutaneous coronary intervention',
'AR':'aortic regurgitation','MVP':'mitral valve prolapse','TR':'tricuspid regurgitation','WPW':'Wolff–Parkinson–White','TAPVR':'total anomalous pulmonary venous return',
'CCB':'calcium-channel blocker','HSD2':'11β-HSD2, 11β-hydroxysteroid dehydrogenase type 2','ICU':'intensive care unit','MAO':'monoamine oxidase','MR':'magnetic resonance (in "MR angiography")',
'ROMK':'renal outer medullary potassium channel','SNRI':'serotonin–norepinephrine reuptake inhibitor','TSH':'thyroid-stimulating hormone','VEGF':'vascular endothelial growth factor',
'STOP':'STOP-BANG, a sleep-apnea screening questionnaire','ARNI':'angiotensin receptor–neprilysin inhibitor','AT1':'angiotensin II type 1 receptor','HIV':'human immunodeficiency virus',
'STEMI':'ST-elevation myocardial infarction','VLDL':'very-low-density lipoprotein','MMP':'matrix metalloproteinase','AAA':'abdominal aortic aneurysm','ARB':'angiotensin receptor blocker',
'LDL':'low-density lipoprotein','HDL':'high-density lipoprotein','PCSK9':'proprotein convertase subtilisin/kexin type 9','MRA':'mineralocorticoid receptor antagonist',
'ECG':'electrocardiogram','EKG':'electrocardiogram','BP':'blood pressure','HR':'heart rate','MI':'myocardial infarction','HF':'heart failure','LV':'left ventricle','RV':'right ventricle',
'LA':'left atrium','RA':'right atrium','AV':'atrioventricular','SA':'sinoatrial','EF':'ejection fraction','CT':'computed tomography','MRI':'magnetic resonance imaging',
'IV':'intravenous','TIA':'transient ischemic attack','AF':'atrial fibrillation','SVT':'supraventricular tachycardia','VT':'ventricular tachycardia','VF':'ventricular fibrillation',
'ATP':'adenosine triphosphate','NO':'nitric oxide','TNF':'tumor necrosis factor','IL':'interleukin','PET':'positron emission tomography','CO':'cardiac output','DNA':'deoxyribonucleic acid',
}
# tokens whose expansion is wrong in that section's context
SKIP={('s5-pharm-basics','NO')}|{(n,'IV') for n in ['s10-antiarrhythmics','s4-exercise','s33-ctd','s9-afib','s30-lipids']}
OVR={('s28-htn','AV'):'arteriovenous',('s35-pad','AV'):'arteriovenous'}
MR_SECTIONS={'s28-htn'}
def txt(x): return html.unescape(re.sub(r'<[^>]+>',' ',x))
dry = '--dry' in sys.argv
for f in sorted(glob.glob('s*.html')):
    name=f[:-5]; s=open(f).read()
    m=re.search(r'(<div class="abbr-strip">)(.*?)(\s*</div>)',s,re.S)
    if not m: print('NO STRIP',name); continue
    strip=txt(m.group(2))
    body=txt(s[:m.start()]+s[m.end():])
    have=set(re.findall(r'[A-Za-z0-9β-]+',strip))
    add=[]
    for k,v in D.items():
        if (name,k) in SKIP: continue
        if not re.search(r'(?<![A-Za-z0-9])'+re.escape(k)+r's?(?![A-Za-z0-9])',body): continue
        if k=='NO' and not re.search(r'\bNO\b(?! [a-z])',body): continue
        # present in strip? check the token or plural or a hyphenated form
        if re.search(r'(?<![A-Za-z0-9])'+re.escape(k)+r's?(?![A-Za-z0-9])',strip): continue
        add.append(k)
    if (name,'MR') in SKIP and 'MR' in add: pass
    if add:
        print(name, add)
        if not dry:
            ins=''.join(f' &middot; <strong>{k}</strong> {html.escape(OVR.get((name,k),D[k]),quote=False)}' for k in add)
            g2=m.group(2).rstrip()
            s=s[:m.start()]+m.group(1)+g2+ins+m.group(3)+s[m.end():]
            open(f,'w').write(s)
