import base64, io, os
from PIL import Image, ImageDraw
P='/Users/jeeval/Documents/GitHub/Second-Year/OMK/Cardio/Week 14/notes/assets/physiology/'
E='/Users/jeeval/Documents/GitHub/Second-Year/OMK/Cardio/Week 14/notes/assets/ekg-2/'
N='/Users/jeeval/Documents/GitHub/Second-Year/OMK/Cardio/Week 14/notes/assets/'
AM='/Users/jeeval/Board Study/figures/amboss/'
AL='/Users/jeeval/Board Study/figures/Text/AMBOSS Library Data/assets/'
RB='/Users/jeeval/Board Study/figures/Robbins/'
L=os.path.join(os.path.dirname(os.path.abspath(__file__)),'ecglib')+'/'
_GRID=None
def _ongrid(p):
    global _GRID
    if _GRID is None: _GRID=Image.open(L+'grid.gif').convert('RGBA')
    im=Image.open(p).convert('RGBA'); bg=Image.new('RGBA',im.size)
    for x in range(0,im.width,_GRID.width):
        for y in range(0,im.height,_GRID.height): bg.paste(_GRID,(x,y))
    bg.alpha_composite(im); return bg.convert('RGB')
# key: (path, crop (l,t,r,b fractions) or None, credit[, list of white-out boxes as fractions])
M='/private/tmp/claude-501/-Users-jeeval/0c82a8bc-abbf-4cdc-8d74-a0bc9651eb94/scratchpad/vasc/deck/ppt/media/'
V=N.replace('Week 14','Week 15')+'vasc-surg/'
IMGS={
 # lecture figures (repo copies in notes/assets/vasc-surg)
 'Vbluetoe':(V+'vs-blue-toe.jpg',None,'Vascular Disease lecture · slide 12'),
 'Vrubor':(V+'vs-dependent-rubor.jpg',None,'Vascular Disease lecture · slide 21'),
 'Vlathromb':(V+'vs-la-thrombus.jpg',None,'Vascular Disease lecture · slide 27',[(0.25,0.66,0.62,0.79,'black'),(0.30,0.12,0.75,0.6,None)][:1]),
 'Vfasc':(V+'vs-fasciotomy.jpg',None,'Vascular Disease lecture · slide 32'),
 'Vctadis':(V+'vs-cta-dissection.jpg',None,'Vascular Disease lecture · slide 44'),
 'Vaaact':(V+'vs-aaa-ct.jpg',None,'Vascular Disease lecture · slide 50'),
 'Vischcol':(V+'vs-ischemic-colitis.jpg',None,'Vascular Disease lecture · slide 53'),
 'Vgraftinf':(V+'vs-graft-infection.jpg',None,'Vascular Disease lecture · slide 54'),
 'Vsplenic':(V+'vs-splenic-aneurysm.jpg',None,'Vascular Disease lecture · slide 55'),
 'Vpopl':(V+'vs-popliteal-aneurysm.jpg',(0,0,0.5,1),'Vascular Disease lecture · slide 56',[(0,0.92,0.06,1,'black')]),
 'Vsma':(V+'vs-sma-embolus.jpg',None,'Vascular Disease lecture · slide 59',[(0.47,0.20,0.73,0.33,'black'),(0.48,0.66,0.62,0.77,'black')]),
 'Vdeadbowel':(V+'vs-dead-bowel.jpg',None,'Vascular Disease lecture · slide 61'),
 'Vrasmra':(V+'vs-renal-artery-stenosis.jpg',None,'Vascular Disease lecture · slide 67'),
 'Vraynaud':(V+'vs-raynaud.jpg',None,'Vascular Disease lecture · slide 70'),
 'Vgca':(V+'vs-temporal-arteritis.jpg',None,'Vascular Disease lecture · slide 72'),
 'Vtaka':(V+'vs-takayasu.jpg',None,'Vascular Disease lecture · slide 73'),
 'Vbuerger':(V+'vs-buerger.jpg',None,'Vascular Disease lecture · slide 74'),
 'Vdvtus':(V+'vs-dvt-duplex.jpg',None,'Vascular Disease lecture · slide 79'),
 'Vphleg':(V+'vs-phlegmasia.jpg',None,'Vascular Disease lecture · slide 86'),
 'Vpts':(V+'vs-post-thrombotic.jpg',(0,0.62,1,1),'Vascular Disease lecture · slide 87',[(0,0.6,0.08,0.68)]),
 'Vcfa':(V+'vs-cfa-occlusion.jpg',None,'Vascular Disease lecture · slide 22',[(0,0.25,0.62,0.42,(150,150,150))]),
 'Vaiod':(V+'vs-aortoiliac-specimen.jpg',None,'Vascular Disease lecture · slide 11'),
 # AMBOSS
 'Abluetoe':(AM+'Blue toe syndrome.png',None,'AMBOSS'),
 'Ahollen':(AM+'Hollenhorst plaque causing branch retinal artery occlusion (BRAO).png',None,'AMBOSS'),
 'Acarotid':(AM+'Carotid artery stenosis.png',None,'AMBOSS'),
 'Aruptaaa':(AM+'Ruptured abdominal aortic aneurysm (AAA).png',None,'AMBOSS'),
 'Agca':(AM+'Giant cell arteritis.png',None,'AMBOSS'),
 'Araynaud':(AM+'Raynaud phenomenon (ischemic phase).png',None,'AMBOSS'),
 'Advt':(AM+'Deep vein thrombosis (DVT).png',None,'AMBOSS'),
 'Acvi':(AM+'Chronic venous insufficiency.png',None,'AMBOSS'),
 'Avenulcer':(AM+'Venous ulcer in chronic venous insufficiency.png',None,'AMBOSS'),
 'Apseudo':(AM+'Pseudoaneurysm of the femoral artery.png',None,'AMBOSS'),
 'Alivedo':(AM+'Livedo reticularis.png',None,'AMBOSS'),
 'Atoegang':(AM+'Toe gangrene.png',None,'AMBOSS'),
 'Adiabfoot':(AM+'Diabetic foot ulcer.png',None,'AMBOSS'),
 # Women's CV health (repo copies in notes/assets/women-cv)
 'Wmenarche':(V.replace('vasc-surg','women-cv')+'wh-menarche.jpg',(0.5,0.17,1,0.93),'Women lecture · slide 12 (Canoy, Circulation 2015)'),
 'Wprev':(V.replace('vasc-surg','women-cv')+'wh-prevalence.jpg',None,'Women lecture · slide 8 (AHA statistics)'),
 'Wptd':(V.replace('vasc-surg','women-cv')+'wh-preterm.jpg',(0.2,0.14,0.68,1),'Women lecture · slide 19 (Kessous 2013)'),
 # Exercise rehab
 'Esv':(V.replace('vasc-surg','exercise-rehab')+'er-exercise-response.jpg',(0.5,0,1,0.5),'Exercise Rehab lecture · slide 8',[(0.5,0,0.6,0.5)]),
 'Ebp':(V.replace('vasc-surg','exercise-rehab')+'er-exercise-response.jpg',(0,0.5,0.5,1),'Exercise Rehab lecture · slide 10',[(0,0.5,0.06,0.62)]),
 'Efit':(V.replace('vasc-surg','exercise-rehab')+'er-fitness-change.jpg',None,'Exercise Rehab lecture · slide 14 (Blair, JAMA 1995)'),
 'Epredimed':(V.replace('vasc-surg','exercise-rehab')+'er-predimed.jpg',None,'Exercise Rehab lecture · slide 38 (Estruch, NEJM 2013)'),
 'Edash':(V.replace('vasc-surg','exercise-rehab')+'er-dash-sodium.jpg',None,'Exercise Rehab lecture · slide 41 (NEJM 2001)',[(0,0.93,0.06,1)]),
 # Cardiac cycle & valve hemodynamics (repo copies in notes/assets/cardiac-cycle); lesion titles and answer labels masked
 'Cms':(V.replace('vasc-surg','cardiac-cycle')+'cc-ms-tracing.jpg',None,'Cardiac Cycle lecture · slide 20',[(0.44,0.10,0.73,0.28,(250,247,238))]),
 'Cas':(V.replace('vasc-surg','cardiac-cycle')+'cc-as-tracing.jpg',None,'Cardiac Cycle lecture · slide 22',[(0.46,0.168,0.76,0.29,(240,236,233))]),
 'Cmr':(V.replace('vasc-surg','cardiac-cycle')+'cc-mr-tracing.jpg',None,'Cardiac Cycle lecture · slide 24',[(0.31,0.192,0.84,0.275,(238,234,231)),(0.385,0.525,0.525,0.635,(238,234,231))]),
 'Car':(V.replace('vasc-surg','cardiac-cycle')+'cc-ar-tracing.jpg',None,'Cardiac Cycle lecture · slide 26',[(0.30,0.20,0.88,0.275,(245,242,235)),(0.555,0.295,0.71,0.405,(245,242,235)),(0.42,0.595,0.53,0.665,(245,242,235)),(0.715,0.63,0.865,0.735,(245,242,235))]),
 'Casx':(V.replace('vasc-surg','cardiac-cycle')+'cc-as-schematic.jpg',(0,0,1,0.86),'Cardiac Cycle lecture · slide 22'),
 'Cph':(V.replace('vasc-surg','cardiac-cycle')+'cc-phase2-ivc.jpg',(0.33,0.14,1,0.97),'Cardiac Cycle lecture · slide 13'),
 # Application Session 1 (repo copies in notes/assets/app-session-1) + clean AMBOSS figures
 'A1xanth':(V.replace('vasc-surg','app-session-1')+'as1-fh-signs.jpg',(0.03,0.45,0.34,0.79),'Application Session 1 · Watkins CAD case'),
 'A1arcus':(V.replace('vasc-surg','app-session-1')+'as1-fh-signs.jpg',(0.685,0.45,1.0,0.79),'Application Session 1 · Watkins CAD case'),
 'A1ecg':(V.replace('vasc-surg','app-session-1')+'as1-nstemi-ecg.jpg',(0.12,0.0,0.97,0.88),'Application Session 1 · Watkins CAD case'),
 'A1vsr':(V.replace('vasc-surg','app-session-1')+'as1-vsr-echo.jpg',None,'Application Session 1 · Watkins CAD case',[(0.08,0.02,0.72,0.14,'black')]),
 'Aretino':(AM+'Grade IV hypertensive retinopathy.png',None,'AMBOSS'),
 'Ahypok':(AM+'ECG features of hypokalemia.png',None,'AMBOSS'),
 'Alvh':(AM+'ECG in left ventricular hypertrophy.png',None,'AMBOSS'),
 'Ainfstemi':(AM+'Acute inferior STEMI.png',None,'AMBOSS'),
 # Application Session 2 (repo copies in notes/assets/app-session-2) + clean AMBOSS figures
 'A2ecg':(V.replace('vasc-surg','app-session-2')+'as2-hfpef-ecg.jpg',None,'Application Session 2 · HF case'),
 'A2psax':(V.replace('vasc-surg','app-session-2')+'as2-psax-lvh.jpg',None,'Application Session 2 · HF case'),
 'A2cxr':(V.replace('vasc-surg','app-session-2')+'as2-cxr-edema.jpg',None,'Application Session 2 · HF case'),
 'A2rubor':(V.replace('vasc-surg','app-session-2')+'as2-dependent-rubor.jpg',None,'Application Session 2 · PAD case',[(0,0.015,0.085,0.095,(86,152,205))]),
 'A2leriche':(V.replace('vasc-surg','app-session-2')+'as2-leriche-ct.jpg',(0,0,1,0.755),'Application Session 2 · PAD case'),
 'Aedema':(AM+'Pitting edema of lower leg.png',None,'AMBOSS'),
 'Acpe':(AM+'Cardiogenic pulmonary edema.png',None,'AMBOSS',[(0,0,0.2,0.08,'black')]),
 'Adcm':(AM+'Dilated cardiomyopathy.png',None,'AMBOSS'),
 'Agangrene':(AM+'Toe gangrene.png',None,'AMBOSS'),
}
# small sources are upscaled so they don't show as thumbnails
UPSCALE={'A1xanth':760,'A1arcus':760}
def load(key, maxw=1100):
    e=IMGS[key]; p,crop=e[0],e[1]; masks=e[3] if len(e)>3 else []
    im=_ongrid(p) if p.endswith('.gif') else Image.open(p).convert('RGB')
    if masks:
        d=ImageDraw.Draw(im); w,h=im.size
        for m in masks:
            l,t,r,b=m[:4]; d.rectangle((int(l*w),int(t*h),int(r*w),int(b*h)),fill=(m[4] if len(m)>4 else 'white'))
    if crop:
        w,h=im.size; l,t,r,b=crop
        im=im.crop((int(l*w),int(t*h),int(r*w),int(b*h)))
    up=UPSCALE.get(key)
    if up and im.width<up:
        im=im.resize((up,int(im.height*up/im.width)),Image.LANCZOS)
    if im.width>maxw:
        im=im.resize((maxw,int(im.height*maxw/im.width)),Image.LANCZOS)
    return im
def data_uri(key):
    im=load(key); buf=io.BytesIO(); im.save(buf,'JPEG',quality=85,optimize=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(buf.getvalue()).decode()
