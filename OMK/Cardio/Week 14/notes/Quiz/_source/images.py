import base64, io, os
from PIL import Image, ImageDraw
P='/Users/jeeval/Documents/GitHub/Second-Year/OMK/Cardio/Week 14/notes/assets/physiology/'
U='/Users/jeeval/Board Study/figures/Uworld images/COMLEX 1 (Step1 + OMT1) - Cardiovascular System/'
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
IMGS={
 'sarcEM':(P+'p-sarcomere-em.jpg',None,'Morganelli lecture · slide 3'),
 'pvloop':(P+'p-pvloop.jpg',None,'Morganelli lecture · slide 19'),
 'guytonHF':(P+'p-guyton-hf.jpg',(0,0,1,0.93),'Koeppen & Stanton, Berne and Levy Physiology (Morganelli lecture · slide 39)'),
 'pvAR':(P+'p-a-pv-ar.jpg',None,'AMBOSS'),
 'pvAS':(P+'p-a-pv-as.jpg',None,'AMBOSS',[(0.66,0.28,0.98,0.47)]),
 'pvMR':(P+'p-a-pv-mr.jpg',None,'AMBOSS',[(0.55,0.2,0.98,0.42)]),
 'Uex':(U+'140_exercise_left_ventricular_pressure_volume_loop.jpg',None,'UWorld'),
 'Uino':(U+'141_exercise_pressure_volume_loop_option_b.png',None,'UWorld'),
 'Uafter':(U+'142_exercise_pressure_volume_loop_option_c.jpg',None,'UWorld'),
 'Upreup':(U+'143_exercise_pressure_volume_loop_option_d.png',None,'UWorld'),
 'Upredown':(U+'144_exercise_pressure_volume_loop_option_e.jpg',None,'UWorld'),
 'Uavf':(U+'169_arteriovenous_fistula_pressure_volume_loop.jpg',None,'UWorld'),
 'Unitro':(U+'171_nitroprusside_pressure_volume_loop_correct.png',None,'UWorld'),
 # ECG II arrhythmias
 'Rnormal':(E+'r-normal-pregnant.png',None,'EKG II lecture · slide 8'),
 'Rartifact':(E+'r-artifact.jpg',None,'EKG II lecture · slide 11'),
 'Rsvt':(E+'r-case-svt.jpg',None,'EKG II lecture · slide 23'),
 'Raf':(E+'r-case-af.jpg',None,'EKG II lecture · slide 31'),
 'Rflutter':(E+'r-case-flutter.jpg',(0,0.1,1,1),'EKG II lecture · slide 42'),
 'Rfl1to1':(E+'r-case-flutter-1to1.png',None,'EKG II lecture · slide 78'),
 'Rvtcap':(E+'r-case-vt-capture.png',None,'EKG II lecture · slide 68'),
 'Rvtcad':(E+'r-case-vt-cad.png',None,'EKG II lecture · slide 70'),
 'Rnegconc':(E+'r-neg-concordance.png',None,'EKG II lecture · slide 57'),
 'Rwpwaf':(E+'r-case-wpw-af.jpg',(0,0.17,1,0.93),'EKG II lecture · slide 83'),
 'Rwpwafter':(E+'r-a-wpw-after.jpg',None,'AMBOSS'),
 'Rtorsades':(E+'r-case-torsades.jpg',None,'EKG II lecture · slide 93'),
 'Rlqt':(E+'r-case-lqt.jpg',None,'EKG II lecture · slide 94'),
 'Rbrugada':(E+'r-a-brugada.jpg',None,'AMBOSS'),
 'Rperi':(E+'r-case-pericarditis.jpg',None,'EKG II lecture · slide 99'),
 'Ravnrt':(E+'r-a-avnrt-ecg.jpg',None,'AMBOSS'),
 'Radenofl':(E+'r-adenosine-flutter.jpg',None,'EKG II lecture · slide 43'),
 'Rafrvr':(E+'r-a-af-rvr.jpg',None,'AMBOSS'),
 'Radeno':(E+'r-adenosine-strip.jpg',None,'EKG II lecture · slide 28'),
 'Rposconc':(E+'r-pos-concordance.jpg',None,'EKG II lecture · slide 59'),
 'Raflutter':(E+'r-a-flutter.jpg',None,'AMBOSS'),
 'Rvtmono':(E+'r-a-vt-mono.jpg',None,'AMBOSS'),
 'Lwpwaf':(L+'img_wpwaf2s.gif',None,'ecglibrary.com'),
 'Lvtavd':(L+'img_vtavd2.gif',(0,0.27,1,1),'ecglibrary.com'),
 'Laflut':(L+'img_aflut.gif',None,'ecglibrary.com'),
 'Ldig':(L+'img_dig.gif',None,'ecglibrary.com'),
 'Ltdp':(L+'img_tdp.gif',None,'ecglibrary.com'),
 'Lafrvr':(L+'img_af_fast2.gif',None,'ecglibrary.com'),
 # ---- Pediatric cardiology (lecture images from ../../assets/peds-cardio/) ----
 'Pkdface':(N+'peds-cardio/pc-kd-face.jpg',(0,0,1,0.83),'Pediatric Cardiology lecture · slide 130'),
 'Pkddesq':(N+'peds-cardio/pc-kd-desquamation.jpg',None,'Pediatric Cardiology lecture · slide 133'),
 'Pboot':(N+'peds-cardio/pc-boot.jpg',None,'Pediatric Cardiology lecture · slide 72'),
 'Pcyan':(N+'peds-cardio/pc-circumoral.jpg',None,'Pediatric Cardiology lecture · slide 68'),
 'Ptet':(N+'peds-cardio/pc-tet-spell.jpg',(0,0.17,1,1),'Pediatric Cardiology lecture · slide 71 (A.D.A.M.)',[(0.63,0.64,0.87,0.74),(0.78,0.92,1,1)]),
 'Pcoarc':(N+'peds-cardio/pc-coarct-mra.jpg',None,'Pediatric Cardiology lecture · slide 49'),
 'Pring':(N+'peds-cardio/pc-ring-barium.jpg',None,'Pediatric Cardiology lecture · slide 63'),
 'Pvsd':(N+'peds-cardio/pc-vsd-echo.jpg',None,'Pediatric Cardiology lecture · slide 30',[(0.46,0.44,0.66,0.55,'black')]),
 'Ppsvt':(N+'peds-cardio/pc-psvt.jpg',(0,0.2,1,1),'Pediatric Cardiology lecture · slide 106'),
 'Phcm':(N+'peds-cardio/pc-hcm-echo.jpg',None,'Pediatric Cardiology lecture · slide 121'),
 'Peffcxr':(N+'peds-cardio/pc-effusion-cxr.jpg',(0,0,0.495,0.86),'Pediatric Cardiology lecture · slide 140 (Children\'s Hospital Boston)',[(0.14,0.76,0.33,0.85,'black')]),
 'Pbav':(N+'peds-cardio/pc-bav-or.jpg',(0.41,0.06,0.94,0.94),'Pediatric Cardiology lecture · slide 56'),
 'Aapdamur':(AM+'Heart murmur in patent ductus arteriosus.png',None,'AMBOSS'),
 'Aafixed':(AM+'Fixed split of S2.png',None,'AMBOSS'),
 'Aasinarr':(AM+'Normal ECG with sinus arrhythmia.png',(0,0.08,1,0.93),'AMBOSS'),
 'Aatriplet':(AM+'Premature ventricular complex (PVC) triplets.png',None,'AMBOSS'),
 'Aamonopvc':(AM+'Monomorphic premature ventricular complexes (PVCs).png',None,'AMBOSS'),
 'Aaapb':(AM+'Atrial premature beats.png',None,'AMBOSS'),
 'Aajaneway':(AM+'Janeway lesions.png',None,'AMBOSS (Wikimedia Commons, CC BY-SA 4.0)'),
 'Aaroth':(AM+'Roth spots.png',None,'AMBOSS (InTechOpen, CC BY 3.0)'),
 'Rbasd':(RB+'The Heart - 1e2ef88518bc5b63.png',None,'Robbins and Cotran Atlas of Pathology'),
 'Lwpw':(L+'img_wpw.gif',(0,0.25,1,1),'ecglibrary.com'),
 'Llqt':(L+'img_l_qt.gif',None,'ecglibrary.com'),
 # ---- Antiarrhythmic pharmacology ----
 'Aacornea':(AM+'Corneal microdeposits.png',None,'AMBOSS'),
 'Aaamiocxr':(AL+'asset-351.jpg',None,'AMBOSS'),
 'Xlupus':(N+'antiarrhythmic-pharm/aa-butterfly-rash.jpg',(0,0.13,1,1),'Scully lecture · slide 20 (illustration)'),
 'Aadigaf':(AM+'Atrial fibrillation with digitalis effect.png',None,'AMBOSS'),
 'Aasbrady':(AM+'Sinus bradycardia.png',None,'AMBOSS'),
 'Aachb':(AM+'Third-degree atrioventricular block (complete heart block).png',None,'AMBOSS'),
 # ---- Heart failure pharmacology ----
 'Aapedema':(AL+'asset-105.jpg',None,'AMBOSS'),
 'Aaflatt':(AM+'Flat T waves in hypokalemia.png',None,'AMBOSS'),
 'Aapeakt':(AM+'Peaked T waves in hyperkalemia.png',None,'AMBOSS'),
 'Aapitting':(AM+'Pitting edema of lower leg.png',None,'AMBOSS'),
 # ---- Ischemic heart disease pharmacology ----
 'Aaprinz':(AM+"Prinzmetal's variant angina (1 - 2).png",(0,0.08,1,1),'AMBOSS'),
 'Xach':(N+'ihd-pharm/ihd-acetylcholine.jpg',None,'Scully lecture · slide 14 (NEJM)',[(0,0,0.075,0.13),(0.495,0,0.575,0.13)]),
 'Aaedema':(AM+'Edema.png',None,'AMBOSS'),
 'Aatorsades':(AM+'Torsades de pointes.png',None,'AMBOSS (courtesy of Jason E. Roediger)'),
 # ---- Dyslipidemia pharmacology ----
 'Aaxanth':(AM+'Xanthelasma.png',None,'AMBOSS'),
 'Aalipemic':(AM+'Hypertriglyceridemia.png',None,'AMBOSS'),
 'Aagout':(AM+'Gouty tophi.png',None,'AMBOSS'),
 'Aaarcus':(AL+'asset-1194.jpg',None,'AMBOSS'),
 'Lhighk':(L+'img_highk.gif',None,'ecglibrary.com'),
 'Lhypok':(L+'img_hypok.gif',None,'ecglibrary.com'),
}
# small sources are upscaled so they don't show as thumbnails
UPSCALE={'Pkddesq':620,'Pboot':560,'Pring':520,'Peffcxr':520,'Xlupus':520,'Pkdface':560,'Pcoarc':560}
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
